from sqlalchemy import Column, BigInteger, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from config.base import Base

class Target(Base):
    __tablename__ = 'targets'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    priority = Column(Integer, nullable=True)
    latitude = Column(Numeric(10, 6),  nullable=True)
    longitude = Column(Numeric(10, 6), nullable=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=True)
    industry_id = Column(Integer, ForeignKey('target_industries.id'), nullable=True)
    type_id = Column(Integer, ForeignKey('target_types.id'), nullable=True)

    city = relationship('City', back_populates='targets', lazy='joined')
    industry = relationship('TargetIndustry', back_populates='targets', lazy='joined')
    type = relationship('TargetType', back_populates='targets', lazy='joined')


    def __repr__(self):
        return f'<Target(id={self.id}, priority={self.priority}, latitude={self.latitude}, longitude={self.longitude})>'