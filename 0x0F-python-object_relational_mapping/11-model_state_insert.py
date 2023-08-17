#!/usr/bin/python3
"""
    A script that adds the State object 'Louisiana' to hbtn_0e_6_usa
    Username, password, dbname will be passed as arguments to the script.
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

    # create the object and add it
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # print state.id
    state_add = session.query(State).filter(State.name == 'Louisiana').one()
    print(state_add.id)

    session.close()
