from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from models.resume import Resume
from services.resume_services import (
    create_resume,
    get_resume,
    get_all_resumes,
    update_resume,
    delete_resume,
)
from schemas.resume_schema import ResumeCreate, ResumeResponse

router = APIRouter(prefix="/resumes", tags=["Resume"])


@router.post("/", response_model=ResumeCreate, status_code=status.HTTP_201_CREATED)
async def create_resume_endpoint(
    resume_data: Resume,
    job_description: str,
    db: AsyncSession = Depends(get_session),
) -> Resume:
    try:
        resume = await create_resume(db, resume_data, job_description)
        if not resume:
            raise HTTPException(status_code=404, detail="Failed to create resume")
        return resume
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{resume_id}", response_model=Resume)
async def get_resume_endpoint(
    resume_id: int,
    db: AsyncSession = Depends(get_session),
) -> Resume:
    try:
        return await get_resume(db, resume_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=list[Resume])
async def get_all_resumes_endpoint(
    db: AsyncSession = Depends(get_session),
) -> list[Resume]:
    try:
        return await get_all_resumes(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{resume_id}", response_model=Resume)
async def update_resume_endpoint(
    resume_id: int,
    resume: Resume,
    db: AsyncSession = Depends(get_session),
) -> Resume:
    try:
        return await update_resume(db, resume_id, resume)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{resume_id}", response_model=Resume)
async def delete_resume_endpoint(
    resume_id: int,
    db: AsyncSession = Depends(get_session),
) -> Resume:
    try:
        return await delete_resume(db, resume_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
