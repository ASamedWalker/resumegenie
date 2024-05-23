from sqlalchemy.ext.asyncio import AsyncSession
from .nlp_service import extract_skills
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.experience import Experience
from schemas.experience_schema import ExperienceCreate, ExperienceUpdate, ExperienceRead

logger = logging.getLogger(__name__)


async def create_experience(session: AsyncSession, experience_data: ExperienceCreate):
    try:
        new_experience = Experience(**experience_data.dict())
        session.add(new_experience)
        await session.commit()
        await session.refresh(new_experience)
        return new_experience
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


async def get_experience(session: AsyncSession, experience_id: int):
    try:
        statement = select(Experience).where(Experience.id == experience_id)
        result = await session.execute(statement)
        experience = result.scalars().first()
        if experience is None:
            raise HTTPException(status_code=404, detail="Experience not found")
        return experience
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def get_all_experiences(session: AsyncSession):
    try:
        statement = select(Experience)
        result = await session.execute(statement)
        experiences = result.scalars().all()
        return experiences
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_experience(
    session: AsyncSession, experience_id: int, experience_data: ExperienceUpdate
):
    try:
        statement = select(Experience).where(Experience.id == experience_id)
        result = await session.execute(statement)
        db_experience = result.scalars().first()
        if db_experience is None:
            raise HTTPException(status_code=404, detail="Experience not found")
        for key, value in experience_data.dict(exclude_unset=True).items():
            setattr(db_experience, key, value)
        await session.commit()
        await session.refresh(db_experience)
        return db_experience
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


async def delete_experience(session: AsyncSession, experience_id: int):
    try:
        statement = select(Experience).where(Experience.id == experience_id)
        result = await session.execute(statement)
        db_experience = result.scalars().first()
        if db_experience is None:
            raise HTTPException(status_code=404, detail="Experience not found")
        session.delete(db_experience)
        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )
