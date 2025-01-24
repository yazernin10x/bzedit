"""Define an implementation of the abstract class ``AbstractSelection``.

Classes
-------
``Selection``: AbstractSelection
    Implement the abstract class ``AbstractSelection``.

"""

from __future__ import annotations

from src.backend.core import AbstractSelection


class Selection(AbstractSelection):
    """Implement the abstract class ``AbstractSelection``."""

    def __init__(self, engine: AbstractEngine) -> None:
        """Initialize the Selection object.

        Parameters
        ----------
        engine: AbstractEngine
            Editor engine for buffer management.
        """
        self._engine = engine
        self._start = 0  # Selection start index
        self._end = 0  # Selection end index

    @property
    def start(self) -> int:
        return self._start

    @start.setter
    def start(self, index: int) -> None:
        self._check_index(index)
        self._start = index

    @property
    def end(self) -> int:
        return self._end

    @end.setter
    def end(self, index: int) -> None:
        self._check_index(index)
        self._end = index + 1

    @property
    def buffer_start(self) -> int:
        return 0

    @property
    def buffer_end(self) -> int:
        return len(self._engine.buffer)

    def _check_index(self, index: int) -> None:
        if (index < 0) or (index > self.buffer_end):
            raise IndexError("Invalid selection index")
