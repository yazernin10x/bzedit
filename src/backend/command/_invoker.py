from __future__ import annotations


class Invoker:
    """Invoke a command

    This class acts as an intermediary to invoke a command and trigger its
    execution.

    Methods
    -------
    invoke(command)
        Invoke the given command and trigger its execution.
    """

    @staticmethod
    def invoke(command: Command) -> None:
        """Invoke the given command and trigger its execution.

        Parameters
        ----------
        command : Command
            The command to invoke.

        Raises
        ------
        ValueError
            If `command` is `None`.
        """
        if command is None:
            raise ValueError("command is required")

        command.execute()
