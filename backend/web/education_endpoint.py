from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from sqlmodel import select
from models.education import Education
from services.education_service import (
    create_education,
    get_education,
    get_all_educations,
    update_education,
    delete_education,
)
from schemas.education_schema import EducationCreate, EducationUpdate, EducationRead
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/educations", tags=["Educations"])


@router.post("/", response_model=Education, status_code=201)
async def create_education_endpoint(
    education_data: EducationCreate,
    db: AsyncSession = Depends(get_session),
) -> Education:
    try:
        new_education = await create_education(db, education_data)
        if not new_education:
            raise HTTPException(status_code=404, detail="Failed to create education")
        return new_education
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


@router.get("/{education_id}", response_model=Education)
async def get_education_endpoint(
    education_id: int,
    db: AsyncSession = Depends(get_session),
) -> Education:
    try:
        return await get_education(db, education_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=list[Education])
async def get_all_educations_endpoint(
    db: AsyncSession = Depends(get_session),
) -> list[Education]:
    try:
        return await get_all_educations(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{education_id}", response_model=Education)
async def update_education_endpoint(
    education_id: int,
    education_data: EducationUpdate,
    db: AsyncSession = Depends(get_session),
) -> Education:
    try:
        return await update_education(db, education_id, education_data)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{education_id}", response_model=Education)
async def delete_education_endpoint(
    education_id: int,
    db: AsyncSession = Depends(get_session),
) -> Education:
    try:
        return await delete_education(db, education_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )
