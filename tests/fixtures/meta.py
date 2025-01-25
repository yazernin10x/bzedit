from typing import Generator

import pytest

from backend.core import DocstringInheritanceMeta

# mypy: disable-error-code=misc


@pytest.fixture
def dummy_class(request: pytest.FixtureRequest) -> Generator[object]:
    meta = DocstringInheritanceMeta if request.param else type

    class Dummy1(metaclass=meta):
        @property
        def t(self) -> None:
            "t in Dummy"
            ...

        def x(self) -> None:
            "x in Dummy"
            ...

    class Dummy2(metaclass=meta):
        @property
        def y(self) -> None:
            "y in DummyArtist"
            ...

        def z(self) -> None:
            "z in DummyArtist"
            ...

    class Dummpy(Dummy1, Dummy2):
        @property
        def t(self) -> None: ...

        def x(self) -> None: ...

        @property
        def y(self) -> None: ...

        def z(self) -> None: ...

    yield Dummpy
