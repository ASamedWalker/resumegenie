from fastapi import FastAPI
from web import resume
from data.init import get_db

app = FastAPI()


@app.on_event("startup")
def startup_event():
    # Initialize the database
    with get_db() as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS resume (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                summary TEXT NOT NULL
            )
            """
        )
        print("Database and table ensured.")


app.include_router(resume.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
