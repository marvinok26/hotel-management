from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base, session

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    address = Column(String)

class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    address = Column(String)

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    capacity = Column(Integer)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))

    # Define the relationship with hotels if needed
    hotel = relationship("Hotel", back_populates="rooms")

class Hotel(Base):
    __tablename__ = 'hotels'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    rooms = relationship("Room", back_populates="hotel", cascade="all, delete-orphan")

# Function to create database tables
def create_tables():
    Base.metadata.create_all(session.get_bind())
