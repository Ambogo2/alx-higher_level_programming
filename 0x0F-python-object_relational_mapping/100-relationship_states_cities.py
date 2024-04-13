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

    my_session.add(City(name="San Francisco", state=State(name="California")))
    my_session.commit()

    my_session.close()
