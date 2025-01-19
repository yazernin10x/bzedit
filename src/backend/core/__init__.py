from ._meta import DocstringInheritanceMeta
from ._abstractengine import AbstractEngine
from ._abstractselection import AbstractSelection
from ._selection import Selection
from ._engine import Engine

__all__ = [
    "DocstringInheritanceMeta",
    "AbstractEngine",
    "AbstractSelection",
    "Selection",
    "Engine",
]

# Adjust __module__ to show objects as part of the current package
for value in list(locals().values()):
    if getattr(value, "__module__", "").startswith(__name__):
        value.__module__ = __name__
