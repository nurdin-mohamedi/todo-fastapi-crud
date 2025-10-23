#!python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

test_db_url = "sqlite:///:memory:"

test_engine = create_engine(test_db_url)
session = sessionmaker(
    autoflush=False, autocommit=False, bind=test_engine
)
