from __future__ import annotations
from abc import ABC, abstractmethod

from backend.core import Meta


class AbstractCaretaker(ABC, metaclass=Meta):
    """Save and restore the mementos representing the editor's states.

    This class manages the editor's state history for undo and redo operations.

    Methods
    -------
    save(memento: AbstractMemento) -> None
        Save the editor's current state.

    undo() -> AbstractMemento
        Restore the last modification made to the editor.

    redo() -> AbstractMemento
        Restore an undone operation in the editor.
    """

    @abstractmethod
    def save(self, memento: AbstractMemento) -> None:
        """Save the editor's current state.

        The saved state represents the editor's state at a specific point in
        time.

        Parameters
        ----------
        memento : AbstractMemento
            The memento representing the editor's state to be saved.

        Raises
        ------
        ValueError
            if `memento` is None.
        """
        ...

    @abstractmethod
    def undo(self) -> AbstractMemento:
        """
        Restores the last modification made to the editor.

        This operation removes the most recent state from the undo stack and moves it
        to the redo stack.

        Returns
        -------
        AbstractMemento
            The last saved memento, or `NullMemento` if the undo stack is empty.
        """
        ...

    @abstractmethod
    def redo(self) -> AbstractMemento:
        """Restores an undone operation on the editor.

        This operation retrieves the most recent state from the redo stack
        and adds it to the undo stack.

        Returns
        -------
        AbstractMemento
            The last undone memento, or `NullMemento` if the redo stack is
            empty.
        """
        ...
