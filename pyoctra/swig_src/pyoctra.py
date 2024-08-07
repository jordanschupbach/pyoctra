# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _pyoctra
else:
    import _pyoctra

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class DynArrayInt(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _pyoctra.delete_DynArrayInt

    def push_back(self, *args):
        return _pyoctra.DynArrayInt_push_back(self, *args)

    def clear(self):
        return _pyoctra.DynArrayInt_clear(self)

    def size(self):
        return _pyoctra.DynArrayInt_size(self)

    def __init__(self, *args):
        _pyoctra.DynArrayInt_swiginit(self, _pyoctra.new_DynArrayInt(*args))

# Register DynArrayInt in _pyoctra:
_pyoctra.DynArrayInt_swigregister(DynArrayInt)
class DynArrayDouble(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _pyoctra.delete_DynArrayDouble

    def push_back(self, *args):
        return _pyoctra.DynArrayDouble_push_back(self, *args)

    def clear(self):
        return _pyoctra.DynArrayDouble_clear(self)

    def size(self):
        return _pyoctra.DynArrayDouble_size(self)

    def __init__(self, *args):
        _pyoctra.DynArrayDouble_swiginit(self, _pyoctra.new_DynArrayDouble(*args))

# Register DynArrayDouble in _pyoctra:
_pyoctra.DynArrayDouble_swigregister(DynArrayDouble)

def __lshift__(*args):
    return _pyoctra.__lshift__(*args)


