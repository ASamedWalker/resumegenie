from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from data.database import get_session
from models.templates import Template
from services.template_service import (
    create_template,
    get_template,
    update_template,
)
from schemas.template_schema import TemplateCreate, TemplateRead, TemplateUpdate


router = APIRouter(prefix="/templates", tags=["templates"])


@router.post("/", response_model=TemplateRead, status_code=status.HTTP_201_CREATED)
async def create_template_endpoint(
    template_data: TemplateCreate,
    db: AsyncSession = Depends(get_session),
) -> Template:
    try:
        new_template = await create_template(template_data, db)
        if not new_template:
            raise HTTPException(status_code=404, detail="Failed to create template")
        return new_template
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}"
        )


@router.get("/{template_id}", response_model=TemplateRead)
async def get_template_endpoint(
    template_id: int,
    db: AsyncSession = Depends(get_session),
) -> Template:
    try:
        return await get_template(template_id, db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{template_id}", response_model=TemplateRead)
async def update_template_endpoint(
    template_id: int,
    template_data: TemplateUpdate,
    db: AsyncSession = Depends(get_session),
) -> Template:
    try:
        return await update_template(template_id, template_data, db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{template_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_template_endpoint(
    template_id: int,
    db: AsyncSession = Depends(get_session),
):
    try:
        return await delete_template(template_id, db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
