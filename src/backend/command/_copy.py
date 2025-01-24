from __future__ import annotations

from backend.command import AbstractCommand


class Copy(AbstractCommand):
    """Copy text to clipboard

    Methods
    -------
    __init__(engine, start, end)
        Build the command
    """

    def __init__(self, engine: Engine, start: int, end: int) -> None:
        """Build the command

        Parameters
        ----------
        engine : Engine
            The editor engine from which to copy the text.

        begin : int
            The start index of the selection to copy.

        end : int
            The end index of the selection to copy.

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
        self._engine.copy()
