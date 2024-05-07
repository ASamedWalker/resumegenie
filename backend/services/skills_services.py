from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.skills import Skills

logger = logging.getLogger(__name__)


async def create_skills(session: AsyncSession, skills: Skills):
    try:
        session.add(skills)
        await session.commit()
        await session.refresh(skills)
        return skills
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def get_skills(session: AsyncSession, skills_id: int):
    try:
        statement = select(Skills).where(Skills.id == skills_id)
        result = await session.execute(statement)
        skills = result.scalars().first()
        if skills is None:
            raise HTTPException(status_code=404, detail="Skills not found")
        return skills
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def get_all_skills(session: AsyncSession):
    try:
        statement = select(Skills)
        result = await session.execute(statement)
        skills = result.scalars().all()
        return skills
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_skills(session: AsyncSession, skills_id: int, skills: Skills):
    try:
        statement = select(Skills).where(Skills.id == skills_id)
        result = await session.execute(statement)
        db_skills = result.scalars().first()
        if db_skills is None:
            raise HTTPException(status_code=404, detail="Skills not found")
        for key, value in skills.dict().items():
            setattr(db_skills, key, value) if value else None
        session.add(db_skills)
        await session.commit()
        await session.refresh(db_skills)
        return db_skills
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def delete_skills(session: AsyncSession, skills_id: int):
    try:
        statement = select(Skills).where(Skills.id == skills_id)
        result = await session.execute(statement)
        skills = result.scalars().first()
        if skills is None:
            raise HTTPException(status_code=404, detail="Skills not found")
        session.delete(skills)
        await session.commit()
        return skills
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
