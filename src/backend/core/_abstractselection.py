"""Provide an abstract class for managing text selection within a buffer.

Classes
-------
``AbstractSelection``
    Abstract base class for managing text selection and buffer boundaries.
"""

from __future__ import annotations
from abc import ABC, abstractmethod

from src.backend.core import Meta


class AbstractSelection(ABC, metaclass=Meta):
    """Manage text selection.

    Provides methods to manage the selection range and buffer boundaries.

    Properties
    ----------
    start : int
        Get or set the index of the first character in the selection.

    end : int
        Get or set the index of the first character after the selection.

    engine: Engine
        Provide the editor's engine used by the selection

    buffer_start : int
        Get the index of the first character in the buffer.

    buffer_end : int
        Get the index of the first "virtual" character after the buffer.
    """

    @property
    @abstractmethod
    def start(self) -> int:
        """Get or set the index of the first character in the selection.

        Returns
        -------
        int
            The index of the first character in the selection.

        Raises
        ------
        IndexError
            If the provided `index` is out of the buffer's bounds
            (for the setter).
        """
        ...

    @start.setter
    @abstractmethod
    def start(self, index: int) -> None: ...

    @property
    @abstractmethod
    def end(self) -> int:
        """Get or set the index of the first character after the selection.

        Returns
        -------
        int
            The index immediately after the last character in the selection.

        Raises
        ------
        ValueError
            If the provided `index` is out of the buffer's bounds
            (for the setter).
        """
        ...

    @end.setter
    @abstractmethod
    def end(self, index: int) -> None: ...

    @property
    @abstractmethod
    def engine(self) -> Engine:
        """Provide the editor's engine.

        Returns
        -------
        Engine
            The editor's engine used by the selection
        """
        ...

    @property
    @abstractmethod
    def buffer_start(self) -> int:
        """Get the index of the first character in the buffer.

        Returns
        -------
        int
            The index of the first character in the buffer.
        """
        ...

    @property
    @abstractmethod
    def buffer_end(self) -> int:
        """Get the index of the first "virtual" character after the buffer.

        Returns
        -------
        int
            The index immediately after the last character in the buffer.
        """
        ...
