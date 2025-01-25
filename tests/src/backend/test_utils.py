from src.backend.utils import reassign_module_names


def test_reassign_module_names() -> None:
    class DummyClass:
        pass

    dummy1 = DummyClass()
    dummy1.__module__ = "src.package.x.submodule"

    dummy2 = DummyClass()
    dummy2.__module__ = "src.package.y.submodule"

    dummy3 = DummyClass()
    dummy3.__module__ = "src.other_package.z.submodule"

    locals_ = {"dummy1": dummy1, "dummy2": dummy2}

    reassign_module_names("src.package", locals_)
    assert dummy1.__module__ == "src.package"
    assert dummy2.__module__ == "src.package"
    assert dummy3.__module__ == "src.other_package.z.submodule"
