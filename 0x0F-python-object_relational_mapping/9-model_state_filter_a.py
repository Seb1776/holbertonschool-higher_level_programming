#!/usr/bin/python3
'''states'''

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    myQuery = session.query(State.id, State.name).order_by(
        State.id).filter(State.name.like("%a%")).all()

    for i in myQuery:
        print('{}: {}'.format(i.id, i.name))
