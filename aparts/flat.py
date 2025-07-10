from aparts.database import Base
from sqlalchemy import Column, Integer, String


class Flat(Base):
    __tablename__ = "flat"

    id = Column(Integer, primary_key=True)
    street = Column(String(250), nullable=False)
    house = Column(String(250), nullable=False)
    floor = Column(Integer)
    square = Column(Integer)

    def __init__(self, street, house, floor, square):
        self.street = street
        self.house = house
        self.floor = floor
        self.square = square

    def __repr__(self):
        return (f" Квартира: улица {self.street}, дом {self.house}, этаж {self.floor}, площадь  {self.square} кв. м.")
