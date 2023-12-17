from pydantic import BaseModel

class MovieSchema(BaseModel):
    image: str
    title: str
    genre: str
    description: str
    runtime : str
    production_date :str