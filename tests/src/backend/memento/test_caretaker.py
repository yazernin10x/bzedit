from collections import deque

import pytest

from src.backend.memento import Caretaker, Memento
from src.backend.memento._caretaker import NullMemento  # type: ignore
from tests.fixtures.memento import caretaker, memento


class TestCaretaker:
    def test_save_none_memento(self, caretaker: Caretaker) -> None:
        with pytest.raises(ValueError, match="memento is required"):
            caretaker.save(None)  # type: ignore

    def test_save_non_none_memento(
        self, caretaker: Caretaker, memento: Memento
    ) -> None:
        len_undo = len(caretaker._undo)
        caretaker.save(memento)
        assert not caretaker._redo
        assert caretaker._undo and (len(caretaker._undo) == len_undo + 1)

    @pytest.mark.dependency(name="move_empty")
    def test_move_empty_from_stack(self, caretaker: Caretaker) -> None:
        response = caretaker._move(deque(), caretaker._redo)
        assert isinstance(response, NullMemento)

    @pytest.mark.dependency(name="move_non_empty")
    def test_move_non_empty_from_stack(self, caretaker: Caretaker) -> None:
        len_undo = len(caretaker._undo)
        len_redo = len(caretaker._redo)

        caretaker._move(caretaker._undo, caretaker._redo)
        assert len(caretaker._undo) == len_undo - 1
        assert len(caretaker._redo) == len_redo + 1

    @pytest.mark.dependency(depends=["move_empty", "move_non_empty"])
    def test_undo(self, caretaker: Caretaker) -> None:
        len_undo = len(caretaker._undo)
        len_redo = len(caretaker._redo)

        caretaker.undo()
        assert len(caretaker._undo) == len_undo - 1
        assert len(caretaker._redo) == len_redo + 1

    @pytest.mark.dependency(depends=["move_empty", "move_non_empty"])
    def test_redo(self, caretaker: Caretaker) -> None:
        len_undo = len(caretaker._undo)
        len_redo = len(caretaker._redo)

        caretaker.redo()
        assert len(caretaker._undo) == len_undo + 1
        assert len(caretaker._redo) == len_redo - 1
