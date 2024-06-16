from fastapi import FastAPI
from web import resume

app = FastAPI()


app.include_router(resume.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
