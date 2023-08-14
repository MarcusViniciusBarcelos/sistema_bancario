# app/persistence/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import (sessionmaker,
                            declarative_base)

Base = declarative_base()
db_engine = None
Session = None


def initialize_db():
    global db_engine
    global Session
    db_engine = create_engine("sqlite:///banco.db")
    Session = sessionmaker(bind=db_engine)
    Base.metadata.create_all(db_engine)


def get_session():
    return Session()


if __name__ == '__main__':
    initialize_db()
    session = get_session()
