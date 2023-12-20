from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
engine = create_engine("postgresql://nelly:1YpddsZtoXczvA2pr0Q5K9JqOkMb62ml@dpg-clv4c9la73kc73bmg7i0-a.singapore-postgres.render.com/movies_fial")

LocalSession = sessionmaker(bind=engine)

def get_db():
    db=LocalSession()
    try:
        yield db
    finally:
        db.close()

        