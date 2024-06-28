#!/usr/bin/python3
from SQLAlchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class State(Base):
    """ State class """

