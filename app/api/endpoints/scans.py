from fastapi import APIRouter, Depends, HTTPException
from repositories.scan import ScanRepository
from models.scan import Scan
from api.deps import get_scan_repository


router = APIRouter()


@router.get("/scans/")
def list_scans(repository: ScanRepository = Depends(get_scan_repository)):
    try:
        scans = repository.get_scans()
        return {"scans": scans}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/scans/")
def create_scan(scan: Scan, repository: ScanRepository = Depends(get_scan_repository)):
    try:
        scan_id = repository.create_scan(scan.start, scan.finish)
        return {"scan_id": scan_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
