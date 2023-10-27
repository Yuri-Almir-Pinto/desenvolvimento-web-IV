from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

# -------------- CRUD USERS --------------

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def del_users(db: Session, id: int = 0):
    user = get_user(db, id)
    if user == None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(user)
    db.commit()
    return user

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

    # -------------- CRUD FAVORITES --------------

def favorite_movie(db: Session, email: str, idMovie: str):
    user = get_user_by_email(db, email)
    if user == None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db_favorite = models.Favorites(idUser=user, idMovie=idMovie)
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite
