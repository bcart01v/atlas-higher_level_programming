#!/usr/bin/python3
"""
This script fetches all cities from the database, along with their associated states,
and prints them in a specific format. It demonstrates the use of SQLAlchemy ORM
for querying and joining tables.

The script takes three command-line arguments: MySQL username, MySQL password, and the database name.
It connects to the MySQL server running on localhost at port 3306.

"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    mysql_user, mysql_pw, mysql_db = sys.argv[1:4]

    engine = create_engine(
        f'mysql+mysqldb://{mysql_user}:{mysql_pw}'
        f'@localhost:3306/{mysql_db}')
    
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
