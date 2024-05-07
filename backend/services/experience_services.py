from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.experience import Experience

logger = logging.getLogger(__name__)


async def create_experience(session: AsyncSession, experience: Experience):
    try:
        session.add(experience)
        await session.commit()
        await session.refresh(experience)
        return experience
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


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


async def get_all_experience(session: AsyncSession):
    try:
        statement = select(Experience)
        result = await session.execute(statement)
        experience = result.scalars().all()
        return experience
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_experience(
    session: AsyncSession, experience_id: int, experience: Experience
):
    try:
        statement = select(Experience).where(Experience.id == experience_id)
        result = await session.execute(statement)
        db_experience = result.scalars().first()
        if db_experience is None:
            raise HTTPException(status_code=404, detail="Experience not found")
        for key, value in experience.dict().items():
            setattr(db_experience, key, value) if value else None
        session.add(db_experience)
        await session.commit()
        await session.refresh(db_experience)
        return db_experience
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def delete_experience(session: AsyncSession, experience_id: int):
    try:
        statement = select(Experience).where(Experience.id == experience_id)
        result = await session.execute(statement)
        experience = result.scalars().first()
        if experience is None:
            raise HTTPException(status_code=404, detail="Experience not found")
        session.delete(experience)
        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
