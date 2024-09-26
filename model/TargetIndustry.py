from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base

class TargetIndustry(Base):
    __tablename__ = 'target_industries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    industry_name = Column(String(255), unique=True, nullable=False)

    targets = relationship('Target', back_populates='industry', lazy='dynamic')

    def __repr__(self):
        return f'<TargetIndustry(id={self.id}, industry_name={self.industry_name})>'