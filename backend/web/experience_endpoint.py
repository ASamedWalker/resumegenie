from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from sqlmodel import select
from models.experience import Experience
from services.experience_service import (
    create_experience,
    get_experience,
    get_all_experiences,
    update_experience,
    delete_experience,
)
from schemas.experience_schema import ExperienceCreate, ExperienceUpdate, ExperienceRead
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/experiences", tags=["Experiences"])


@router.post("/", response_model=Experience, status_code=201)
async def create_experience_endpoint(
    experience_data: ExperienceCreate,
    db: AsyncSession = Depends(get_session),
) -> Experience:
    try:
        new_experience = await create_experience(db, experience_data)
        if not new_experience:
            raise HTTPException(status_code=404, detail="Failed to create experience")
        return new_experience
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


@router.get("/{experience_id}", response_model=Experience)
async def get_experience_endpoint(
    experience_id: int,
    db: AsyncSession = Depends(get_session),
) -> Experience:
    try:
        return await get_experience(db, experience_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=list[Experience])
async def get_all_experiences_endpoint(
    db: AsyncSession = Depends(get_session),
) -> list[Experience]:
    try:
        return await get_all_experiences(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{experience_id}", response_model=Experience)
async def update_experience_endpoint(
    experience_id: int,
    experience_data: ExperienceUpdate,
    db: AsyncSession = Depends(get_session),
) -> Experience:
    try:
        return await update_experience(db, experience_id, experience_data)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{experience_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_experience_endpoint(
    experience_id: int,
    db: AsyncSession = Depends(get_session),
):
    try:
        return await delete_experience(db, experience_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
