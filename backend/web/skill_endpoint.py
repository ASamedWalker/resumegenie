from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from models.skill import Skill
from services.skill_service import (
    create_skill_db,
    get_skill_db,
    get_all_skills_db,
    update_skill_db,
    delete_skill_db,
)
from schemas.skill_schema import SkillCreate, SkillRead, SkillUpdate

router = APIRouter(prefix="/skills", tags=["skills"])


@router.post("/", response_model=SkillRead, status_code=status.HTTP_201_CREATED)
async def create_skill_endpoint(
    skill_data: SkillCreate,
    db: AsyncSession = Depends(get_session),
) -> Skill:
    try:
        if not skill_data.resume_id:
            raise HTTPException(status_code=400, detail="Resume ID is required")
        new_skill = await create_skill_db(db, skill_data)
        if not new_skill:
            raise HTTPException(status_code=404, detail="Failed to create skill")
        return new_skill
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


@router.get("/{skill_id}", response_model=SkillRead)
async def get_skill_endpoint(
    skill_id: int,
    db: AsyncSession = Depends(get_session),
) -> Skill:
    try:
        return await get_skill_db(skill_id, db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/", response_model=SkillRead)
async def get_all_skills_endpoint(
    db: AsyncSession = Depends(get_session),
) -> List[Skill]:
    try:
        return await get_all_skills_db(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{skill_id}", response_model=SkillRead)
async def update_skill_endpoint(
    skill_id: int,
    skill_data: SkillUpdate,
    db: AsyncSession = Depends(get_session),
) -> Skill:
    try:
        return await update_skill_db(skill_id, skill_data, db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


@router.delete("/{skill_id}", response_model=SkillRead)
async def delete_skill_endpoint(
    skill_id: int,
    db: AsyncSession = Depends(get_session),
) -> Skill:
    try:
        return await delete_skill_db(skill_id, db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )
