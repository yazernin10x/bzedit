from __future__ import annotations

from backend.command import AbstractCommand


class Paste(AbstractCommand):
    """Paste text from clipboard to the buffer.

    Methods
    -------
    __init__(engine, start, end)
        Build the command
    """

    def __init__(self, engine: Engine, start: int = 0, end: int = 0) -> None:
        """Build the command

        Parameters
        ----------
        engine : Engine
            The editor engine from which to paste the text.

        start : int, default 0
            The start index of the selection to paste.

        end : int, default 0
            The end index of the selection to paste.

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
        self._engine.selection.start = start
        self._engine.selection.end = end

    def execute(self) -> None:
        self._engine.paste()
