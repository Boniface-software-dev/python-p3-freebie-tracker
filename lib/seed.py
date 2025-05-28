#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

# Create an engine and session
engine = create_engine('sqlite:///lib/freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

# Create sample companies
company1 = Company(name='TechCorp', founding_year=2000)
company2 = Company(name='InnovateX', founding_year=1995)

# Create sample devs
dev1 = Dev(name='Alice')
dev2 = Dev(name='Bob')

# Create sample freebies
freebie1 = Freebie(item_name='T-Shirt', value=20, company=company1, dev=dev1)
freebie2 = Freebie(item_name='Mug', value=10, company=company2, dev=dev2)

# Add to session and commit
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
session.commit()

