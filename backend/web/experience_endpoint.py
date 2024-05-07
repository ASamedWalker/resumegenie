from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from models.experience import ExperienceDetail
from services.resume_services import (
    create_resume,
    get_resume,
    get_all_resumes,
    update_resume,
    delete_resume,
)

router = APIRouter(prefix="/experience", tags=["Experience"])


@router.post("/", response_model=ExperienceDetail, status_code=status.HTTP_201_CREATED)
async def create_experience_endpoint(
    experience: ExperienceDetail,
    db: AsyncSession = Depends(get_session),
) -> ExperienceDetail:
    try:
        return await create_experience(db, experience)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{experience_id}", response_model=ExperienceDetail)
async def get_experience_endpoint(
    experience_id: int,
    db: AsyncSession = Depends(get_session),
) -> ExperienceDetail:
    try:
        return await get_experience(db, experience_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=list[ExperienceDetail])
async def get_all_experience_endpoint(
    db: AsyncSession = Depends(get_session),
) -> list[ExperienceDetail]:
    try:
        return await get_all_experience(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{experience_id}", response_model=ExperienceDetail)
async def update_experience_endpoint(
    experience_id: int,
    experience: ExperienceDetail,
    db: AsyncSession = Depends(get_session),
) -> ExperienceDetail:
    try:
        return await update_experience(db, experience_id, experience)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{experience_id}", response_model=ExperienceDetail)
async def delete_experience_endpoint(
    experience_id: int,
    db: AsyncSession = Depends(get_session),
) -> ExperienceDetail:
    try:
        return await delete_experience(db, experience_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
