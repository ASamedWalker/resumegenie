from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from sqlmodel import select
from models.certification import Certification
from services.certification_service import (
    create_certification,
    get_certification,
    get_all_certifications,
    update_certification,
    delete_certification,
)
from schemas.certification_schema import (
    CertificationCreate,
    CertificationUpdate,
    CertificationRead,
)
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/certifications", tags=["Certifications"])


@router.post("/", response_model=Certification, status_code=201)
async def create_certification_endpoint(
    certification_data: CertificationCreate,
    db: AsyncSession = Depends(get_session),
) -> Certification:
    try:
        new_certification = await create_certification(db, certification_data)
        if not new_certification:
            raise HTTPException(
                status_code=404, detail="Failed to create certification"
            )
        return new_certification
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


@router.get("/{certification_id}", response_model=Certification)
async def get_certification_endpoint(
    certification_id: int,
    db: AsyncSession = Depends(get_session),
) -> Certification:
    try:
        return await get_certification(db, certification_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=list[Certification])
async def get_all_certifications_endpoint(
    db: AsyncSession = Depends(get_session),
) -> list[Certification]:
    try:
        return await get_all_certifications(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{certification_id}", response_model=Certification)
async def update_certification_endpoint(
    certification_id: int,
    certification_data: CertificationUpdate,
    db: AsyncSession = Depends(get_session),
) -> Certification:
    try:
        return await update_certification(db, certification_id, certification_data)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{certification_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_certification_endpoint(
    certification_id: int,
    db: AsyncSession = Depends(get_session),
):
    try:
        return await delete_certification(db, certification_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )
