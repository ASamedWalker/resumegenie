from fastapi import APIRouter, HTTPException, status
from typing import List
from model.resume import Resume
from service.resume import (
    service_get_all_resumes,
    service_get_resume_by_id,
    service_create_resume,
    service_modify_resume,
    service_delete_resume,
)
from error import Missing, Duplicate

router = APIRouter(prefix="/resume", tags=["resume"])


@router.get("")
@router.get("/", response_model=List[Resume])
def get_all_resumes():
    return service_get_all_resumes()


@router.get("/{id}", response_model=Resume)
def get_resume(id: int):
    try:
        return service_get_resume_by_id(id)
    except Missing as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc.msg))

@router.get("")
@router.post("/", response_model=Resume, status_code=status.HTTP_201_CREATED)
def create_resume(resume_data: dict):
    try:
        return service_create_resume(resume_data)
    except Duplicate as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc.msg))


@router.patch("/{id}", response_model=Resume)
def modify_resume(id: int, resume_data: dict):
    try:
        return service_modify_resume(id, resume_data)
    except Missing as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc.msg))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resume(id: int):
    try:
        service_delete_resume(id)
    except Missing as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc.msg))
