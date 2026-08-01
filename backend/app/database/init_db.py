from app.database.models.base import Base
from app.database.session.database import engine


def initialize_database():

    Base.metadata.create_all(bind=engine)
