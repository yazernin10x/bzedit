import pytest

from src.backend.core import Selection, Engine
from tests.fixtures.selection import selection, engine, selection_check_index


class TestSelection:
    """Test the Selection class

    For the tests of the `_check_index` method, different scenarios are
    evaluated, whether the buffer is empty or not.
    To get a value beyond ``buffer_end``, whether the buffer is empty or not,
    we use ``BUFFER_END_NON_EMPTY_TEXT + 1``.
    """

    TEXT = "I'm content in the buffer"
    SELECTION_START = 10
    SELECTION_END = 10
    BUFFER_END_EMPTY_TEXT = 0
    BUFFER_END_NON_EMPTY_TEXT = len(TEXT)
    SELECTION_START_AFTER_CREATION = 0

    def test_start_getter(self, selection: Selection) -> None:
        assert selection.start == self.SELECTION_START_AFTER_CREATION

    def test_start_setter(self, selection_check_index: Selection) -> None:
        selection_check_index.start = self.SELECTION_START
        assert selection_check_index.start == self.SELECTION_START

    def test_end_getter(self, selection: Selection) -> None:
        assert selection.end == self.SELECTION_START_AFTER_CREATION

    def test_end_setter(self, selection_check_index: Selection) -> None:
        selection_check_index.end = self.SELECTION_END
        assert selection_check_index.end == self.SELECTION_END + 1

    def test_engine(self, selection: Selection) -> None:
        assert isinstance(selection.engine, Engine)

    def test_buffer_start(self, selection: Selection) -> None:
        assert selection.buffer_start == self.SELECTION_START_AFTER_CREATION

    def test_buffer_end(self, engine: Engine) -> None:
        sut = Selection(engine=engine)
        assert sut.buffer_end == len(sut.engine.buffer)

    @pytest.mark.parametrize("index", [-2, BUFFER_END_NON_EMPTY_TEXT + 1])
    @pytest.mark.parametrize(
        "selection",
        [(BUFFER_END_EMPTY_TEXT, ""), (BUFFER_END_NON_EMPTY_TEXT, TEXT)],
        indirect=True,
    )
    def test_check_index_outbound(self, selection: Selection, index: int) -> None:
        """Test the out-of-bounds index."""

        with pytest.raises(IndexError, match="Invalid selection index"):
            selection._check_index(index)

    @pytest.mark.parametrize("index", [0])
    @pytest.mark.parametrize(
        "selection",
        [(BUFFER_END_EMPTY_TEXT, ""), (BUFFER_END_NON_EMPTY_TEXT, TEXT)],
        indirect=True,
    )
    def test_check_index_empty_buffer_zero_index(
        self, selection: Selection, index: int
    ) -> None:
        """Test the index 0."""
        assert selection._check_index(index) is None  # type: ignore[func-returns-value]

    @pytest.mark.parametrize("index", [BUFFER_END_NON_EMPTY_TEXT - 1])
    @pytest.mark.parametrize(
        "selection", [(BUFFER_END_NON_EMPTY_TEXT, TEXT)], indirect=True
    )
    def test_check_index_empty_buffer_positive_inbound(
        self, selection: Selection, index: int
    ) -> None:
        """Test the index located within the buffer's index range."""
        assert selection._check_index(index) is None  # type: ignore[func-returns-value]
