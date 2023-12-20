from pydantic import BaseModel

class MovieSchema(BaseModel):
    image: str
    title: str
    genre: str
    description: str
    runtime : str
    production_date :str

class UserSchema(BaseModel):
    first_name: str
    last_name: str
    phone: str
    nationality: str
    
class ReviewSchema(BaseModel):
    reviews_text: str
    rating: int
    movie_id: int
    user_id: int

    