from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "tu_clave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    hashed = pwd_context.hash(user.password)
    db_user = models.Usuario(email=user.email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    return {"mensaje": "Usuario creado"}

@router.post("/login")
def login(user: schemas.UsuarioLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.Usuario).filter(models.Usuario.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    token_data = {
        "sub": db_user.email,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token}
