from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from models.projects import Projects
from services.resume_services import (
    create_resume,
    get_resume,
    get_all_resumes,
    update_resume,
    delete_resume,
)

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/", response_model=Projects, status_code=status.HTTP_201_CREATED)
async def create_projects_endpoint(
    projects: Projects,
    db: AsyncSession = Depends(get_session),
) -> Projects:
    try:
        return await create_projects(db, projects)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{projects_id}", response_model=Projects)
async def get_projects_endpoint(
    projects_id: int,
    db: AsyncSession = Depends(get_session),
) -> Projects:
    try:
        return await get_projects(db, projects_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=list[Projects])
async def get_all_projects_endpoint(
    db: AsyncSession = Depends(get_session),
) -> list[Projects]:
    try:
        return await get_all_projects(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{projects_id}", response_model=Projects)
async def update_projects_endpoint(
    projects_id: int,
    projects: Projects,
    db: AsyncSession = Depends(get_session),
) -> Projects:
    try:
        return await update_projects(db, projects_id, projects)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{projects_id}", response_model=Projects)
async def delete_projects_endpoint(
    projects_id: int,
    db: AsyncSession = Depends(get_session),
) -> Projects:
    try:
        return await delete_projects(db, projects_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
