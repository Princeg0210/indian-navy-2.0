from typing import List, Optional
from fastapi import APIRouter, Query, HTTPException
from services.detection_service import (
    get_all_alerts, get_vessel_registry_enhanced, get_vessel_track, get_alert_by_mmsi,
    get_summary_stats, get_global_history, get_vessel_operational_history,
    get_search_criteria_stats, get_map_layers
)

router = APIRouter(prefix="/api/vessels", tags=["vessels"])

@router.get("/layers")
async def fetch_layers():
    """Retrieve tactical map layers (Shoreline, IUU, etc.)."""
    layers = get_map_layers()
    return layers if layers else []

@router.get("/search-stats")
async def fetch_search_stats():
    """Retrieve tactical activity criteria counts for the search engine."""
    return get_search_criteria_stats()

@router.get("/history")
async def get_traffic_history(hours: int = 1):
    return {"history": get_global_history(hours=hours)}

@router.get("/history/{mmsi}")
async def fetch_vessel_history(mmsi: str, hours: int = 24):
    """Retrieve detailed history for a specific vessel."""
    return get_vessel_operational_history(mmsi, hours)

@router.get("")
async def list_vessels(
    anomalous_only: bool = Query(False),
    vessel_type: Optional[str] = Query(None)
):
    """Returns the full fleet with specifications and filtering."""
    vessels = get_vessel_registry_enhanced()
    
    if anomalous_only or vessel_type:
        filtered = []
        for v in vessels:
            if anomalous_only and v.get("severity") == "NORMAL": continue
            if vessel_type and v.get("type", "").lower() != vessel_type.lower(): continue
            filtered.append(v)
        return {"vessels": filtered}
    
    return {"vessels": vessels}

@router.get("/{mmsi}")
def get_vessel(mmsi: str):
    alert = get_alert_by_mmsi(mmsi)
    if not alert:
        raise HTTPException(status_code=404, detail=f"Vessel {mmsi} not found")

    track = get_vessel_track(mmsi)
    return {
        **alert,
        "track_history": track
    }
