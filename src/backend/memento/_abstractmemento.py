from dataclasses import dataclass
from abc import ABC

from backend.core import Meta


@dataclass(frozen=True, slots=True)
class AbstractMemento(ABC, metaclass=Meta):
    """Records the state of the editor.

    This class encapsulates the state of the editor, including the buffer
    and the selection indices.

    Attributes
    ----------
    buffer : str
        The editor's buffer.
    start : int
        The starting index of the selection.
    end : int
        The ending index of the selection.
    """

    buffer: str
    start: int
    end: int
