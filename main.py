from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import session
from database import get_db
from schemas import MovieSchema
from models import Movie
from schemas import ReviewSchema
from models import Review, Movie, User

app = FastAPI()

origins =["*"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],

)

@app.get('/')
def index():
    return {"message": "welcome to movies-database"}

@app.get('/movies')
def movies(db:session=Depends(get_db)):
    movies = db.query(Movie).all()
    return movies

@app.get('/movies/{movie_id}')
def movie(movie_id:int, db:session=Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    return movie

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
def delete_movie(movie_id: int, db: session = Depends(get_db)):
    delete_movie = db.query(Movie).get(movie_id)

    if delete_movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Movie {movie_id} does not exist")

    try:
        db.delete(delete_movie)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Failed to delete movie {movie_id}. Error: {str(e)}")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.post('/reviews')
def create_review(review: ReviewSchema, db: session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == review.movie_id).first()
    user = db.query(User).filter(User.id == review.user_id).first()

    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Movie with ID {review.movie_id} not found",
        )

    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {review.user_id} not found",
        )

    new_review = Review(**review.dict())
    new_review.movie = movie
    new_review.user = user

    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return {'message': 'Review submitted successfully', 'review': new_review}