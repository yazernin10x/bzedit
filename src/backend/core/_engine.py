"""Define an implementation of the abstract class ``AbstractEngine``.

Classes
-------
``Engine``
    Implement the abstract class ``AbstractEngine``.

"""

from src.backend.core import AbstractEngine, Selection


class Engine(AbstractEngine):
    """Implement the abstract class ``AbstractEngine``."""

    def __init__(self) -> None:
        """Initializes the engine.

        The engine is initialized with an empty buffer,
        an empty clipboard, and an initial selector.

        See Also
        --------
        Selection : Manage text selection.
        """
        self._clipboard = ""
        self._buffer = ""
        self._selection = Selection(self)

    @property
    def selection(self) -> Selection:
        return self._selection

    @property
    def buffer(self) -> str:
        return self._buffer

    @property
    def clipboard(self) -> str:
        return self._clipboard

    def cut(self) -> None:
        self.copy()
        self.delete()

    def paste(self) -> None:
        self.insert(self._clipboard)

    def insert(self, text: str) -> None:
        self._update(text)

    def delete(self) -> None:
        self._update()

    def copy(self) -> None:
        start, end = self._selected_range()
        self._clipboard = self._buffer[start:end]

    def _update(self, text: str = "") -> None:
        start, end = self._selected_range()
        self._buffer = "".join([self._buffer[:start], text, self._buffer[end:]])
        self._selection.start = self._selection.end = start + len(text)

    def _selected_range(self) -> tuple[int, int]:
        return self._selection.start, self._selection.end
