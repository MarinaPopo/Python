from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from biathlon.database import Base

class ResultTable(Base):
    __tablename__ = 'result_table'

    place = Column(Integer, primary_key=True)
    last_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    lag = Column(Integer)
    athlete = relationship('Athlete')

    def __init__(self, last_name, first_name, lag):
        self.last_name = last_name
        self.first_name = first_name
        self.lag = lag

    def __repr__(self):
        return f"{self.last_name} занял место {self.place} с отставанием {self.lag}"
