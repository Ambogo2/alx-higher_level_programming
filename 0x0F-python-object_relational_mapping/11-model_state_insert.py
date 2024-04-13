#!/usr/bin/python3
"""connects a python script to a database"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    connection_string = "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(connection_string, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State object
    new_obj = State(name="Louisiana")

    # Add new object to session
    session.add(new_obj)

    # Commit changes to database
    session.commit()

    # Print the ID of the newly added object
    print(new_obj.id)

    session.close()
