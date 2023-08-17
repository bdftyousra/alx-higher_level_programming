#!/usr/bin/python3
"""
    A script that prints the State object with the name passed as an argument
    from hbtn_0e_6_usa
    Username, password, dbname and name to search
    will be passed as arguments to the script.
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
    states = session.query(State) \
                    .filter(State.name == sys.argv[4]).one_or_none()

    # print state.id
    if states is None:
        print("Not found")
    else:
        print(states.id)

    session.close()
