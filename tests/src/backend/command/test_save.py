import pytest

from src.backend.command import Save
from src.backend.memento import Caretaker
from src.backend.core import Engine
from tests.fixtures.memento import engine, caretaker, memento


class TestSave:
    @pytest.mark.parametrize(
        "engine, caretaker",
        [(None, Caretaker()), (Engine(), None), (None, None)],
    )
    def test_init_none_engine_or_none_cartaker(
        self, engine: Engine, caretaker: Caretaker
    ) -> None:
        with pytest.raises(ValueError, match="engine or caretaker are required"):
            Save(engine, caretaker)

    def test_execute(self, engine: Engine, caretaker: Caretaker) -> None:
        len_undo = len(caretaker._undo)

        Save(engine, caretaker).execute()

        assert len(caretaker._undo) == len_undo + 1
        assert len(caretaker._redo) == 0
