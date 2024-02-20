#!/usr/bin/python3


"""
This module demonstrates a basic Object Relational Mapping (ORM) usage
with SQLAlchemy in Python. It defines two key components:
- Base: a base class for declarative class definitions.
- State: a class representing a 'states' table in a database.

The script also includes a conditional main section to create a database engine
that connects to a MySQL database, demonstrating how to establish a connection.
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Defines the base class. 
Base = declarative_base()

# Defines the state class.
class City(Base):
    """
    Represents a city with an ID and name, mapping to the 'city' table in a database.
    
    Attributes:
        __tablename__ (str): The name of the table to map to in the database.
        id (Column): An integer column that represents the city's ID, serving as the primary key.
        name (Column): A string column that represents the name of the city.
    """


    __tablename__ = 'cities' # Here's the table we're using
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_key=('states.id'))

if __name__ == "__main__":
    engine = create_engine ('mysql+mysqldb://<root>:<#Frederf2024>@localhost:3306/<hbtn_0e_6_usa>', echo=True)
