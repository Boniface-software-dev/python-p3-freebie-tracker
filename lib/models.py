from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Define the naming convention for foreign keys
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

# Create a base class for declarative models with the defined metadata
Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    founding_year = Column(Integer(), nullable=False)

    # Establish a relationship with Freebie
    freebies = relationship('Freebie', backref='company', lazy='dynamic')

    def __repr__(self):
        return f'<Company {self.name}', f'Founded in {self.founding_year}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String(), nullable=False)

    # Establish a relationship with Freebie
    freebies = relationship('Freebie', backref='dev', lazy='dynamic')

    def __repr__(self):
        return f'<Dev {self.name}>'
    
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    date_given = Column(String(), default=datetime.utcnow().strftime('%Y-%m-%d'))
    
    # Foreign keys
    company_id = Column(Integer(), ForeignKey('companies.id'), nullable=False)
    dev_id = Column(Integer(), ForeignKey('devs.id'), nullable=False)

    def __repr__(self):
        return f'<Freebie {self.name}>'
