"""
The pyOctra library.
"""

__name__ = "pyoctra"

from .swig_src import pyoctra as octra


# import importlib
def simple_function():
    print("This is a simple function.")


__all__ = [
    "simple_function",
]
