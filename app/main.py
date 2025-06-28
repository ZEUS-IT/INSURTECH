from fastapi import FastAPI
from app.database import Base, engine
from app.auth import router as auth_router
from app.routers import polizas

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(polizas.router)
