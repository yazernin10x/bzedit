from src.backend.core._selection import Selection

import pytest


class TestSelection:
    def test_begin_index_valid(self, selection):
        selection.begin = 20
        assert selection.begin == 20

    @pytest.mark.parametrize("index", [-25, 5, 110])
    def test_begin_index_invalid(self, selection, index):
        with pytest.raises(IndexError, match="Invalid selection begin index"):
            selection.begin = index

    def test_end_index_valid(self, selection):
        selection.end = 49
        assert selection.end == 50

    @pytest.mark.parametrize("index", [-25, 9, 102])
    def test_end_index_invalid(self, selection, index):
        with pytest.raises(IndexError, match="Invalid selection end index"):
            selection.end = index

    def test_buffer_begin(self, engine):
        sut = Selection(engine=engine)
        assert sut.buffer_begin == 0

    @pytest.mark.parametrize("engine", ["", "I'm content"], indirect=True)
    def test_buffer_end(self, engine):
        sut = Selection(engine=engine)
        expected = (len(engine.content) - 1) if engine.content else 0
        sut.buffer_end == expected
