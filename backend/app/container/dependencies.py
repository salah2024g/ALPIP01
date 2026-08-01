from backend.app.container.container import container


def get_service(name: str):

    return container.resolve(name)
