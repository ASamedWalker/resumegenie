from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.certifications import Certifications

logger = logging.getLogger(__name__)


async def create_certifications(session: AsyncSession, certifications: Certifications):
    try:
        session.add(certifications)
        await session.commit()
        await session.refresh(certifications)
        return certifications
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def get_certifications(session: AsyncSession, certifications_id: int):
    try:
        statement = select(Certifications).where(Certifications.id == certifications_id)
        result = await session.execute(statement)
        certifications = result.scalars().first()
        if certifications is None:
            raise HTTPException(status_code=404, detail="Certifications not found")
        return certifications
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def get_all_certifications(session: AsyncSession):
    try:
        statement = select(Certifications)
        result = await session.execute(statement)
        certifications = result.scalars().all()
        return certifications
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_certifications(
    session: AsyncSession, certifications_id: int, certifications: Certifications
):
    try:
        statement = select(Certifications).where(Certifications.id == certifications_id)
        result = await session.execute(statement)
        db_certifications = result.scalars().first()
        if db_certifications is None:
            raise HTTPException(status_code=404, detail="Certifications not found")
        for key, value in certifications.dict().items():
            setattr(db_certifications, key, value) if value else None
        session.add(db_certifications)
        await session.commit()
        await session.refresh(db_certifications)
        return db_certifications
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def delete_certifications(session: AsyncSession, certifications_id: int):
    try:
        statement = select(Certifications).where(Certifications.id == certifications_id)
        result = await session.execute(statement)
        db_certifications = result.scalars().first()
        if db_certifications is None:
            raise HTTPException(status_code=404, detail="Certifications not found")
        session.delete(db_certifications)
        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
