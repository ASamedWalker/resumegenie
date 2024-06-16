from model.resume import Resume
import fake.resume as data


def get_all() -> list[Resume]:
    return data.get_all()


def get_one(name: str) -> Resume | None:
    return data.get_one(name)


def create(resume: Resume) -> Resume:
    return data.create(resume)


def modify(id, resume: Resume) -> Resume:
    return data.modify(id, resume)


def replace(id, resume: Resume) -> Resume:
    return data.replace(id, resume)


def delete(id, resume: Resume) -> bool:
    return data.delete(id)
