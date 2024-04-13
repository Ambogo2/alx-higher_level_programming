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

    # Query the state with id=2
    state = session.query(State).filter_by(id=2).first()

    # Update the name of the state
    state.name = "New Mexico"

    # Commit changes to the database
    session.commit()

    # Close session
    session.close()
