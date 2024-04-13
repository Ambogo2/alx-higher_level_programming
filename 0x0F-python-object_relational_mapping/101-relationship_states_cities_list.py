#!/usr/bin/python3
"""connects a python script to a database"""

from relationship_city import Base, City
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    my_session_maker = sessionmaker(bind=engine)

    my_session = my_session_maker()

    for state in my_session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("  {}: {}".format(city.id, city.name))

    my_session.close()
