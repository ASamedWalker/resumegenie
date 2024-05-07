from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from models.certifications import Certifications
from services.resume_services import (
    create_resume,
    get_resume,
    get_all_resumes,
    update_resume,
    delete_resume,
)

router = APIRouter(prefix="/certifications", tags=["Certifications"])


@router.post("/", response_model=Certifications, status_code=status.HTTP_201_CREATED)
async def create_certifications_endpoint(
    certifications: Certifications,
    db: AsyncSession = Depends(get_session),
) -> Certifications:
    try:
        return await create_certifications(db, certifications)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{certifications_id}", response_model=Certifications)
async def get_certifications_endpoint(
    certifications_id: int,
    db: AsyncSession = Depends(get_session),
) -> Certifications:
    try:
        return await get_certifications(db, certifications_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=list[Certifications])
async def get_all_certifications_endpoint(
    db: AsyncSession = Depends(get_session),
) -> list[Certifications]:
    try:
        return await get_all_certifications(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{certifications_id}", response_model=Certifications)
async def update_certifications_endpoint(
    certifications_id: int,
    certifications: Certifications,
    db: AsyncSession = Depends(get_session),
) -> Certifications:
    try:
        return await update_certifications(db, certifications_id, certifications)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{certifications_id}", response_model=Certifications)
async def delete_certifications_endpoint(
    certifications_id: int,
    db: AsyncSession = Depends(get_session),
) -> Certifications:
    try:
        return await delete_certifications(db, certifications_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
