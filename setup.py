### WARNING: This file is generated from octra. Do not edit. ###

# File : setup.py

from distutils.core import Extension, setup

from setuptools.command.build_py import build_py as _build_py

# name of module
name = "pyoctra"

# version of module
version = "0.1"


from setuptools import find_packages, setup
from setuptools.dist import Distribution


class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

    def has_ext_modules(self):
        return True


from setuptools.command.install import install


class InstallPlatlib(install):
    def finalize_options(self):
        install.finalize_options(self)
        self.install_lib = self.install_platlib


class build_py(_build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()


# specify the name of the extension and source files
# required to compile this
ext_modules = Extension(
    name="_pyoctra",
    sources=["pyoctra/swig_src/pyoctra.i", "pyoctra/swig_src/octra/dynarray.c"],
    include_dirs=["pyoctra/swig_src", "pyoctra/swig_src/octra"],
    depends=["pyoctra/swig_src/octra/dynarray.h"],
)

setup(
    name=name,
    version=version,
    cmdclass={"build_py": build_py},
    # packages=["pyoctra"],
    # include_package_data=True,
    # package_data={"./pyoctra/swig_src/": ["*"], "./pyoctra/swig_src/": ["_pyoctra*"]},
    distclass=BinaryDistribution,
    # cmdclass={"install": InstallPlatlib},
    packages=find_packages(),
    package_data={
        "pyoctra": ["_pyoctra*"],
        "pyoctra": ["test.txt"],
    },
    include_package_data=True,
    ext_modules=[ext_modules],
)
