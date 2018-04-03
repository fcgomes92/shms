from shms.app import app

_session = None


def session():
    global _session
    if not _session:
        _session = app.config.Session()
    return _session
