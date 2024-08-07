"""
The pyOctra library.

"""

__name__ = "pyoctra"

from .swig_src.pyoctra import *


# import importlib
def simple_function():
    print("This is a simple function.")


__all__ = [
    "simple_function",
]
