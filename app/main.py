from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import heroes, teams

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(heroes.router, prefix="/api/v1")
app.include_router(teams.router, prefix="/api/v1")