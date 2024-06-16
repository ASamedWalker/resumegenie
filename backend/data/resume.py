from init import conn, curs, IntegrityError
from model.resume import Resume
from error import Missing, Duplicate


curs.execute(
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


def row_to_model(row: tuple) -> Resume:
    id, name, email, phone, summary = row
    return Resume(id=id, name=name, email=email, phone=phone, summary=summary)


def model_to_dict(resume: Resume) -> dict:
    return resume.dict()


def get_one(name: str) -> Resume:
    qry = "SELECT * FROM resume WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Resume {name} not found")


def get_all() -> list[Resume]:
    qry = "SELECT * FROM resume"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(resume: Resume) -> Resume:
    qry = "INSERT INTO resume (name, email, phone, summary) VALUES (:name, :email, :phone, :summary)"
    params = model_to_dict(resume)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=f"Resume {resume.name} already exists")
    return get_one(resume.name)


def modify(resume: Resume) -> Resume:
    if not get_one(resume.name):
        return None
    qry = "UPDATE resume SET email=:email, phone=:phone, summary=:summary WHERE name=:name"
    params = model_to_dict(resume)
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(resume.name)
    else:
        raise Missing(msg=f"Resume {resume.name} not found")


def delete(resume: Resume) -> bool:
    if not name: return False
    qry = "DELETE FROM resume WHERE name=:name"
    params = {"name": resume.name}
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return Missing(msg=f"Resume {resume.name} not found")
