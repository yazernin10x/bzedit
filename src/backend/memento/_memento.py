from dataclasses import dataclass, field

from src.backend.memento import AbstractMemento


@dataclass(frozen=True, slots=True)
class Memento(AbstractMemento):
    """Implement the abstract class AbstractMemento"""

    ...


@dataclass(frozen=True, slots=True)
class NullMemento(AbstractMemento):
    """Implement the abstract class AbstractMemento"""

    buffer: str = field(default="", init=False)
    start: int = field(default=0, init=False)
    end: int = field(default=0, init=False)
