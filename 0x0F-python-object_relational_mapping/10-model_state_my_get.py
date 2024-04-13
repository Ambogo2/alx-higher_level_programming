#!/usr/bin/python3
"""connects a python script to a database"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    connection_string = "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(connection_string, pool_pre_ping=True)

    my_session_maker = sessionmaker(bind=engine)

    # instance of session
    my_session = my_session_maker()

    for state in my_session.query(State):
    if sys.argv[4] == state.name:
        print("{}".format(state.id))
        break
    else:
        print("Not found")

    my_session.close()
