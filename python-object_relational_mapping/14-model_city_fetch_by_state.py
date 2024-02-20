#!/usr/bin/python3

"""
This module will delete any state containing a,A
In the hbtn_0e_6_usa database
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from model_state import Base, State
from model_city import City
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
    Base.metadata.create_all(engine)
    # Create the session to the database.
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join\
        (State).order_by(City.id).all()

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
