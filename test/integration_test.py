import pytest
import os
from .spack_commands import spack_info, spack_spec

packages_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "repo", "packages"
)

all_packages = [
    name
    for name in os.listdir(packages_dir)
    if os.path.isdir(os.path.join(packages_dir, name))
]


@pytest.mark.parametrize('package', all_packages)
def test_info(package: str):
    "Tests that the command 'spack info <package>' works for all packages."
    spack_info(package)


@pytest.mark.parametrize('package', all_packages)
def test_spec(package: str):
    "Tests that the command 'spack spec <package>' works for all packages."
    spack_info(package)

def test_spec_gridtools():
    spack_spec("gridtools ~cuda")
    spack_spec("gridtools +cuda")

def test_spec_int2lm():
    spack_spec("int2lm +parallel")
