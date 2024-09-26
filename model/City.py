from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.base import Base

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(100), unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=True)


    targets = relationship('Target', back_populates='city', lazy='dynamic')
    country = relationship('Country', back_populates='cities', lazy='joined')

    def __repr__(self):
        return f'<City(id={self.id}, city_name={self.city_name})>'