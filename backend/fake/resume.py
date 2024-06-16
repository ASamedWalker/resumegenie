from model.resume import Resume

_resume = [
    Resume(
        name="John Doe",
        email="john.doe@example.com",
        phone="123-456-7890",
        summary="I am a software engineer with experience in developing web applications.",
    ),
    Resume(
        name="Jane Doe",
        email="jane.doe@example.com",
        phone="123-456-7890",
        summary="I am a sales representative with experience in selling software products.",
    ),
]


def get_all() -> list[Resume]:
    return _resume


def get_one(name: str) -> Resume:
    for resume in _resume:
        if resume.name == name:
            return resume
    return None


def create(resume: Resume) -> Resume:
    _resume.append(resume)
    return resume


def modify(name: str, resume: Resume) -> Resume:
    for i, r in enumerate(_resume):
        if r.name == resume.name:
            for field in resume.dict(exclude_unset=True):
                setattr(_resume[i], field, getattr(resume, field))
            return _resume[i]
    return None


def replace(name: str, resume: Resume) -> Resume:
    for i, r in enumerate(_resume):
        if r.name == resume.name:
            _resume[i] = resume
            return resume
    return None


def delete(name: str) -> Resume:
    for i, r in enumerate(_resume):
        if r.name == name:
            return _resume.pop(i)
    return None
