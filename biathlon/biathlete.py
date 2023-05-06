from sqlalchemy import Column, ForeignKey, Integer, String

from biathlon.database import Base


class Athlete(Base):
    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True)
    last_name = Column(String(250), ForeignKey('result_table.last_name'), nullable=False)
    first_name = Column(String(250), nullable=False)
    region = Column(String(250), nullable=False)
    points = Column(Integer)

    def __init__(self, last_name, first_name, region, points):
        self.last_name = last_name
        self.first_name = first_name
        self.region = region
        self.points = points

    def __repr__(self):
        return f"Спортсмен ({self.last_name} {self.first_name}," \
               f"Регион: {self.region}, Очки: {self.points})"
