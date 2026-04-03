def safe_import_isaac():
    try:
        import omni  # type: ignore
        return omni
    except Exception:
        return None
