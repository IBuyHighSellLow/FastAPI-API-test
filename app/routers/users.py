from .. import models, schemas, utils
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    #hash password - user.password

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)    
    return new_user

@router.get("/", status_code=status.HTTP_200_OK,)
def get_users(db: Session = Depends(get_db)):
    #cursor.execute("""SELECT * FROM users;""")
    #posts = cursor.fetchall()
    users = db.query(models.User).all()
    print(users)
    return users


@router.get("/{id}", response_model=schemas.UserOut)
def get_post(id: int, db: Session = Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.id==id)
    post = user_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} does not exist")
    return post
