#!/usr/bin/env bash

# Copyright (c) 2023-2024, Arm Limited.
#
# SPDX-License-Identifier: Apache-2.0

set -e

export vppctl_binary

DIR=$(dirname "$0")
DATAPLANE_TOP=${DIR}/../..
# shellcheck source=../../tools/check-path.sh
. "${DATAPLANE_TOP}"/tools/check-path.sh
SUFFIX=$(whoami)


help_func()
{
    echo "Usage: ./traffic_monitor.sh options"
    echo
    echo "Options:"
    echo "  -t <duration>        time in seconds for testing (default 3 seconds)"
    echo "  -s <suffix>          VPP directory name suffix (defaults to username)."
    echo "  -h                   show this message and quit"
    echo
}

options=(-o "ht:s:")
opts=$(getopt "${options[@]}" -- "$@")
eval set -- "$opts"

test_duration=3

while true; do
    case "$1" in
      -h)
        help_func
        exit 0
        ;;
      -t)
        if ! [[ "$2" =~ ^[1-9][0-9]*$ ]]; then
            echo "error: \"-t\" requires correct test duration"
            help_func
            exit 1
        fi
        test_duration=$2
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

check_vppctl > /dev/null

SOCKFILE="/run/vpp/${SUFFIX}/rt/cli_rt.sock"

 "${vppctl_binary}" -s "${SOCKFILE}" clear interfaces
 "${vppctl_binary}" -s "${SOCKFILE}" clear run
echo "Letting VPP route packets for ${test_duration} seconds:"
for _ in $(seq "${test_duration}"); do
    echo -n "..$_"
    sleep 1
done

echo
echo
echo "=========="
 "${vppctl_binary}" -s "${SOCKFILE}" show interface
 "${vppctl_binary}" -s "${SOCKFILE}" show run
 

