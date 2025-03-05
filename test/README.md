The tests are segmented according to the following idea: There's code in spack, there's code in this repo, and there's code in the packages.
Neither testing spack, nor testing the packages, is the responsibility of this repo.
Testing this repo and the integration with spack and the packages is this repo's responsibility.

# Unit tests
They test this repo.
They run without a spack instance. They do not test spack, nor packages.

# Integration tests
They test the integration of this repo with spack.
They do not test packages. They test package descriptions.

# System tests
They test the collaboration of this repo, spack, and the packages.
