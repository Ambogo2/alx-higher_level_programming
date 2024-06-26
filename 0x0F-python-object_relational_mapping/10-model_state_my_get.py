#!/usr/bin/python3
"""Connects a Python script to a database and prints the State object with the given name"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    # Check if all necessary arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./script_name.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Construct connection string
    connection_string = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}"

    # Create SQLAlchemy engine
    engine = create_engine(connection_string, pool_pre_ping=True)

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query for the State object with the given state_name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Check if state exists
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close the session
    session.close()
