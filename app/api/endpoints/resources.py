from fastapi import APIRouter, Depends, HTTPException
from repositories.resource import ResourceRepository
from api.deps import get_resource_repository
from models.resource import Resource


router = APIRouter()


@router.get("/resources/")
def list_resources(
    scan_id: int = None,
    type: str = None,
    repository: ResourceRepository = Depends(get_resource_repository)
):
    try:
        resources = repository.get_resources(scan_id=scan_id, type=type)
        return {"resources": resources}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/resources/")
def create_resource(
    resource: Resource,
    repository: ResourceRepository = Depends(get_resource_repository)
):
    try:
        repository.create_resource(
            scan_id=resource.scan_id,
            urn=resource.urn,
            name=resource.name,
            type=resource.type,
            date_fetched=resource.date_fetched,
            data=resource.data
        )
        return {"message": "Resource created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
