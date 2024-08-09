### WARNING: This file is generated from octra. Do not edit. ###

# TODO: place above warning in cmake build
# File : setup.py

from distutils.core import Extension, setup

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


# name of module
name = "pyoctra"

# version of module
version = "0.1"

# specify the name of the extension and source files
# required to compile this
ext_modules = Extension(
    name="_pyoctra",
    swig_opts=["-c++"],
    language="c++",
    sources=[
        "pyoctra/octra/c/dynarray.c",
        "pyoctra/swig_src/pyoctra.i",  # all just in the header... TODO: figure out how to separate
        # "pyoctra/octra/cxx/dynarray.cxx",
    ],
)

setup(
    name=name,
    version=version,
    distclass=BinaryDistribution,
    cmdclass={"install": InstallPlatlib},
    packages=find_packages(),
    include_package_data=True,
    ext_modules=[ext_modules],
)
