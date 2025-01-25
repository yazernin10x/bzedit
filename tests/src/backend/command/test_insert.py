import pytest

from src.backend.core import Engine
from backend.command import Insert
from tests.fixtures.command import engine


class TestInsert:
    BUFFER = "Insert to the buffer."

    def test_none_engine(self) -> None:
        with pytest.raises(ValueError, match="engine is required"):
            Insert(None)

    @pytest.mark.parametrize("engine", [BUFFER], indirect=True)
    def test_execute(self, engine: Engine) -> None:
        Insert(engine, " the text ", 6, 6).execute()
        assert engine.clipboard == ""
        assert engine.buffer == "Insert the text to the buffer."
