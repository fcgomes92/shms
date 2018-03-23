_session = None


def session():
    from shms import settings
    global _session
    if not _session:
        _session = settings.Session()
    return _session
