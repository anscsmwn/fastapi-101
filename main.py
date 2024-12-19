from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models as models, schemas as schemas
import crud as crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency

def get_database_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Movie API",
        "endpoints": {
            "/api/v1/movies/": "Fetch all movies",
            "/api/v1/movies/{movie_id}": "Fetch a movie by ID",
            "/api/v1/movies/": "Create a new movie",
            "/api/v1/movies/{movie_id}": "Update a movie by ID",
            "/api/v1/movies/{movie_id}": "Delete a movie by ID",
        }
    }


@app.get("/api/v1/movies/", response_model=List[schemas.MovieInfo])
def fetch_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_database_session)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies

@app.post("/api/v1/movies/", response_model=schemas.MovieInfo)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_database_session)):
    return crud.create_movie(db, movie)

@app.get("/api/v1/movies/{movie_id}", response_model=schemas.MovieInfo)
def fetch_movie(movie_id: int, db: Session = Depends(get_database_session)):
    movie = crud.get_movie_by_id(db, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.put("/api/v1/movies/{movie_id}", response_model=schemas.MovieInfo)
def update_movie(movie_id: int, movie: schemas.MovieCreate, db: Session = Depends(get_database_session)):
    db_movie = crud.get_movie_by_id(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return crud.update_movie(db, movie_id, movie)

@app.delete("/api/v1/movies/{movie_id}", response_model=schemas.MovieInfo)
def delete_movie(movie_id: int, db: Session = Depends(get_database_session)):
    db_movie = crud.get_movie_by_id(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return crud.delete_movie(db, movie_id)
