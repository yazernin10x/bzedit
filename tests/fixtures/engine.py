from typing import Generator

import pytest
from pytest_mock import MockerFixture

from src.backend.core._engine import Engine


@pytest.fixture
def engine(mocker: MockerFixture, request: pytest.FixtureRequest) -> Generator[Engine]:
    path = "src.backend.core.Selection"
    mock_start = mocker.patch(f"{path}.start", new_callable=mocker.PropertyMock)
    mock_end = mocker.patch(f"{path}.end", new_callable=mocker.PropertyMock)
    if hasattr(request, "param"):
        mock_start.return_value = request.param[0]
        mock_end.return_value = request.param[1]

    sut = Engine()
    sut._buffer = "I'm content in the buffer"
    yield sut
