#!/usr/bin/python3
"""
This prints states that contain an a.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pw = sys.argv[2]
    mysql_database = sys.argv[3]

    # Create an engine and connect to the database
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_pw}@localhost:3306/{mysql_database}')
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State objects that contain the letter 'a', ordered by states.id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
