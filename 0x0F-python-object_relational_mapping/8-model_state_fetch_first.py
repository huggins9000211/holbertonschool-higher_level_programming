#!/usr/bin/python3
""" sql """

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    x = session.query(State).order_by(State.id).first()
    if x is None:
        print("{}: {}".format(x.id, x.name))
    else:
        print("Nothing")
