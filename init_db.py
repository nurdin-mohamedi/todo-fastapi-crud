#!python

from database import engine
from schema import Base

Base.metadata.create_all(engine)
