import pytest

from src.backend.core import Engine
from src.backend.command import Copy, Invoker
from tests.fixtures.command import engine


class TestInvoker:
    BUFFER = "Copy text to clipboard"

    def test_none_command(self) -> None:
        with pytest.raises(ValueError, match="command is required"):
            Invoker.invoke(None)

    @pytest.mark.parametrize("engine", [BUFFER], indirect=True)
    def test_execute(self, engine: Engine) -> None:
        Invoker.invoke(Copy(engine, 5, 11))
        assert engine.clipboard == "text to"
        assert engine.buffer == self.BUFFER
