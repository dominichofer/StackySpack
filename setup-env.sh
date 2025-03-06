#!/bin/bash

parent_dir=$( cd "$(dirname "${BASH_SOURCE[0]:-${(%):-%x}}")" ; pwd -P )

# Override local configuration
# https://spack.readthedocs.io/en/latest/configuration.html#overriding-local-configuration
if [[ "$#" == 1 ]]; then
    export SPACK_SYSTEM_CONFIG_PATH="$1"/config
fi
export SPACK_USER_CONFIG_PATH="$parent_dir"/user-config
export SPACK_USER_CACHE_PATH="$parent_dir"/user-cache

. "$parent_dir"/spack/share/spack/setup-env.sh

if [[ "$#" == 1 ]]; then
    echo Spack configured with upstream "$1" .
else
    echo Spack configured with no upstream.
fi
