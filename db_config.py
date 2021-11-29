from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from KEYS import DB_USER_NAME, DB_USER_PWD, DB_HOST, DB_NAEM

DATABASE = f'postgresql://{DB_USER_NAME}:{DB_USER_PWD}@{DB_HOST}/{DB_NAEM}?charset=utf8'


ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()