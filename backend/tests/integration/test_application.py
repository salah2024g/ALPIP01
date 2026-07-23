from backend.app.factory.application import (
    create_application
)


def test_application_creation():

    app = create_application()

    assert app.title == "ALPIP"
