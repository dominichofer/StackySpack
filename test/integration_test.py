import pytest
from .spack_commands import ALL_PACKAGES, spack_info, spack_spec


@pytest.mark.parametrize("package", ALL_PACKAGES)
def test_info(package: str):
    "Tests that the command 'spack info <package>' works."
    spack_info(package)


@pytest.mark.parametrize("package", ALL_PACKAGES)
def test_spec(package: str):
    "Tests that the command 'spack spec <package>' works."
    spack_spec(package)
