from __future__ import annotations

from src.backend.memento import AbstractOriginator
from src.backend.memento import Memento


class Originator(AbstractOriginator):
    """Implement the abstract class ``AbstractOriginator``."""

    def __init__(self, engine: Engine):
        """Initialize the Originator.

        Constructs an object with the engine whose state is to be saved.

        Parameters
        ----------
        engine : Engine
            The engine whose state is to be saved.
        """
        self._engine = engine

    def save(self) -> AbstractMemento:
        return Memento(
            self._engine.buffer,
            self._engine.selection.start,
            self._engine.selection.end,
        )

    def restore(self, memento: Memento) -> None:
        selection = self._engine.selection
        selection.start = selection.buffer_start
        selection.end = selection.buffer_end

        self._engine.insert(memento.buffer)
        selection.start = memento.start
        selection.end = memento.end
