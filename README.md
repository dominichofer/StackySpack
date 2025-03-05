# Stacky Spack

Clone this repo
```bash
git clone -c feature.manyFiles=true --recurse-submodules --shallow-submodules https://github.com/dominichofer/StackySpack.git
```

Source it with an upstream
```bash
. StackySpack/setup-env.sh /cluster/project/sis/hpc/software/2025-03
. StackySpack/setup-env.sh /mch-environment/v86
. StackySpack/setup-env.sh $USER_ENV_ROOT
```
or none
```bash
. StackySpack/setup-env.sh
```
and enjoy spack on a software stack.

Packages in "repo/packages" are automatically detected and tested.
