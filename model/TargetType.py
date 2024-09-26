from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base

class TargetType(Base):
    __tablename__ = 'target_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String(100), unique=True, nullable=False)

    targets = relationship('Target', back_populates='type', lazy='dynamic')

    def __repr__(self):
        return f'<TargetType(id={self.id}, target_type_name={self.target_type_name})>'