"""Define metaclass"""

from abc import ABCMeta

# mypy: disallow-untyped-defs = false


class DocstringInheritanceMeta(type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if isinstance(attr_value, property) or callable(attr_value):
                for base in bases:
                    if base_attr := getattr(base, attr_name, None):
                        attr_value.__doc__ = base_attr.__doc__

        return super().__new__(cls, name, bases, dct)


class Meta(ABCMeta, DocstringInheritanceMeta): ...
