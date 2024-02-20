#!/usr/bin/python3

"""
This module will update state.id 2's name to New Mexico.
In the hbtn_0e_6_usa database
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Get variable's passed into program.
    mysql_user = sys.argv[1]
    mysql_pw = sys.argv[2]
    mysql_database = sys.argv[3]
# Establish connection to the database.
    engine = create_engine(
        f'mysql+mysqldb://{mysql_user}:{mysql_pw}'
        f'@localhost:3306/{mysql_database}')
    Base.metadata.bind = engine
    # Create the session to the database.
    Session = sessionmaker(bind=engine)
    session = Session()
    # Update a line of data!
    session.query(State).filter_by(id='2').update\
    ({"name": "New Mexico"})
    session.commit()
