import unittest
from .spack_commands import spack_install


class CdoTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("cdo")


class ClangFormatTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("clang-format")


class CosmoEccodesDefinitionsTest(unittest.TestCase):
    def test_install_version_2_25_0_1(self):
        spack_install("cosmo-eccodes-definitions @2.25.0.1")

    def test_install_version_2_19_0_7(self):
        spack_install("cosmo-eccodes-definitions @2.19.0.7")


class FckitTest(unittest.TestCase):
    def test_install_0_9_0(self):
        spack_install("fckit@0.9.0")


class FdbTest(unittest.TestCase):
    def test_install_5_11_17_gcc(self):
        spack_install("fdb @5.11.17 %gcc")

    def test_install_5_11_17_nvhpc(self):
        # tests fail because compiler emitted warnings.
        spack_install("fdb @5.11.17 %nvhpc", test_root=False)


class FdbFortranTest(unittest.TestCase):
    def test_install(self):
        spack_install("fdb-fortran")


class FlexpartIfsTest(unittest.TestCase):
    def test_install_10_4_4(self):
        spack_install("flexpart-ifs @10.4.4")

    def test_install_fdb(self):
        spack_install("flexpart-ifs @fdb")


class FlexpartCosmoTest(unittest.TestCase):
    def test_install(self):
        spack_install("flexpart-cosmo @V8C4.0")


class GridToolsTest(unittest.TestCase):
    def test_install_version_1_1_3_gcc(self):
        spack_install("gridtools @1.1.3 %gcc")

    def test_install_version_1_1_3_nvhpc(self):
        spack_install("gridtools @1.1.3 %nvhpc")


class IconTest(unittest.TestCase):
    def test_install_2024_1_gcc(self):
        spack_install("icon @2024.1-1 %gcc")

    def test_install_2024_1_nvhpc(self):
        spack_install("icon @2024.1-1 %nvhpc")

    def test_install_conditional_dependencies(self):
        # +coupling triggers libfyaml, libxml2, netcdf-c
        # +rttov triggers rttov
        # serialization=create triggers serialbox
        # +cdi-pio triggers libcdi-pio, yaxt                   (but unfortunately this is broken)
        # +emvorado triggers eccodes, hdf5, zlib
        # +eccodes-definitions triggers cosmo-eccodes-definitions
        # +mpi triggers mpi
        # gpu=openacc+cuda triggers cuda
        spack_install(
            "icon @2024.1-1 %nvhpc +coupling +rttov serialization=create +emvorado +mpi gpu=openacc+cuda"
        )


class IconHamTest(unittest.TestCase):
    pass


class IconToolsTest(unittest.TestCase):
    def test_install_2_5_2(self):
        spack_install("icontools @2.5.2")


class Int2lmTest(unittest.TestCase):
    def test_install_version_3_00_gcc(self):
        spack_install("int2lm @int2lm-3.00 %gcc")

    def test_install_version_3_00_nvhpc(self):
        spack_install("int2lm @int2lm-3.00 %nvhpc")


class LibfyamlTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("libfyaml")


class LibTorchTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("libtorch")


class LibCdiPioTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("libcdi-pio")


class LibGrib1Test(unittest.TestCase):
    def test_install_version_22_01_2020(self):
        spack_install("libgrib1 @22-01-2020")


class Makedepf90Test(unittest.TestCase):
    def test_install(self):
        spack_install("makedepf90 @3.0.1")


class PyAsttokensTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-asttokens")


class PyBlackTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-black")


class PyBoltonsTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-boltons")


class PyCytoolzTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-cytoolz")


class PyDevtoolsTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-devtools")


class PyEditablesTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-editables")


class PyExecutingTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-executing")


class PyFactoryBoyTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-factory-boy")


class PyFprettifyTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-fprettify")


class PyFrozendictTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-frozendict")


class PyGridtoolsCppTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-gridtools-cpp")


class PyGt4pyTest(unittest.TestCase):
    def test_install_version_1_0_3_6(self):
        spack_install("py-gt4py @1.0.3.6")

    def test_install_version_1_0_3_5(self):
        spack_install("py-gt4py @1.0.3.5")


class PyHatchlingTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-hatchling")


class PyIcon4pyTest(unittest.TestCase):
    def test_install_version_0_0_10(self):
        spack_install("py-icon4py @0.0.10")

    def test_install_version_0_0_9(self):
        spack_install("py-icon4py @0.0.9")


class PyInflectionTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-inflection")


class PyIsortTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-isort")


class PyLarkTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-lark")


class PyNanobindTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-nanobind")


class PyNumpyTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-numpy")


class PyPathspecTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-pathspec")


class PyPytestTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-pytest")


class PyPytestFactoryboyTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-pytest-factoryboy")


class PySetuptoolsTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-setuptools")


class PySphinxcontribJqueryTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-sphinxcontrib-jquery")


class PyTabulateTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-tabulate")


class PyToolzTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-toolz")


class PyTypingExtensionsTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("py-typing-extensions")


class RttovTest(unittest.TestCase):
    def test_install_version_13_1_gcc(self):
        spack_install("rttov @13.1 %gcc")

    def test_install_version_13_1_nvhpc(self):
        spack_install("rttov @13.1 %nvhpc")


class ScalesPPMTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("scales-ppm")


class YaxtTest(unittest.TestCase):
    def test_install_default(self):
        spack_install("yaxt")
