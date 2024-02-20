#!/usr/bin/python3

"""
This module defines the City model, which represents the 'cities' table in a database.

The City model contains three fields: `id`, `name`, and `state_id`. It inherits from
Base, which is imported from `model_state`, linking it to the SQLAlchemy ORM infrastructure.
The `state_id` field establishes a foreign key relationship to the `states.id` column,
linking each city to a specific state.

Attributes:
    __tablename__ (str): Specifies the table name in the database.
    id (Column): Defines the primary key column, an auto-incrementing integer.
    name (Column): A string column for the city's name, cannot be null.
    state_id (Column): An integer foreign key linking the city to its state.

Classes:
    City: Represents a row in the 'cities' table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

class City(Base):
    """
    This is class documentation
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
