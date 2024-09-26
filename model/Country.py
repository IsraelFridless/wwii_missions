from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(100), nullable=False)

    targets = relationship('Target', back_populates='country', lazy='dynamic')
    cities = relationship('City', back_populates='country', lazy='dynamic')

    def __repr__(self):
        return f'<Country(id={self.id}, Country={self.country})>'