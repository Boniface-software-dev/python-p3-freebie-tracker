from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import relationship, declarative_base
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
    freebies = relationship('Freebie', back_populates='company')

    def __repr__(self):
        return f'<Company {self.name}', f'Founded in {self.founding_year}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String(), nullable=False)

    # Establish a relationship with Freebie
    freebies = relationship('Freebie', back_populates='dev')

    def __repr__(self):
        return f'<Dev {self.name}>'
    
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    date_given = Column(String(), default=datetime.utcnow().strftime('%Y-%m-%d'))
    
    # Foreign keys
    company_id = Column(Integer(), ForeignKey('companies.id'), nullable=False)
    dev_id = Column(Integer(), ForeignKey('devs.id'), nullable=False)
     
     #Relationships
    company = relationship('Company', back_populates='freebies')
    dev = relationship('Dev', back_populates='freebies')
    
    def __repr__(self):
        return f'Item: {self.item_name}', f'Description: {self.description}', f'Date Given: {self.date_given}>'
