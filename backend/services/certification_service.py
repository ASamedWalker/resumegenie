from sqlalchemy.ext.asyncio import AsyncSession
from .nlp_service import extract_skills
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.certification import Certification
from schemas.certification_schema import (
    CertificationCreate,
    CertificationUpdate,
    CertificationRead,
)

logger = logging.getLogger(__name__)


async def create_certification(
    session: AsyncSession, certification_data: CertificationCreate
):
    try:
        new_certification = Certification(**certification_data.dict())
        session.add(new_certification)
        await session.commit()
        await session.refresh(new_certification)
        return new_certification
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


async def get_certification(session: AsyncSession, certification_id: int):
    try:
        statement = select(Certification).where(Certification.id == certification_id)
        result = await session.execute(statement)
        certification = result.scalars().first()
        if certification is None:
            raise HTTPException(status_code=404, detail="Certification not found")
        return certification
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def get_all_certifications(session: AsyncSession):
    try:
        statement = select(Certification)
        result = await session.execute(statement)
        certifications = result.scalars().all()
        return certifications
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_certification(
    session: AsyncSession,
    certification_id: int,
    certification_data: CertificationUpdate,
):
    try:
        statement = select(Certification).where(Certification.id == certification_id)
        result = await session.execute(statement)
        db_certification = result.scalars().first()
        if db_certification is None:
            raise HTTPException(status_code=404, detail="Certification not found")
        for key, value in certification_data.dict(exclude_unset=True).items():
            setattr(db_certification, key, value)
        await session.commit()
        return db_certification
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


async def delete_certification(session: AsyncSession, certification_id: int):
    try:
        statement = select(Certification).where(Certification.id == certification_id)
        result = await session.execute(statement)
        db_certification = result.scalars().first()
        session.delete(db_certification)
        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )
