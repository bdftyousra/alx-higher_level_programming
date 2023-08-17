#!/usr/bin/python3
"""
    A script that returns the first State object from hbtn_0e_6_usa
    Username, password and dbname wil be passed as arguments to the script.
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # extract first state
    states = session.query(State).order_by(State.id).first()

    # print state
    if states is None:
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))

    session.close()
