#!/usr/bin/python3
"""Connects a Python script to a database"""

from relationship_city import Base, City
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    # Check if all necessary arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./script_name.py <mysql_username> <mysql_password> <database_name>")
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

    try:
        # Query all City objects and print in the required format
        for city in session.query(City).order_by(City.id):
            print(f"{city.id}: {city.name} -> {city.state.name}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()
