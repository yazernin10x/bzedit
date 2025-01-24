import pytest
from src.backend.core import Engine, Selection


class TestEngine:
    """Testing the Engine class

    All tests are based on the text "I'm content in the buffer," defined in
    the engine fixture. The tests are performed at different positions in the
    buffer: at the beginning, in the middle, and at the end.
    """

    SAME_START_INDEX = (0, 0)
    SAME_MIDDLE_INDEX = (3, 3)
    SAME_END_INDEX = (25, 25)
    DIFF_INDEX = (4, 11)

    def test_selection(self, engine: Engine) -> None:
        assert isinstance(engine.selection, Selection)

    def test_buffer(self, engine: Engine) -> None:
        assert isinstance(engine.buffer, str)

    def test_clipboard(self, engine: Engine) -> None:
        assert isinstance(engine.clipboard, str)

    @pytest.mark.parametrize(
        "engine", [SAME_START_INDEX, SAME_MIDDLE_INDEX, SAME_END_INDEX], indirect=True
    )
    def test_copy_same_index(self, engine: Engine) -> None:
        engine.copy()
        assert engine.clipboard == ""

    @pytest.mark.parametrize("engine", [DIFF_INDEX], indirect=True)
    def test_copy_diff_index(self, engine: Engine) -> None:
        engine.copy()
        assert engine.clipboard == "content"

    @pytest.mark.parametrize(
        "engine", [SAME_START_INDEX, SAME_MIDDLE_INDEX, SAME_END_INDEX], indirect=True
    )
    def test_update_empty_text_same_index(self, engine: Engine) -> None:
        engine._update()
        assert engine.buffer == "I'm content in the buffer"

    @pytest.mark.parametrize("engine", [DIFF_INDEX], indirect=True)
    def test_update_empty_text_diff_index(self, engine: Engine) -> None:
        engine._update()
        assert engine.buffer == "I'm  in the buffer"

    @pytest.mark.parametrize("engine", [SAME_START_INDEX], indirect=True)
    def test_update_non_empty_text_same_index_start(self, engine: Engine) -> None:
        engine._update("Yes ! , ")
        assert engine.buffer == "Yes ! , I'm content in the buffer"

    @pytest.mark.parametrize("engine", [SAME_MIDDLE_INDEX], indirect=True)
    def test_update_non_empty_text_same_index_middle(self, engine: Engine) -> None:
        engine._update(" new")
        assert engine.buffer == "I'm new content in the buffer"

    @pytest.mark.parametrize("engine", [SAME_END_INDEX], indirect=True)
    def test_update_non_empty_text_same_index_end(self, engine: Engine) -> None:
        engine._update(" !")
        assert engine.buffer == "I'm content in the buffer !"

    @pytest.mark.parametrize("engine", [DIFF_INDEX], indirect=True)
    def test_update_non_empty_text_diff_index(self, engine: Engine) -> None:
        engine._update("new text")
        assert engine.buffer == "I'm new text in the buffer"

    def test_selected_range(self, engine: Engine) -> None:
        expected = (engine.selection.start, engine.selection.end)
        assert engine._selected_range() == expected
