"""Define global fixtures"""

from typing import Generator

import pytest
from pytest_mock import MockerFixture

from backend.core import Engine, Selection


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


@pytest.fixture
def selection(
    mocker: MockerFixture, request: pytest.FixtureRequest
) -> Generator[Selection]:
    engine = mocker.patch("src.backend.core.Engine", autospec=True)
    engine = engine.return_value

    if hasattr(request, "param"):
        mock_buffer_end = mocker.patch(
            "src.backend.core.Selection.buffer_end", new_callable=mocker.PropertyMock
        )
        mock_buffer_end.return_value = request.param[0]

        p = mocker.PropertyMock(return_value=f"{request.param[1]}")
        type(engine).buffer = p

    yield Selection(engine=engine)
