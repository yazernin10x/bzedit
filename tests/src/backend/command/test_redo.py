import pytest

from src.backend.command import Redo
from src.backend.memento import Caretaker, Memento
from src.backend.core import Engine
from tests.fixtures.memento import engine, caretaker, memento


class TestRedo:
    @pytest.mark.parametrize(
        "engine, caretaker", [(None, Caretaker()), (Engine(), None)]
    )
    def test_init_none_engine_or_none_cartaker(
        self, engine: Engine, caretaker: Caretaker
    ) -> None:
        with pytest.raises(ValueError, match="engine or caretaker are required"):
            Redo(engine, caretaker)

    def test_execute(
        self, engine: Engine, caretaker: Caretaker, memento: Memento
    ) -> None:
        len_redo = len(caretaker._redo)
        Redo(engine, caretaker).execute()

        assert len(caretaker._redo) == len_redo - 1
        assert engine.buffer == memento.buffer
        assert engine.selection.start == memento.start
        assert engine.selection.end == memento.end + 1
