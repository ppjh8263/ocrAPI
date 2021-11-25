from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
 
user_name = "*"
user_pwd = "*"
db_host = "*"
db_name = "*"

DATABASE = f'postgresql://{user_name}:{user_pwd}@{db_host}/{db_name}?charset=utf8'


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