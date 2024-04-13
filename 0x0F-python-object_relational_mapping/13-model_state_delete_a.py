#!/usr/bin/python3
"""connects a python script to a database"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(sys.argv[1],
        sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create session maker
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query states with names containing 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state from the query results
    for state in states:
        session.delete(state)

    # Commit changes to the database
    session.commit()

    # Close session
    session.close()
