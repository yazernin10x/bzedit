def reassign_module_names() -> None:
    """Reassign the `__module__` attribute of objects to the current package.

    This function iterates through all local objects and adjusts their
    `__module__` attribute if it starts with the name of the current module.
    This ensures that objects are displayed as part of the current package.

    Notes
    -----
    This is particularly useful for dynamically created objects or objects
    imported from other modules that need to appear as if they belong to the
    current package.

    Examples
    --------
    >>> reassign_module_names()
    """
    for value in list(locals().values()):
        if getattr(value, "__module__", "").startswith(__name__):
            value.__module__ = __name__
