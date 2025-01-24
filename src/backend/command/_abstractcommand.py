from abc import ABC, abstractmethod

from src.backend.core import Meta


class AbstractCommand(ABC, metaclass=Meta):
    """Abstract base class for all commands.

    Methods
    -------
    execute()
        Call a feature of the receiver.
    """

    @abstractmethod
    def execute(self) -> None:
        """Call a feature of the receiver.

        The receiver is the class that contains the business logic.

        See Also
        --------
        engine: Implement the abstract class ``AbstractEngine``."
        """
        ...
