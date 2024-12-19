from typing import List, Optional
from pydantic import BaseModel
import datetime as _dt

class _MovieBase(BaseModel):
    name: str
    description: str
    rating: int
    playing_date: _dt.datetime

class MovieCreate(_MovieBase):
    pass

class MovieInfo(_MovieBase):
    id: int
    created_date: _dt.datetime
    last_updated: _dt.datetime

class Config:
    orm_mode = True

