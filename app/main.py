from fastapi import FastAPI
from app.database import Base, engine
from app.auth import router as auth_router
from app.routers import polizas
from fastapi.middleware.cors import CORSMiddleware
from app.routers import polizas
app.include_router(polizas.router)


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(polizas.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Origen del frontend local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

