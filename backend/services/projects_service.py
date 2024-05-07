from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.projects import Projects

logger = logging.getLogger(__name__)


async def create_projects(session: AsyncSession, projects: Projects):
    try:
        session.add(projects)
        await session.commit()
        await session.refresh(projects)
        return projects
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def get_projects(session: AsyncSession, projects_id: int):
    try:
        statement = select(Projects).where(Projects.id == projects_id)
        result = await session.execute(statement)
        projects = result.scalars().first()
        if projects is None:
            raise HTTPException(status_code=404, detail="Projects not found")
        return projects
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def get_all_projects(session: AsyncSession):
    try:
        statement = select(Projects)
        result = await session.execute(statement)
        projects = result.scalars().all()
        return projects
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_projects(session: AsyncSession, projects_id: int, projects: Projects):
    try:
        statement = select(Projects).where(Projects.id == projects_id)
        result = await session.execute(statement)
        db_projects = result.scalars().first()
        if db_projects is None:
            raise HTTPException(status_code=404, detail="Projects not found")
        for key, value in projects.dict().items():
            setattr(db_projects, key, value) if value else None
        session.add(db_projects)
        await session.commit()
        await session.refresh(db_projects)
        return db_projects
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


async def delete_projects(session: AsyncSession, projects_id: int):
    try:
        statement = select(Projects).where(Projects.id == projects_id)
        result = await session.execute(statement)
        db_projects = result.scalars().first()
        if db_projects is None:
            raise HTTPException(status_code=404, detail="Projects not found")
        session.delete(db_projects)
        await session.commit()
        return db_projects
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
