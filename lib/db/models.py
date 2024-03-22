from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    address = Column(String)

    def __repr__(self):
        return f"<Client(name='{self.name}', phone_number='{self.phone_number}', address='{self.address}')>"


class Worker(Base):
    __tablename__ = 'workers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    address = Column(String)

    def __repr__(self):
        return f"<Worker(name='{self.name}', phone_number='{self.phone_number}', address='{self.address}')>"


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    capacity = Column(Integer)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))

    def __repr__(self):
        return f"<Room(number='{self.number}', capacity='{self.capacity}', hotel_id='{self.hotel_id}')>"


def create_tables():
    Base.metadata.create_all(engine)
