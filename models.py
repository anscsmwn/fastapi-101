from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime as _dt

class Movie(Base):
    __tablename__ = "movie_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    rating = Column(Integer)
    playing_date = Column(DateTime, default=_dt.datetime.now())
    created_date = Column(DateTime, default=_dt.datetime.now())
    last_updated = Column(DateTime, default=_dt.datetime.now())

