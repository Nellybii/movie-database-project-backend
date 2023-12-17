from fastapi import FastAPI
from schemas import MovieSchema

app = FastAPI()

@app.get('/')
def index():
    return {"message": "welcome to movies-database"}

@app.get('/movies/{movie_id}')
def movie():
    return{}

@app.post('/movies')
def create_movie(movie: MovieSchema):
    return{"message":"movie database created sucessfully"}

@app.patch('/movies/{movie_id}')
def update_movies(movie_id: int):
    return {"message":f"Movie {movie_id} updated successfully"}

@app.delete('/movies/{movie_id}')
def delete_movies(movie_id: int):
    return {"message":f"Movie {movie_id} deleted successfully"}