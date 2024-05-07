from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from web import (
    resume_endpoint,
    education_endpoint,
    experience_endpoint,
    skills_endpoint,
    certifications_endpoint,
    projects_endpoint,
)
from data.database import create_tables


def load_resources():
    print("Loading resources...")


def unload_resources():
    print("Unloading resources...")


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await create_tables()
    load_resources()
    yield
    unload_resources()


app = FastAPI(lifespan=app_lifespan)


app.include_router(resume_endpoint.router)
app.include_router(education_endpoint.router)
app.include_router(experience_endpoint.router)
app.include_router(skills_endpoint.router)
app.include_router(certifications_endpoint.router)
app.include_router(projects_endpoint.router)

