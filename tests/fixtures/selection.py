from typing import Generator
import pytest
from pytest_mock import MockerFixture

from src.backend.core import Selection


@pytest.fixture
def engine(mocker: MockerFixture) -> Generator[Selection]:
    expected = "I'm buffer"
    sut = mocker.patch("src.backend.core.Engine", autospec=True)
    sut = sut.return_value
    p = mocker.PropertyMock(return_value=expected)
    type(sut).buffer = p

    return sut


@pytest.fixture
def selection(
    mocker: MockerFixture,
    engine: MockerFixture,
    request: pytest.FixtureRequest,
) -> Generator[Selection]:
    if hasattr(request, "param"):
        mock_buffer_end = mocker.patch(
            "src.backend.core.Selection.buffer_end", new_callable=mocker.PropertyMock
        )
        mock_buffer_end.return_value = request.param[0]
        engine.buffer = request.param[1]

    yield Selection(engine=engine)
