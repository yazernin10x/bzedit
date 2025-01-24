from typing import Generator
import pytest
from pytest_mock import MockerFixture

from backend.core import Engine


@pytest.fixture
def engine(mocker: MockerFixture, request: pytest.FixtureRequest) -> Generator[Engine]:
    sut = Engine()
    buffer = request.param
    mocker.patch.object(sut, "_buffer", buffer)
    yield sut
