import sqlalchemy.orm as _orm

import models as _models, schemas as _schemas, database as _database

def get_movies(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.Movie).offset(skip).limit(limit).all()

def create_movie(db: _orm.Session, movie: _schemas.MovieCreate):
    db_movie = _models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie 

def get_movie_by_id(db: _orm.Session, movie_id: int):
    return db.query(_models.Movie).filter(_models.Movie.id == movie_id).first()

def update_movie(db: _orm.Session, movie_id: int, movie: _schemas.MovieCreate):
    db_movie = get_movie_by_id(db, movie_id)
    db_movie.name = movie.name
    db_movie.description = movie.description
    db_movie.rating = movie.rating
    db_movie.playing_date = movie.playing_date
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: _orm.Session, movie_id: int):
    db_movie = get_movie_by_id(db, movie_id)
    db.delete(db_movie)
    db.commit()
    return db_movie

    

