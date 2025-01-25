import pytest
from pytest_mock import MockFixture

from backend.command import Paste
from src.backend.core import Engine
from tests.fixtures.command import engine


class TestPaste:
    BUFFER = "Paste text to the buffer."

    def test_none_engine(self) -> None:
        with pytest.raises(ValueError, match="engine is required"):
            Paste(None, 1, 1)

    @pytest.mark.parametrize("engine", [BUFFER], indirect=True)
    def test_execute(self, mocker: MockFixture, engine: Engine) -> None:
        mocker.patch.object(engine, "_clipboard", " from the clipboard ")
        Paste(engine, 10, 10).execute()
        assert engine.buffer == "Paste text from the clipboard to the buffer."
