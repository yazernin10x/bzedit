from collections import deque
from typing import Generator

from backend.memento._originator import Originator
import pytest
from pytest_mock import MockerFixture

from src.backend.memento import Caretaker, Memento
from src.backend.core import Engine


@pytest.fixture
def memento(mocker: MockerFixture) -> Generator[Memento]:
    mem = mocker.patch("src.backend.memento.Memento", autospec=True)
    mem = mem.return_value
    mem.buffer = "I'm buffer in memento"
    mem.start = 4
    mem.end = 9
    yield mem


@pytest.fixture
def caretaker(mocker: MockerFixture, memento: Memento) -> Generator[Caretaker]:
    sut = Caretaker()
    mocker.patch.object(sut, "_redo", deque([memento, memento]))
    mocker.patch.object(sut, "_undo", deque([memento, memento, memento]))
    yield sut


@pytest.fixture
def engine() -> Generator[Engine]:
    engine = Engine()
    engine._buffer = "I'm buffer"
    engine.selection.start = 1
    engine.selection.end = 3
    yield engine


@pytest.fixture
def originator(engine: Engine) -> Generator[Originator]:
    yield Originator(engine)
