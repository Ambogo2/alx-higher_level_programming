#!/usr/bin/python3
"""connects a python script to a database"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    connection_string = "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(connection_string, pool_pre_ping=True)

   # Create session maker
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query for State and City objects with a join condition
    result = session.query(State, City).filter(State.id == City.state_id).all()

    # Print the result
    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
