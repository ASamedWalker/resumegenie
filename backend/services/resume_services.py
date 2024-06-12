from sqlalchemy.ext.asyncio import AsyncSession
from .nlp_service import extract_skills
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.resume import Resume
from schemas.resume_schema import ResumeCreate, ResumeUpdate

logger = logging.getLogger(__name__)


async def create_resume(session: AsyncSession, resume_data: ResumeCreate):
    try:
        # Convert Pydantic model to dictionary for ORM model creation
        logger.debug(f"Creating resume with data: {resume_data.dict()}")
        new_resume = Resume(**resume_data.dict())
        session.add(new_resume)
        await session.commit()
        await session.refresh(new_resume)
        return new_resume
    except SQLAlchemyError as e:
        await session.rollback()
        logger.error(f"Database error during resume creation: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        logger.error(f"Failed to create resume: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


async def get_resume(session: AsyncSession, resume_id: int):
    try:
        statement = (
            select(Resume)
            .options(
                selectinload(Resume.skills),
                selectinload(Resume.projects),
                selectinload(Resume.experiences),
                selectinload(Resume.certifications),
            )
            .where(Resume.id == resume_id)
        )
        result = await session.execute(statement)
        resume = result.scalars().first()
        return resume
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def get_all_resumes(session: AsyncSession):
    try:
        statement = select(Resume)
        result = await session.execute(statement)
        resumes = result.scalars().all()
        return resumes
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_resume(
    session: AsyncSession, resume_id: int, update_data: ResumeUpdate
):
    try:
        statement = select(Resume).where(Resume.id == resume_id)
        result = await session.execute(statement)
        db_resume = result.scalars().first()
        if db_resume is None:
            raise HTTPException(status_code=404, detail="Resume not found")

        # Convert Pydantic model to dictionary excluding unset values
        update_dict = update_data.dict(exclude_unset=True)

        for key, value in update_dict.items():
            setattr(db_resume, key, value)

        session.add(db_resume)
        await session.commit()
        await session.refresh(db_resume)
        return db_resume

    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def delete_resume(session: AsyncSession, resume_id: int):
    try:
        result = await session.execute(select(Resume).where(Resume.id == resume_id))
        resume = result.scalars().first()
        if not resume:
            raise HTTPException(status_code=404, detail="Resume not found")

        await session.delete(resume)
        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
