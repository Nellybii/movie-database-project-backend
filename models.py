from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, Integer, VARCHAR, DateTime
Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer(), primary_key=True)
    image = Column(VARCHAR, nullable=False)
    title = Column(Text(), nullable=False)
    genre = Column(VARCHAR(), nullable=False)
    description = Column(Text(), nullable=False)
    runtime = Column(VARCHAR(), nullable=False)
    production_date = Column(DateTime(), nullable=False)