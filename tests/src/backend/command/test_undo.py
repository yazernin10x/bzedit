import pytest

from src.backend.command import Undo
from src.backend.memento import Caretaker, Memento
from src.backend.core import Engine
from tests.fixtures.memento import engine, caretaker, memento


class TestUndo:
    @pytest.mark.parametrize(
        "engine, caretaker",
        [(None, Caretaker()), (Engine(), None), (None, None)],
    )
    def test_init_none_engine_or_none_cartaker(
        self, engine: Engine, caretaker: Caretaker
    ) -> None:
        with pytest.raises(ValueError, match="engine or caretaker are required"):
            Undo(engine, caretaker)

    def test_execute(
        self, engine: Engine, caretaker: Caretaker, memento: Memento
    ) -> None:
        len_undo = len(caretaker._undo)
        Undo(engine, caretaker).execute()

        assert len(caretaker._undo) == len_undo - 1
        assert engine.buffer == memento.buffer
        assert engine.selection.start == memento.start
        assert engine.selection.end == memento.end + 1
