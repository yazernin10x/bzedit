"""Define an implementation of the abstract class ``AbstractSelection``.

Classes
-------
``Selection``: AbstractSelection
    Implement the abstract class ``AbstractSelection``.

"""

from __future__ import annotations
import inspect

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
        self._begin = 0  # Selection begin index
        self._end = 0  # Selection end index

    @property
    def begin(self) -> int:
        return self._begin

    @begin.setter
    def begin(self, index: int) -> None:
        self._check_index(index)
        self._begin = index

    @property
    def end(self) -> int:
        return self._end

    @end.setter
    def end(self, index: int) -> None:
        self._check_index(index)
        self._end = index + 1

    @property
    def buffer_begin(self) -> int:
        return 0

    @property
    def buffer_end(self) -> int:
        content = self._engine.content
        return (len(content) - 1) if content else 0

    def _check_index(self, index: int):
        stack = inspect.stack()
        caller = stack[1].function
        if (index < 0) or (index < self.buffer_begin) or (index > self.buffer_end):
            raise IndexError(f"Invalid selection {caller} index")
