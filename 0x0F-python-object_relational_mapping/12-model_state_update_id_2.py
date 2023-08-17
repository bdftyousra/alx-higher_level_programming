#!/usr/bin/python3
"""
    A script that changes teh name of a State object in hbtn_0e_6_usa
    name of State where id = 2 to New Mexico
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

    # fetch row to change
    rename_state = session.query(State) \
                          .filter(State.id == 2).first()
    rename_state.name = 'New Mexico'
    session.commit()

    session.close()
