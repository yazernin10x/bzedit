"""Define global fixtures"""

from unittest.mock import PropertyMock, patch

import pytest

from src.backend.core._selection import Selection


@pytest.fixture
def engine(mocker, request):
    engine = mocker.patch("src.backend.core.Engine", autospec=True)
    engine = engine.return_value

    if hasattr(request, "param"):
        p = PropertyMock(return_value=f"{request.param}")
        type(engine).content = p

    yield engine


@pytest.fixture
def selection(engine):
    selection_path = "src.backend.core.Selection"
    with (
        patch(
            f"{selection_path}.buffer_begin", new_callable=PropertyMock
        ) as mock_buffer_begin,
        patch(
            f"{selection_path}.buffer_end", new_callable=PropertyMock
        ) as mock_buffer_end,
    ):
        mock_buffer_begin.return_value = 10
        mock_buffer_end.return_value = 100
        yield Selection(engine=engine)
