from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(100), nullable=False)

    targets = relationship('Target', back_populates='city', lazy='dynamic')
    country = relationship('TargetCountry', back_populates='city', lazy='dynamic')

    def __repr__(self):
        return f'<City(id={self.id}, city={self.city})>'