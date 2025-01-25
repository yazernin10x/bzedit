from __future__ import annotations

from backend.command import AbstractCommand
from backend.memento import Originator


class Undo(AbstractCommand):
    """Efface la dernière modification apportée à l'éditeur.

    Methods
    -------
    __init__(engine, caretaker)
        Initialize the command
    """

    def __init__(self, engine: Engine, caretaker: Caretaker) -> None:
        """Initialize the Undo command.

        Parameters
        ----------
        engine : Engine
            The engine whose state is to be restored.

        caretaker : Caretaker
            The caretaker responsible for maintaining the engine's state.

        Raises
        ------
        ValueError
            If either `engine` or `caretaker` is None.

        See Also
        --------
        Originator
            Used to manage the state of the engine.
        """
        if engine is None or caretaker is None:
            raise ValueError("engine or caretaker are required")

        self._caretaker = caretaker
        self._originator = Originator(engine)

    def execute(self) -> None:
        self._originator.restore(self._caretaker.undo())
