from multiprocessing import synchronize
import pydantic
from os import stat
from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from typing import Optional, List
from random import randrange
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
import psycopg2
from .routers import post, users, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)

