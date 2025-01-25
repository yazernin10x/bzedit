from __future__ import annotations
from abc import ABC, abstractmethod

from backend.core import Meta


class AbstractOriginator(ABC, metaclass=Meta):
    """Base interface for originators.

    This abstract class defines methods for managing states
    and undo/redo operations within an editor.

    Methods
    --------
    save() -> AbstractMemento
        Saves the current state of the editor and returns an object
        representing that state.

    restore(memento: AbstractMemento) -> None
        Restore the editor's state.
    """

    @abstractmethod
    def save(self) -> AbstractMemento:
        """Save the current state of the editor.

        Returns
        -------
        AbstractMemento
            The object representing the saved state of the editor.
        """
        ...

    @abstractmethod
    def restore(self, memento: AbstractMemento) -> None:
        """Restore the editor's state.

        Based on the provided memento, the editor engine's buffer and the
        selection indices (start and end) are update.

        Parameters
        ----------
        memento : Memento
            A snapshot of the editor's state used to restore its buffer and selection.
        """
        ...
