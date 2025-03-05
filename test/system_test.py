import pytest
from .spack_commands import ALL_PACKAGES, spack_install


@pytest.mark.parametrize("package", ALL_PACKAGES)
def test_install(package: str):
    "Tests that the command 'spack install <package>' works."
    spack_install(package)
