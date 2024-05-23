from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from web import (
    resume_endpoint,
    template_endpoint
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
app.include_router(template_endpoint.router)

