from model.resume import Resume
from error import Missing, Duplicate
from data.init import get_db


def row_to_model(row: tuple) -> Resume:
    id, name, email, phone, summary = row
    return Resume(id=id, name=name, email=email, phone=phone, summary=summary)


def model_to_dict(resume: Resume) -> dict:
    return resume.dict()


def get_one(id: int) -> Resume:
    with get_db() as cursor:
        cursor.execute("SELECT * FROM resume WHERE id = ?", (id,))
        row = cursor.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Resume with id {id} not found")


def get_all() -> list[Resume]:
    with get_db() as cursor:
        cursor.execute("SELECT * FROM resume")
        rows = cursor.fetchall()
    return [row_to_model(row) for row in rows]


def create(resume: Resume) -> Resume:
    with get_db() as cursor:
        params = model_to_dict(resume)
        try:
            cursor.execute(
                "INSERT INTO resume (name, email, phone, summary) VALUES (:name, :email, :phone, :summary)",
                params,
            )
            return get_one(cursor.lastrowid)  # Fetch the newly created resume
        except IntegrityError as e:
            raise Duplicate(msg=f"Resume {resume.name} already exists")


def modify(id: int, resume: Resume) -> Resume:
    with get_db() as cursor:
        params = model_to_dict(resume)
        params["id"] = id
        cursor.execute(
            "UPDATE resume SET name=:name, email=:email, phone=:phone, summary=:summary WHERE id=:id",
            params,
        )
        if cursor.rowcount == 0:
            raise Missing(msg=f"Resume with id {id} not found")
    return get_one(id)


def delete(id: int) -> bool:
    with get_db() as cursor:
        cursor.execute("DELETE FROM resume WHERE id = ?", (id,))
        if cursor.rowcount == 0:
            raise Missing(msg=f"Resume with id {id} not found")
    return True
