
import os
from typing import Iterator
from sqlmodel import SQLModel, Session, create_engine

from app.core.config import settings

DATABASE_URL = os.environ["DATABASE_URL"]
connect_args = {}
if DATABASE_URL.startswith("postgres"):
    connect_args = {"sslmode": "require"}
engine = create_engine(DATABASE_URL, pool_pre_ping=True,
                       connect_args=connect_args)

# engine = create_engine(settings.DATABASE_URL, echo=False, connect_args={
#                        "check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {})


def init_db() -> None:
    pass
    # if settings.ENVIRONMENT == "DEV":
    #     SQLModel.metadata.create_all(engine)  # dev


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
