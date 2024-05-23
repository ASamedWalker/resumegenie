from sqlalchemy.ext.asyncio import AsyncSession
from .nlp_service import extract_skills
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging

from models.project import Project
from schemas.project_schema import ProjectCreate, ProjectUpdate, ProjectRead

logger = logging.getLogger(__name__)


async def create_project(session: AsyncSession, project_data: ProjectCreate):
    try:
        new_project = Project(**project_data.dict())
        session.add(new_project)
        await session.commit()
        await session.refresh(new_project)
        return new_project
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )

async def get_project(session: AsyncSession, project_id: int):
    try:
        statement = select(Project).where(Project.id == project_id)
        result = await session.execute(statement)
        project = result.scalars().first()
        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        return project
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

async def get_all_projects(session: AsyncSession):
    try:
        statement = select(Project)
        result = await session.execute(statement)
        projects = result.scalars().all()
        return projects
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

async def update_project(session: AsyncSession, project_id: int, project_data: ProjectUpdate):
    try:
        statement = select(Project).where(Project.id == project_id)
        result = await session.execute(statement)
        db_project = result.scalars().first()
        if db_project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        for key, value in project_data.dict(exclude_unset=True).items():
            setattr(db_project, key, value)
        await session.commit()
        await session.refresh(db_project)
        return db_project
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )

async def delete_project(session: AsyncSession, project_id: int):
    try:
        statement = select(Project).where(Project.id == project_id)
        result = await session.execute(statement)
        db_project = result.scalars().first()
        if db_project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        session.delete(db_project)
        await session.commit()
        return db_project
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )