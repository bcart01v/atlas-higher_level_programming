#!/usr/bin/python3


"""
This module demonstrates a basic Object Relational Mapping (ORM) usage
with SQLAlchemy in Python. It defines two key components:
- Base: a base class for declarative class definitions.
- State: a class representing a 'states' table in a database.

The script also includes a conditional main section to create a database engine
that connects to a MySQL database, demonstrating how to establish a connection.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pw = sys.argv[2]
    mysql_database = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_pw}@localhost:3306/{mysql_database}')

    Base.metadata.bind = engine

    session = sessionmaker(bind = engine)
    session = session()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")