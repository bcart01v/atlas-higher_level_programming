#!/usr/bin/python3


"""
This module only prints states that contain an A. It's
Pretty simple.
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

    a_states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for states in a_states:
        print(f"{state.id}: {state.name}")
