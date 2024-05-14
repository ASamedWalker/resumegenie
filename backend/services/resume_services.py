from sqlalchemy.ext.asyncio import AsyncSession
from .nlp_service import extract_skills
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.resume import Resume

logger = logging.getLogger(__name__)


async def create_resume(session: AsyncSession, resume_data: dict, job_description: str):
    try:
        skill_names = extract_skills(job_description)
        if not skill_names:
            skill_names = set()

        # Create new Resume instance
        async with session.begin():
            new_resume = Resume(**resume_data)
            session.add(new_resume)
            await session.commit()
            skills = [Skill(name=name, resume_id=new_resume.id, proficiency_level="Unknown") for name in skill_names]
            for skill in skills:
                session.add(skill)
            await session.commit()
            await session.refresh(new_resume)
        return new_resume
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def get_resume(session: AsyncSession, resume_id: int):
    try:
        statement = select(Resume).where(Resume.id == resume_id)
        result = await session.execute(statement)
        resume = result.scalars().first()
        if resume is None:
            raise HTTPException(status_code=404, detail="Resume not found")
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


async def update_resume(session: AsyncSession, resume_id: int, resume: Resume):
    try:
        statement = select(Resume).where(Resume.id == resume_id)
        result = await session.execute(statement)
        db_resume = result.scalars().first()
        if db_resume is None:
            raise HTTPException(status_code=404, detail="Resume not found")
        for key, value in resume.dict().items():
            setattr(db_resume, key, value) if value else None
        session.add(db_resume)
        await session.commit()
        await session.refresh(db_resume)
        return db_resume
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def delete_resume(session: AsyncSession, resume_id: int):
    try:
        statement = select(Resume).where(Resume.id == resume_id)
        result = await session.execute(statement)
        resume = result.scalars().first()
        if resume is None:
            raise HTTPException(status_code=404, detail="Resume not found")
        await session.delete(resume)
        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
