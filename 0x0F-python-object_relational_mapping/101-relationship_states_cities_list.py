#!/usr/bin/python3
"""Connects a Python script to a database and lists State and City objects"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    # Check if all necessary arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./list_states_cities.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Construct connection string and create SQLAlchemy engine
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True
    )

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    try:
        # Query all State objects and their associated City objects, sorted by State.id
        states = session.query(State).order_by(State.id).all()

        # Print the result in the required format
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"  {city.id}: {city.name}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()
