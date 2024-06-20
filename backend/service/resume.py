from data.resume import get_one, get_all, create, modify, delete
from model.resume import Resume
from error import Missing, Duplicate


def service_get_all_resumes() -> list[Resume]:
    return get_all()


def service_get_resume_by_id(id: int) -> Resume:
    try:
        return get_one(id)
    except Missing as exc:
        raise Missing(msg=f"Resume with id {id} not found")


def service_create_resume(resume_data: dict) -> Resume:
    resume = Resume(**resume_data)
    try:
        return create(resume)
    except Duplicate as exc:
        raise Duplicate(msg=f"A resume with similar details already exists")


def service_modify_resume(id: int, resume_data: dict) -> Resume:
    existing_resume = service_get_resume_by_id(id)  # Ensure the resume exists
    updated_resume = Resume(**resume_data)
    return modify(id, updated_resume)


def service_delete_resume(id: int) -> bool:
    try:
        return delete(id)
    except Missing as exc:
        raise Missing(msg=f"Resume with id {id} not found")
