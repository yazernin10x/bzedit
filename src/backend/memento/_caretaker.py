from collections import deque
from typing import Deque

from src.backend.memento import AbstractMemento, AbstractCaretaker, NullMemento


class Caretaker(AbstractCaretaker):
    """Implement the abstract class ``AbstractCaretaker``."""

    def __init__(self) -> None:
        """Initialize the Caretaker.

        This constructor initializes the Caretaker with two empty stacks:
        one for actions to undo and another for actions to redo.

        Attributes
        ----------
        _undo : Deque[AbstractMemento]
            The stack of actions to undo.

        _redo : Deque[AbstractMemento]
            The stack of actions to redo.
        """
        self._undo: Deque[AbstractMemento] = deque()
        self._redo: Deque[AbstractMemento] = deque()

    def save(self, memento: AbstractMemento) -> None:
        if memento is None:
            raise ValueError("memento is required.")

        self._redo.clear()
        self._undo.append(memento)

    def undo(self) -> AbstractMemento:
        return self._move(self._undo, self._redo)

    def redo(self) -> AbstractMemento:
        return self._move(self._redo, self._undo)

    def _move(
        self,
        from_: Deque[AbstractMemento],
        to: Deque[AbstractMemento],
    ) -> AbstractMemento:
        """Move the memento from the 'from' stack to the 'to' stack.

        It is used in undo and redo operations.

        Parameters
        ----------
        from_ : Deque[AbstractMemento]
            The source stack from which to retrieve the memento.

        to : Deque[AbstractMemento]
            The destination stack to which the memento is moved.

        Returns
        -------
        AbstractMemento
            The moved memento, or `NullMemento` if the 'from' stack is empty.
        """
        if not from_:
            return NullMemento()

        memento = from_.pop()
        to.append(memento)
        return memento
