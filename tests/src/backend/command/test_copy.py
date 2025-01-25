import pytest

from src.backend.core import Engine
from src.backend.command import Copy
from tests.fixtures.command import engine


class TestCopy:
    BUFFER = "Copy text to clipboard"

    def test_none_engine(self) -> None:
        with pytest.raises(ValueError, match="engine is required"):
            Copy(None)

    @pytest.mark.parametrize("engine", [BUFFER], indirect=True)
    def test_execute(self, engine: Engine) -> None:
        Copy(engine, 5, 11).execute()
        assert engine.clipboard == "text to"
        assert engine.buffer == self.BUFFER
