from sqlalchemy.ext.asyncio import AsyncSession
from .nlp_service import extract_skills
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.templates import Template
from schemas.template_schema import TemplateCreate, TemplateUpdate, TemplateRead


async def create_template(
    template_data: TemplateCreate, session: AsyncSession
) -> Template:
    try:
        new_template = Template(**template_data.dict())
        session.add(new_template)
        await session.commit()
        await session.refresh(new_template)
        return new_template
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


async def get_template(template_id: int, session: AsyncSession) -> Template:
    try:
        statement = select(Template).where(Template.id == template_id)
        result = await session.execute(statement)
        template = result.scalars().first()
        if template is None:
            raise HTTPException(status_code=404, detail="Template not found")
        return template
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_template(
    template_id: int, template_data: TemplateUpdate, session: AsyncSession
) -> Template:
    try:
        statement = select(Template).where(Template.id == template_id)
        result = await session.execute(statement)
        db_template = result.scalars().first()
        if db_template is None:
            raise HTTPException(status_code=404, detail="Template not found")
        for key, value in template_data.dict(exclude_unset=True).items():
            setattr(db_template, key, value)
        await session.commit()
        await session.refresh(db_template)
        return db_template
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )
