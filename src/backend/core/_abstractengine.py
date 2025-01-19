"""Provide an abstract class for managing text editing operations in a buffer.

Classes
-------
``AbstractEngine``
    Abstract base class for the text editing engine, with methods to get the
    selection object, clipboard management, and text editing operations.
"""

from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod

from src.backend.core._meta import DocstringInheritanceMeta


class Meta(ABCMeta, DocstringInheritanceMeta): ...


class AbstractEngine(ABC, metaclass=Meta):
    """Manage buffer.

    Abstract class providing methods to get the selection object, clipboard
    content, and perform common text editing tasks such as cutting, copying,
    pasting, inserting, and deleting text.

    Properties
    ----------
    selection : Selection
        Provides selection control to manage portions of text in the buffer.
    content : str
        Provides access to the content of the buffer.
    clipboard_content : str
        Provides access to the content of the clipboard.

    Methods
    -------
    cut() -> None
        Copies the selected text to the clipboard and deletes it from the
        buffer.
    copy() -> None
        Copies the selected text to the clipboard.
    paste() -> None
        Pastes the clipboard content at the selection point and updates the
        buffer.
    insert(text: str) -> None
        Inserts the provided text into the buffer at the selection point.
    delete() -> None
        Deletes the contents of the selected text in the buffer.
    """

    @property
    @abstractmethod
    def selection(self) -> Selection:
        """Provide selection control.

        The selection control manages and manipulates portions of text in a
        buffer for operations like cutting, copying, or replacing.

        Returns
        -------
        Selection
            The selection control object
        """
        ...

    @property
    @abstractmethod
    def content(self) -> str:
        """Access the buffer's content.

        The buffer temporarily stores the text to allow operations such as
        insertion, modification, and deletion before saving.

        Returns
        -------
        str
            A copy of the buffer's contents.
        """
        ...

    @property
    @abstractmethod
    def clipboard_content(self) -> str:
        """Access the clipboard's content.

        The clipboard temporarily stores text for copy, cut, and paste
        operations.

        Returns
        -------
        str
            A copy of the clipboard's contents.
        """
        ...

    @abstractmethod
    def cut(self) -> None:
        """Cut the selected text.

        The text selected by the selection object is copied to the clipboard
        and then deleted from the buffer.
        """
        ...

    @abstractmethod
    def copy(self) -> None:
        """Copy the selected text.

        The text selected by the selection object is copied to the clipboard.
        """
        ...

    @abstractmethod
    def paste(self) -> None:
        """Paste the text from the clipboard at the selection point.

        The text selected by the selection object is replaced with the
        clipboard content, and the buffer is updated.
        """
        ...

    @abstractmethod
    def insert(self, text: str) -> None:
        """Insert a text into the buffer.

        Parameters
        ----------
        text: str
            The text to insert
        """
        ...

    @abstractmethod
    def delete(self) -> None:
        """Delete the contents of the selection in the buffer."""
        ...
