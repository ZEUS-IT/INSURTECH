from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app import database, models, schemas
from jose import jwt, JWTError
from datetime import datetime

router = APIRouter()

SECRET_KEY = "tu_clave_secreta"  # podés poner algo más seguro en producción
ALGORITHM = "HS256"

# Dependencia para obtener sesión de base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para extraer el usuario desde el token
def get_current_user_email(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

# Ruta para crear una póliza
@router.post("/polizas", response_model=schemas.PolizaOut)
def crear_poliza(
    poliza: schemas.PolizaCreate,
    db: Session = Depends(get_db),
    authorization: str = Header(...)
):
    token = authorization.split(" ")[1] if " " in authorization else authorization
    usuario_email = get_current_user_email(token)

    nueva = models.Poliza(
        aseguradora=poliza.aseguradora,
        numero=poliza.numero,
        vencimiento=datetime.strptime(poliza.vencimiento, "%Y-%m-%d").date(),
        usuario_email=usuario_email
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

# Ruta para listar pólizas del usuario logueado
@router.get("/polizas", response_model=list[schemas.PolizaOut])
def listar_polizas(
    db: Session = Depends(get_db),
    authorization: str = Header(...)
):
    token = authorization.split(" ")[1] if " " in authorization else authorization
    usuario_email = get_current_user_email(token)

    return db.query(models.Poliza).filter(models.Poliza.usuario_email == usuario_email).all()


