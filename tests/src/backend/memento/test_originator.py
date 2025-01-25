from src.backend.memento import Originator, Memento
from tests.fixtures.memento import originator, memento, engine


class TestOriginator:
    def test_save(self, originator: Originator) -> None:
        memento = originator.save()
        engine = originator._engine
        selection = originator._engine.selection
        assert memento.buffer == engine.buffer
        assert memento.start == selection.start
        assert memento.end == selection.end

    def test_restore(self, originator: Originator, memento: Memento) -> None:
        originator.restore(memento)
        engine = originator._engine
        selection = originator._engine.selection
        assert memento.buffer == engine.buffer
        assert memento.start == selection.start
        assert memento.end + 1 == selection.end
