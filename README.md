# Stacky Spack

Clone this repo
```bash
git clone -c feature.manyFiles=true --recurse-submodules --shallow-submodules https://github.com/dominichofer/StackySpack.git
```

Source it with an upstream
```bash
. StackySpack/setup-env.sh /cluster/software/stacks/2025-06
. StackySpack/setup-env.sh /mch-environment/v86
. StackySpack/setup-env.sh $USER_ENV_ROOT
```
or none
```bash
. StackySpack/setup-env.sh
```
and enjoy [spack](https://spack.io/) on a software stack.

## Content
- `repo/`: Repository of package descriptions. Parallel to https://github.com/spack/spack/tree/v0.23.1/var/spack/repos/builtin
- `spack/`: Git submodule.
- `test/`: Framework to test package descriptions in `repo/`.
- `user-config/`: Configurations to make spack emit files only into this repo's directory, so it doesn't spill files. (Configured as "user" scope, as described in https://spack-tutorial.readthedocs.io/en/latest/tutorial_configuration.html#configuration-scopes)
- `setup-env.sh`: Main entry point. Sourcable script.

## Tesing + CI
Packages in `repo/packages` are automatically detected and tested with the framework in `test/`, which is triggered by `.github/workflows/spack_ci.yml`.
