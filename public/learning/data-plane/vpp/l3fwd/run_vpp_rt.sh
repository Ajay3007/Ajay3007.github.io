#!/usr/bin/env bash

# Copyright (c) 2023-2024, Arm Limited.
#
# SPDX-License-Identifier: Apache-2.0

set -e

export vppctl_binary
export vpp_binary

DIR=$(dirname "$0")
DATAPLANE_TOP=${DIR}/../..
# shellcheck source=../../tools/check-path.sh
. "${DATAPLANE_TOP}"/tools/check-path.sh
SUFFIX=$(whoami)

help_func()
{
    echo "Usage: ./run_vpp_rt.sh options"
    echo
    echo "Options:"
    echo "  -c <core list>       set CPU affinity. Assign VPP main thread to 1st core"
    echo "                       in list and place worker threads on other listed cores."
    echo "                       Cores are separated by commas, and worker cores can"
    echo "                       include ranges."
    echo "  -m                   test via DPDK memif interface"
    echo "  -p <PCIe addresses>  test via DPDK physical NIC. Require input NIC port PCIe"
    echo "                       address followed by output NIC port PCIe address,"
    echo "                       separated by comma."
    echo "  -f <count>           number of flows with different IP destination addresses"
    echo "                       to route"
    echo "  -s <suffix>          VPP directory name suffix (defaults to username)."
    echo "  -h                   show this message and quit"
    echo
    echo "Example:"
    echo "  ./run_vpp_rt.sh -m -c 1,3-4,6 -f 10"
    echo "  ./run_vpp_rt.sh -p 0001:01:00.0,0001:01:00.1 -c 1,3-4,6 -f 10"
    echo
}

err_cleanup()
{
    echo "VPP router startup error, cleaning up..."
    if [[ -f "${VPP_PIDFILE}" ]]; then
        vpp_rt_pid=$(cat "${VPP_PIDFILE}")
         kill -9 "${vpp_rt_pid}"
         rm "${VPP_PIDFILE}"
    fi
    exit 1
}

cal_cores()
{
  IFS=',' read -ra array <<< "$1"

  count=0

  for item in "${array[@]}"; do
      if [[ $item == *-* ]]; then
          start=${item%-*}
          end=${item#*-}
          count=$((count + end - start + 1))
      else
          count=$((count + 1))
      fi
  done

  echo $count
}

flows_num=1

setup_iface()
{
     "${vppctl_binary}" -s "${SOCKFILE}" set int state Ethernet0 up
     "${vppctl_binary}" -s "${SOCKFILE}" create sub-interfaces Ethernet0 100
     "${vppctl_binary}" -s "${SOCKFILE}" set int ip address Ethernet0.100 10.0.0.10/32
     "${vppctl_binary}" -s "${SOCKFILE}" set int state Ethernet0.100 up
     "${vppctl_binary}" -s "${SOCKFILE}" set int state Ethernet1 up
     "${vppctl_binary}" -s "${SOCKFILE}" create sub-interfaces Ethernet1 100
     "${vppctl_binary}" -s "${SOCKFILE}" set int ip address Ethernet1.100 10.0.0.20/32
     "${vppctl_binary}" -s "${SOCKFILE}" set int state Ethernet1.100 up
     "${vppctl_binary}" -s "${SOCKFILE}" set ip neighbor Ethernet1.100 10.0.0.30 DD:DD:DD:DD:DD:DD
     "${vppctl_binary}" -s "${SOCKFILE}" ip route add 1.1.1.1/32 count "${flows_num}" via 10.0.0.30 Ethernet1.100

    LOG=$( "${vppctl_binary}" -s "${SOCKFILE}" show interface)
    if ! [[ "${LOG}" == *Ethernet0* && "${LOG}" == *Ethernet1* ]]; then
        echo "Failed to set up interfaces!"
        err_cleanup
    fi
}

options=(-o "hmp:c:f:s:")
opts=$(getopt "${options[@]}" -- "$@")
eval set -- "$opts"

while true; do
    case "$1" in
      -h)
          help_func
          exit 0
          ;;
      -m)
          memif_iface="1"
          shift 1
          ;;
      -p)
          phy_iface="1"
          PCIE_PATTERN='[0-9a-fA-F]{4}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.[0-9a-fA-F]'
          if ! [[ "$2" =~ ^${PCIE_PATTERN},${PCIE_PATTERN}$ ]];then
              echo "Incorrect PCIe addresses format: $2"
              help_func
              exit 1
          fi
          pcie_addr[0]=$(echo "$2" | cut -d "," -f 1)
          pcie_addr[1]=$(echo "$2" | cut -d "," -f 2)
          if [[ "${pcie_addr[0]}" == "${pcie_addr[1]}" ]]; then
              echo "error: \"-p\" option bad usage"
              help_func
              exit 1
          fi
          shift 2
          ;;
      -c)
        if ! [[ "$2" =~ ^[0-9]{1,3}((,[0-9]{1,3})|(,[0-9]{1,3}-[0-9]{1,3}))+$ ]]; then
            echo "error: \"-c\" requires correct isolated cpu core id"
            help_func
            exit 1
        fi
        main_core=$(echo "$2" | cut -d "," -f 1)
        worker_cores=$(echo "$2" | cut -d "," -f 2-)
        if [[ "${main_core}" == "${worker_cores}" ]]; then
            echo "error: \"-c\" option bad usage"
            help_func
            exit 1
        fi
        queues_count=$(cal_cores "$worker_cores")
        shift 2
        ;;
      -f)
        if ! [[ "$2" =~ ^[1-9][0-9]*$ ]]; then
            echo "error: \"-f\" requires correct number of flows"
            help_func
            exit 1
        fi
        flows_num=$2
        shift 2
        ;;
      -s)
        if [[ -z "$2" ]]; then
            echo "error: \"-s\" requires suffix"
            help_func
            exit 1
        fi
          SUFFIX="$2"
          shift 2
          ;;
      --)
          shift
          break
          ;;
      *)
          echo "Invalid Option!!"
          help_func
          exit 1
          ;;
    esac
done

if [[ "${memif_iface}" && "${phy_iface}" ]]; then
    echo "Can't support both -m and -p at the same time!!"
    help_func
    exit 1
fi

if ! [[ "${memif_iface}" || "${phy_iface}" ]]; then
    echo "require an option: \"-m\" or \"-p\""
    help_func
    exit 1
fi

VPP_RUNTIME_DIR="/run/vpp/${SUFFIX}/rt"
VPP_PIDFILE="${VPP_RUNTIME_DIR}/vpp_rt.pid"
SOCKFILE="${VPP_RUNTIME_DIR}/cli_rt.sock"
#SOCKFILE="/run/vpp/root/rt/cli_rt.sock"
MEMIF_SOCKET1="/tmp/memif_dut_1-${SUFFIX}"
MEMIF_SOCKET2="/tmp/memif_dut_2-${SUFFIX}"

check_vpp > /dev/null
check_vppctl > /dev/null

if [[ -n "$memif_iface" ]]; then
     "${vpp_binary}" unix "{ runtime-dir ${VPP_RUNTIME_DIR} cli-listen ${SOCKFILE} pidfile ${VPP_PIDFILE} }"   \
                         cpu "{ main-core ${main_core} corelist-workers ${worker_cores} }"                         \
                         plugins "{ plugin default { disable } plugin dpdk_plugin.so { enable } }"                 \
                         dpdk "{ no-pci single-file-segments dev default {num-tx-queues ${queues_count} num-rx-queues ${queues_count} }
                                 vdev net_memif0,role=client,id=1,socket-abstract=no,socket=${MEMIF_SOCKET1},mac=c6:ce:78:fe:5f:77,zero-copy=yes
                                 vdev net_memif1,role=client,id=1,socket-abstract=no,socket=${MEMIF_SOCKET2},mac=c6:ce:78:fe:5f:78,zero-copy=yes }"
fi

if [[ -n "$phy_iface" ]]; then
     "${vpp_binary}" unix "{ runtime-dir ${VPP_RUNTIME_DIR} cli-listen ${SOCKFILE} pidfile ${VPP_PIDFILE} }"   \
                         cpu "{ main-core ${main_core} corelist-workers ${worker_cores} }"                         \
                         plugins "{ plugin default { disable } plugin dpdk_plugin.so { enable } }"                 \
                         dpdk "{ dev default {num-tx-queues ${queues_count} num-rx-queues ${queues_count} }
                                 dev ${pcie_addr[0]} { name Ethernet0 } dev ${pcie_addr[1]} { name Ethernet1 } }"
fi

echo "VPP router starting up"
sleep 5

# Disable "Exit on Error" temporarily to allow vppctl to try connection several
# times for slow starting up VPP on some platforms.
set +e
max_conn_retries=10

echo "SOCKFILE=${SOCKFILE}"
for conn_count in $(seq ${max_conn_retries}); do
    if ! output=$( "${vppctl_binary}" -s "${SOCKFILE}" show threads) ; then
        if [[ ${conn_count} -eq ${max_conn_retries} ]]; then
            err_cleanup
        fi
        sleep 0.5
    elif [[ -z "${output}" ]]; then
        err_cleanup
    else
        break
    fi
done

set -e

echo "Setting up interfaces and routes..."
setup_iface
echo "Successfully start VPP router!"
