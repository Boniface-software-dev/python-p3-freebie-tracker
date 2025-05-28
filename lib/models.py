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
    freebies = relationship('Freebie', back_populates='company', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Company {self.name}', f'Founded in {self.founding_year}>'
    
    def give_freebie(self,dev, item_name, value):
        """Creates a new Freebie associated with this company and the given dev."""
        return Freebie(item_name=item_name, value=value, dev=dev, company=self)
    
    @classmethod
    def oldest_company(cls, session):
        """Returns the oldest company in the database."""
        return session.query(cls).order_by(cls.founding_year).first()


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String(), nullable=False)

    # Establish a relationship with Freebie
    freebies = relationship('Freebie', back_populates='dev')

    def __repr__(self):
        return f'<Dev {self.name}>'
    
    def received_one(self, item_name):
        """Checks if the dev has received a freebie with the given item name."""
        return any(freebie.item_name == item_name for freebie in self.freebies)
    
    def give_away(self, other_dev, freebie):
        """
        Transfers a freebie to another dev if the freebie belongs to this dev.
        """
        if freebie in self.freebies:
            freebie.dev = other_dev
    
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    value = Column(String(), nullable=False)
    date_given = Column(String(), default=datetime.utcnow().strftime('%Y-%m-%d'))
    
    # Foreign keys
    company_id = Column(Integer(), ForeignKey('companies.id'), nullable=False)
    dev_id = Column(Integer(), ForeignKey('devs.id'), nullable=False)
     
     #Relationships
    company = relationship('Company', back_populates='freebies')
    dev = relationship('Dev', back_populates='freebies')
    
    def __repr__(self):
        return f'Item: {self.item_name}', f'Description: {self.value}', f'Date Given: {self.date_given}>'
