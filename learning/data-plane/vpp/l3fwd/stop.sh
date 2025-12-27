#!/usr/bin/env bash

# Copyright (c) 2023-2024, Arm Limited.
#
# SPDX-License-Identifier: Apache-2.0

set -e

SUFFIX=$(whoami)

options=(-o "hs:")
opts=$(getopt "${options[@]}" -- "$@")
eval set -- "$opts"

help_func() {
    echo "Usage: ./stop.sh options"
    echo
    echo "Options:"
    echo "  -s <suffix>  VPP directory name suffix (defaults to username)."
    echo "  -h           Show this message and quit."
    echo
}

while true; do
    case "$1" in
      -h)
        help_func
        exit 0
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

echo "Stop traffic and release VPP router & traffic generator instances..."

VPP_RT_PIDFILE="/run/vpp/${SUFFIX}/rt/vpp_rt.pid"
VPP_TG_PIDFILE="/run/vpp/${SUFFIX}/tg/vpp_tg.pid"

if [[ -f "${VPP_RT_PIDFILE}" ]];then
     kill -9 "$(cat "${VPP_RT_PIDFILE}")"
     rm "${VPP_RT_PIDFILE}"
fi

if [[ -f "${VPP_TG_PIDFILE}" ]];then
     kill -9 "$(cat "${VPP_TG_PIDFILE}")"
     rm "${VPP_TG_PIDFILE}"
fi

