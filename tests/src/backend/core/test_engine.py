import pytest

from src.backend.core import Engine, Selection
from tests.fixtures.engine import engine  # noqa: F401


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
    SAME_INDEX = [SAME_START_INDEX, SAME_MIDDLE_INDEX, SAME_END_INDEX]
    UPDATE_DEPENDENCIES = [
        "empty_text_same_index",
        "empty_text_diff_index",
        "same_index_start",
        "same_index_middle",
        "same_index_end",
        "diff_index",
    ]

    ###### Copy tests ######
    @pytest.mark.parametrize("engine", SAME_INDEX, indirect=True)
    @pytest.mark.dependency(name="copy_same_index")
    def test_copy_same_index(self, engine: Engine) -> None:
        engine.copy()
        assert engine.clipboard == ""

    @pytest.mark.parametrize("engine", [DIFF_INDEX], indirect=True)
    @pytest.mark.dependency(name="copy_diff_index")
    def test_copy_diff_index(self, engine: Engine) -> None:
        engine.copy()
        assert engine.clipboard == "content"

    ###### Update tests ######
    @pytest.mark.parametrize("engine", SAME_INDEX, indirect=True)
    @pytest.mark.dependency(name="empty_text_same_index")
    def test_update_empty_text_same_index(self, engine: Engine) -> None:
        engine._update()
        assert engine.buffer == "I'm content in the buffer"

    @pytest.mark.parametrize("engine", [DIFF_INDEX], indirect=True)
    @pytest.mark.dependency(name="empty_text_diff_index")
    def test_update_empty_text_diff_index(self, engine: Engine) -> None:
        engine._update()
        assert engine.buffer == "I'm  in the buffer"

    @pytest.mark.parametrize("engine", [SAME_START_INDEX], indirect=True)
    @pytest.mark.dependency(name="same_index_start")
    def test_update_non_empty_text_same_index_start(self, engine: Engine) -> None:
        engine._update("Yes ! , ")
        assert engine.buffer == "Yes ! , I'm content in the buffer"

    @pytest.mark.parametrize("engine", [SAME_MIDDLE_INDEX], indirect=True)
    @pytest.mark.dependency(name="same_index_middle")
    def test_update_non_empty_text_same_index_middle(self, engine: Engine) -> None:
        engine._update(" new")
        assert engine.buffer == "I'm new content in the buffer"

    @pytest.mark.parametrize("engine", [SAME_END_INDEX], indirect=True)
    @pytest.mark.dependency(name="same_index_end")
    def test_update_non_empty_text_same_index_end(self, engine: Engine) -> None:
        engine._update(" !")
        assert engine.buffer == "I'm content in the buffer !"

    @pytest.mark.parametrize("engine", [DIFF_INDEX], indirect=True)
    @pytest.mark.dependency(name="diff_index")
    def test_update_non_empty_text_diff_index(self, engine: Engine) -> None:
        engine._update("new text")
        assert engine.buffer == "I'm new text in the buffer"

    ###### Delete tests ######
    @pytest.mark.dependency(name="delete", depends=UPDATE_DEPENDENCIES)
    @pytest.mark.parametrize("engine", [DIFF_INDEX], indirect=True)
    def test_delete(self, engine: Engine) -> None:
        engine.delete()
        assert engine.buffer == "I'm  in the buffer"

    ###### Insert tests ######
    @pytest.mark.dependency(name="insert", depends=UPDATE_DEPENDENCIES)
    @pytest.mark.parametrize("engine", [DIFF_INDEX], indirect=True)
    def test_insert(self, engine: Engine) -> None:
        engine.insert("new text")
        assert engine.buffer == "I'm new text in the buffer"

    ###### Paste tests ######
    @pytest.mark.parametrize("engine", [DIFF_INDEX], indirect=True)
    @pytest.mark.dependency(name="paste", depends=["insert"])
    def test_paste(self, engine: Engine) -> None:
        engine._clipboard = "new text"
        engine.paste()
        assert engine.clipboard == "new text"
        assert engine.buffer == "I'm new text in the buffer"

    ###### Cut tests ######
    @pytest.mark.parametrize("engine", [DIFF_INDEX], indirect=True)
    @pytest.mark.dependency(
        name="cut", depends=["copy_same_index", "copy_diff_index", "delete"]
    )
    def test_cut(self, engine: Engine) -> None:
        engine.cut()
        assert engine.clipboard == "content"
        assert engine.buffer == "I'm  in the buffer"
