from app.database.session.database import engine
from app.database.models.base import Base


def initialize_database():

    Base.metadata.create_all(
        bind=engine
    )
