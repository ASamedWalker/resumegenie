from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from models.education import EducationDetail
from services.resume_services import (
    create_resume,
    get_resume,
    get_all_resumes,
    update_resume,
    delete_resume,
)

router = APIRouter(prefix="/education", tags=["Education"])


@router.post("/", response_model=EducationDetail, status_code=status.HTTP_201_CREATED)
async def create_education_endpoint(
    education: EducationDetail,
    db: AsyncSession = Depends(get_session),
) -> EducationDetail:
    try:
        return await create_education(db, education)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{education_id}", response_model=EducationDetail)
async def get_education_endpoint(
    education_id: int,
    db: AsyncSession = Depends(get_session),
) -> EducationDetail:
    try:
        return await get_education(db, education_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=list[EducationDetail])
async def get_all_education_endpoint(
    db: AsyncSession = Depends(get_session),
) -> list[EducationDetail]:
    try:
        return await get_all_education(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{education_id}", response_model=EducationDetail)
async def update_education_endpoint(
    education_id: int,
    education: EducationDetail,
    db: AsyncSession = Depends(get_session),
) -> EducationDetail:
    try:
        return await update_education(db, education_id, education)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{education_id}", response_model=EducationDetail)
async def delete_education_endpoint(
    education_id: int,
    db: AsyncSession = Depends(get_session),
) -> EducationDetail:
    try:
        return await delete_education(db, education_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
