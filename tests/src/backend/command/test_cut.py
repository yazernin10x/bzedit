import pytest

from src.backend.core import Engine
from backend.command import Cut
from tests.fixtures.command import engine


class TestCut:
    BUFFER = "Cut the text from the buffer."

    def test_none_engine(self) -> None:
        with pytest.raises(ValueError, match="engine is required"):
            Cut(None)

    @pytest.mark.parametrize("engine", [BUFFER], indirect=True)
    def test_execute(self, engine: Engine) -> None:
        Cut(engine, 12, len(self.BUFFER) - 2).execute()
        assert engine.clipboard == " from the buffer"
        assert engine.buffer == "Cut the text."
