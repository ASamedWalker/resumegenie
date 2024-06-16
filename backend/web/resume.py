from fastapi import APIRouter, HTTPException
from model.resume import Resume
import fake.resume as service
from error import Missing, Duplicate

router = APIRouter(prefix="/resume", tags=["resume"])


@router.get("")
@router.get("/")
def get_all():
    return service.get_all()


@router.get("/{name}")
def get_one(name: str):
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=str(exc.msg))


@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(resume: Resume) -> Resume:
    try:
        return service.create(resume)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=str(exc.msg))


@router.patch("/{name}")
def modify(name: str, resume: Resume) -> Resume:
    try:
        return service.modify(name, resume)
    except Missing as exc:
        return HTTPException(status_code=404, detail=str(exc.msg))


@router.delete("/{name}", status_code=204)
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=str(exc.msg))
