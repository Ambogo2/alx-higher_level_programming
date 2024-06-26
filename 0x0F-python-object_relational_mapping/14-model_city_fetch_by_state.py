#!/usr/bin/python3
"""connects a python script to a database"""

from model_state import Base, State
from model_city import City
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

    # Query State and City objects joined by State.id == City.state_id
    result = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()

    # Print the result in the required format
    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
