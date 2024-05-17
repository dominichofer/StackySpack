#!/bin/sh

parent_dir=$( cd "$(dirname "${BASH_SOURCE[0]:-${(%):-%x}}")" ; pwd -P )

if [[ "$#" == 1 ]]; then
    uenv="$1"
    export SPACK_SYSTEM_CONFIG_PATH="$uenv"/config
fi

export SPACK_USER_CONFIG_PATH="$parent_dir"/user-config
export SPACK_USER_CACHE_PATH="$parent_dir"/user-cache
. "$parent_dir"/spack/share/spack/setup-env.sh
spack external find --all > /dev/null 2>&1

if [[ -n "$uenv" ]]; then
    echo Spack configured with upstream "$uenv" .
else
    echo Spack configured with no upstream.
fi
