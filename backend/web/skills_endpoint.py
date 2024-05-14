from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from models.skills import Skill
from services.resume_services import (
    create_resume,
    get_resume,
    get_all_resumes,
    update_resume,
    delete_resume,
)

router = APIRouter(prefix="/skills", tags=["Skills"])


@router.post("/", response_model=Skill, status_code=status.HTTP_201_CREATED)
async def create_skills_endpoint(
    skills: Skill,
    db: AsyncSession = Depends(get_session),
) -> Skill:
    try:
        return await create_skills(db, skills)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{skills_id}", response_model=Skill)
async def get_skills_endpoint(
    skills_id: int,
    db: AsyncSession = Depends(get_session),
) -> Skill:
    try:
        return await get_skills(db, skills_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=list[Skill])
async def get_all_skills_endpoint(
    db: AsyncSession = Depends(get_session),
) -> list[Skill]:
    try:
        return await get_all_skills(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{skills_id}", response_model=Skill)
async def update_skills_endpoint(
    skills_id: int,
    skills: Skill,
    db: AsyncSession = Depends(get_session),
) -> Skill:
    try:
        return await update_skills(db, skills_id, skills)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{skills_id}", response_model=Skill)
async def delete_skills_endpoint(
    skills_id: int,
    db: AsyncSession = Depends(get_session),
) -> Skill:
    try:
        return await delete_skills(db, skills_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
