import pytest

from src.backend.core import Engine
from backend.command import Delete
from tests.fixtures.command import engine


class TestDelete:
    BUFFER = "Delete the text from the buffer."

    def test_none_engine(self) -> None:
        with pytest.raises(ValueError, match="engine is required"):
            Delete(None)

    @pytest.mark.parametrize("engine", [BUFFER], indirect=True)
    def test_execute(self, engine: Engine) -> None:
        Delete(engine, 15, len(self.BUFFER) - 2).execute()
        assert engine.clipboard == ""
        assert engine.buffer == "Delete the text."
