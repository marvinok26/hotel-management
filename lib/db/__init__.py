from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# Database connection string
DB_URL = 'sqlite:///lib/db/hoteldb.db'

# Create engine
engine = create_engine(DB_URL)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Create Base
Base = declarative_base()
