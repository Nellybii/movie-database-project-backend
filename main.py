from fastapi import FastAPI, Depends
from sqlalchemy.orm import session
from database import get_db
from schemas import MovieSchema
from models import Movie

app = FastAPI()

@app.get('/')
def index():
    return {"message": "welcome to movies-database"}

@app.get('/movies')
def movies(db:session=Depends(get_db)):
    movies = db.query(Movie).all()
    return movies

@app.get('/movies/{movie_id}')
def movie():
    return{}

@app.post('/movies')
def create_movie(movie: MovieSchema, db:session=Depends(get_db)):
    print(movie)
    new_movie = Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return{"mesage": "successfully created", "movie": new_movie}

@app.patch('/movies/{movie_id}')
def update_movies(movie_id: int):
    return {"message":f"Movie {movie_id} updated successfully"}

@app.delete('/movies/{movie_id}')
def delete_movies(movie_id: int):
    return {"message":f"Movie {movie_id} deleted successfully"}