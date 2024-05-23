from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from sqlmodel import select
from models.project import Project
from services.project_service import (
    create_project,
    get_project,
    get_all_projects,
    update_project,
    delete_project,
)
from schemas.project_schema import ProjectCreate, ProjectUpdate, ProjectRead
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/", response_model=Project, status_code=201)
async def create_project_endpoint(
    project_data: ProjectCreate,
    db: AsyncSession = Depends(get_session),
) -> Project:
    try:
        new_project = await create_project(db, project_data)
        if not new_project:
            raise HTTPException(status_code=404, detail="Failed to create project")
        return new_project
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


@router.get("/{project_id}", response_model=Project)
async def get_project_endpoint(
    project_id: int,
    db: AsyncSession = Depends(get_session),
) -> Project:
    try:
        return await get_project(db, project_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=list[Project])
async def get_all_projects_endpoint(
    db: AsyncSession = Depends(get_session),
) -> list[Project]:
    try:
        return await get_all_projects(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{project_id}", response_model=Project)
async def update_project_endpoint(
    project_id: int,
    project_data: ProjectUpdate,
    db: AsyncSession = Depends(get_session),
) -> Project:
    try:
        return await update_project(db, project_id, project_data)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{project_id}", response_model=Project)
async def delete_project_endpoint(
    project_id: int,
    db: AsyncSession = Depends(get_session),
) -> Project:
    try:
        return await delete_project(db, project_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )
