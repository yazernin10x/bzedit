from __future__ import annotations

from backend.command import AbstractCommand


class Insert(AbstractCommand):
    """Insert text to the buffer.

    Methods
    -------
    __init__(engine, start, end)
        Build the command
    """

    def __init__(
        self, engine: Engine, text: str = "", start: int = 0, end: int = 0
    ) -> None:
        """Build the command

        Parameters
        ----------
        engine : Engine
            The editor engine from which to insert the text.

        text: str, default ""
            The text to insert into the editor's buffer.

        start : int, default 0
            The start index of the selection to insert.

        end : int, default 0
            The end index of the selection to insert.

        Raises
        ------
        ValueError
            If `engine` is `None`

        See Also
        --------
        Engine: Implement the abstract class ``AbstractEngine``.
        """
        if engine is None:
            raise ValueError("engine is required")

        self._engine = engine
        self._text = text
        self._engine.selection.start = start
        self._engine.selection.end = end

    def execute(self) -> None:
        self._engine.insert(self._text)
