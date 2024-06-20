import os
from pathlib import Path
from sqlite3 import connect, Connection
from contextlib import contextmanager


# Function to determine the database path
def get_db_path():
    default_path = Path(__file__).resolve().parents[1] / "db" / "resume.db"
    return os.getenv("RESUME_SQLITE_DB", str(default_path))


# Context manager for managing database connections
@contextmanager
def get_db():
    conn: Connection = None
    try:
        db_path = get_db_path()
        conn = connect(db_path, check_same_thread=False)
        yield conn.cursor()
    finally:
        if conn:
            conn.close()


# Example usage within your application
if __name__ == "__main__":
    with get_db() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS resume (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL, phone TEXT NOT NULL, summary TEXT NOT NULL)"
        )
        print("Database and table ensured.")
