from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, Integer, VARCHAR, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
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

    reviews = relationship("Review", backref="movie")




class User(Base):
    __tablename__ ="users"

    id = Column(Integer(), primary_key=True)
    first_name = Column(Text(), nullable=False)
    last_name = Column(Text(), nullable=False)
    Phone = Column(VARCHAR(), nullable=False)
    nationality=Column(Text(), nullable=False)

    reviews = relationship("Review", backref="user")
    
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer(), primary_key=True)
    reviews_text = Column(Text(), nullable=False)
    rating= Column(Integer(), nullable=False)
    movie_id=Column(Integer(), ForeignKey('movies.id'))
    user_id=Column(Integer(), ForeignKey('users.id'))
    
    