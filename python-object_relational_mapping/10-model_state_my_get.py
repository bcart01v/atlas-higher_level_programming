#!/usr/bin/python3
"""
This prints the state object from the name passed as an argument.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pw = sys.argv[2]
    mysql_database = sys.argv[3]
    # If the user forgets the state, raise an error.
    if len(sys.argv) > 4:
        searchvalue = sys.argv[4]
    else:
        raise ValueError("Missing required field: State Name")
    # Create an engine and connect to the database
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_pw}@localhost:3306/{mysql_database}')
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State objects that contain the letter 'a', ordered by states.id
    state = session.query(State).filter(State.name == searchvalue).first()

    # Print the results
    if state:
        print(f"{state.id}")
    else:
        print("Not found")