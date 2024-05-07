from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.education import Education

logger = logging.getLogger(__name__)


async def create_education(session: AsyncSession, education: Education):
    try:
        session.add(education)
        await session.commit()
        await session.refresh(education)
        return education
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def get_education(session: AsyncSession, education_id: int):
    try:
        statement = select(Education).where(Education.id == education_id)
        result = await session.execute(statement)
        education = result.scalars().first()
        if education is None:
            raise HTTPException(status_code=404, detail="Education not found")
        return education
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def get_all_education(session: AsyncSession):
    try:
        statement = select(Education)
        result = await session.execute(statement)
        education = result.scalars().all()
        return education
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_education(
    session: AsyncSession, education_id: int, education: Education
):
    try:
        statement = select(Education).where(Education.id == education_id)
        result = await session.execute(statement)
        db_education = result.scalars().first()
        if db_education is None:
            raise HTTPException(status_code=404, detail="Education not found")
        for key, value in education.dict().items():
            setattr(db_education, key, value) if value else None
        session.add(db_education)
        await session.commit()
        await session.refresh(db_education)
        return db_education
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def delete_education(session: AsyncSession, education_id: int):
    try:
        statement = select(Education).where(Education.id == education_id)
        result = await session.execute(statement)
        db_education = result.scalars().first()
        if db_education is None:
            raise HTTPException(status_code=404, detail="Education not found")
        session.delete(db_education)
        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
