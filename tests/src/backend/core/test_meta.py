from __future__ import annotations

import pytest

from tests.fixtures.meta import dummy_class

# mypy: disable-error-code=name-defined
# ruff: noqa: F821


class TestMeta:
    @pytest.mark.parametrize("dummy_class", [False], indirect=True)
    def test_without_metaclass(self, dummy_class: Dummpy) -> None:  # type: ignore
        assert dummy_class.t.__doc__ is None
        assert dummy_class.x.__doc__ is None
        assert dummy_class.y.__doc__ is None
        assert dummy_class.z.__doc__ is None

    @pytest.mark.parametrize("dummy_class", [True], indirect=True)
    def test_with_metaclass(self, dummy_class: Dummpy) -> None:  # type: ignore
        assert dummy_class.t.__doc__ == "t in Dummy"
        assert dummy_class.x.__doc__ == "x in Dummy"
        assert dummy_class.y.__doc__ == "y in DummyArtist"
        assert dummy_class.z.__doc__ == "z in DummyArtist"
