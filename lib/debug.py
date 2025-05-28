#!/usr/bin/env python3

from sqlalchemy import create_engine
from models import Base, Company, Dev, Freebie
from sqlalchemy.orm import sessionmaker
# Create an engine and session
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # Fetch all devs
    devs = session.query(Dev).all()
    for dev in devs:
        print(dev)
        print(f"Companies: {[company.name for company in dev.companies]}")
        print(f"Received 'T-Shirt': {dev.received_one('T-Shirt')}")