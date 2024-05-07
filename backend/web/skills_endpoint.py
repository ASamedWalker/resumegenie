from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from models.skills import Skills
from services.resume_services import (
    create_resume,
    get_resume,
    get_all_resumes,
    update_resume,
    delete_resume,
)

router = APIRouter(prefix="/skills", tags=["Skills"])


@router.post("/", response_model=Skills, status_code=status.HTTP_201_CREATED)
async def create_skills_endpoint(
    skills: Skills,
    db: AsyncSession = Depends(get_session),
) -> Skills:
    try:
        return await create_skills(db, skills)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{skills_id}", response_model=Skills)
async def get_skills_endpoint(
    skills_id: int,
    db: AsyncSession = Depends(get_session),
) -> Skills:
    try:
        return await get_skills(db, skills_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=list[Skills])
async def get_all_skills_endpoint(
    db: AsyncSession = Depends(get_session),
) -> list[Skills]:
    try:
        return await get_all_skills(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{skills_id}", response_model=Skills)
async def update_skills_endpoint(
    skills_id: int,
    skills: Skills,
    db: AsyncSession = Depends(get_session),
) -> Skills:
    try:
        return await update_skills(db, skills_id, skills)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{skills_id}", response_model=Skills)
async def delete_skills_endpoint(
    skills_id: int,
    db: AsyncSession = Depends(get_session),
) -> Skills:
    try:
        return await delete_skills(db, skills_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
