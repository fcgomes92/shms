from shms.application import SHMSApplication

app = None


def create_app():
    global app
    # create the app
    app = SHMSApplication()
    return app


def get_app():
    if not app:
        return create_app().app
    else:
        return app.app
