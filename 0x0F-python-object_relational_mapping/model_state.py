#!/usr/bin/python3

"""
    this module contains a Base and State class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer


Base = declarative_base()


class State(Base):
    """
        State class inherits the Base class
        Attributes:
            id (int)
            name (string)
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
