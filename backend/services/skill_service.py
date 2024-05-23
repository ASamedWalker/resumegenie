from sqlalchemy.ext.asyncio import AsyncSession
from .nlp_service import extract_skills
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.skill import Skill
from schemas.skill_schema import SkillCreate, SkillUpdate, SkillRead

logger = logging.getLogger(__name__)


async def create_skill_db(session: AsyncSession, skill_data: SkillCreate):
    try:
        new_skill = Skill(**skill_data.dict())
        session.add(new_skill)
        await session.commit()
        await session.refresh(new_skill)
        return new_skill
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


async def get_skill_db(session: AsyncSession, skill_id: int):
    try:
        statement = select(Skill).where(Skill.id == skill_id)
        result = await session.execute(statement)
        skill = result.scalars().first()
        if skill is None:
            raise HTTPException(status_code=404, detail="Skill not found")
        return skill
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def get_all_skills_db(session: AsyncSession):
    try:
        statement = select(Skill)
        result = await session.execute(statement)
        skills = result.scalars().all()
        return skills
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_skill_db(
    session: AsyncSession, skill_id: int, skill_data: SkillUpdate
):
    try:
        statement = select(Skill).where(Skill.id == skill_id)
        result = await session.execute(statement)
        db_skill = result.scalars().first()
        if db_skill is None:
            raise HTTPException(status_code=404, detail="Skill not found")
        for key, value in skill_data.dict(exclude_unset=True).items():
            setattr(db_skill, key, value)
        await session.commit()
        await session.refresh(db_skill)
        return db_skill
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


async def delete_skill_db(session: AsyncSession, skill_id: int):
    try:
        statement = select(Skill).where(Skill.id == skill_id)
        result = await session.execute(statement)
        db_skill = result.scalars().first()
        if db_skill is None:
            raise HTTPException(status_code=404, detail="Skill not found")
        session.delete(db_skill)
        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )
