"""Provide an abstract class for managing text selection within a buffer.

Classes
-------
``AbstractSelection``
    Abstract base class for managing text selection and buffer boundaries.
"""

from abc import ABC, ABCMeta, abstractmethod

from src.backend.core._meta import DocstringInheritanceMeta


class Meta(ABCMeta, DocstringInheritanceMeta): ...


class AbstractSelection(ABC, metaclass=Meta):
    """Manage text selection.

    Provides methods to manage the selection range and buffer boundaries.

    Properties
    ----------
    begin : int
        Get or set the index of the first character in the selection.
    end : int
        Get or set the index of the first character after the selection.
    buffer_begin : int
        Get the index of the first character in the buffer.
    buffer_end : int
        Get the index of the first "virtual" character after the buffer.
    """

    @property
    @abstractmethod
    def begin(self) -> int:
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

    @begin.setter
    @abstractmethod
    def begin(self, index: int) -> None: ...

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
    def end(self, index) -> None: ...

    @property
    @abstractmethod
    def buffer_begin(self) -> int:
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
