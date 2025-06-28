from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database
from datetime import date

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/polizas")
def crear_poliza(p: schemas.PolizaCreate, db: Session = Depends(get_db)):
    poliza = models.Poliza(**p.dict())
    db.add(poliza)
    db.commit()
    return {"mensaje": "Póliza cargada"}

@router.get("/polizas/resumen")
def resumen(db: Session = Depends(get_db)):
    total = db.query(models.Poliza).count()
    vencidas = db.query(models.Poliza).filter(models.Poliza.fecha_vencimiento < date.today()).count()
    activas = total - vencidas
    return {"total": total, "activas": activas, "vencidas": vencidas}
