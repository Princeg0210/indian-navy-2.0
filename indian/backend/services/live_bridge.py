import asyncio
import json
import logging
import websockets
import datetime
import ssl
from .detection_service import ingest_live_message
from config import AIS_STREAM_KEY, BOUNDING_BOXES

import os

logger = logging.getLogger("live_bridge")

# SSL context configuration (Enforce verification by default, allow toggle for dev environments)
VERIFY_SSL = os.getenv("VERIFY_SSL", "true").lower() in ("true", "1", "yes")
ssl_context = ssl.create_default_context()
if not VERIFY_SSL:
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

class AISLiveBridge:
    def __init__(self):
        self.url = "wss://stream.aisstream.io/v0/stream"
        self.running = False
        self._vessel_meta = {}

    async def start(self):
        self.running = True
        logger.info("📡 Connecting to Global Satellite AIS Feed...")
        while self.running:
            try:
                async with websockets.connect(self.url, ssl=ssl_context) as websocket:
                    subscribe_msg = {
                        "APIKey": AIS_STREAM_KEY,
                        "BoundingBoxes": BOUNDING_BOXES
                    }
                    await websocket.send(json.dumps(subscribe_msg))

                    async for message in websocket:
                        if not self.running: break
                        data = json.loads(message)
                        self._process_message(data)
            except Exception as e:
                if self.running:
                    logger.error(f"Live Bridge Connection Delay: {e}")
                    await asyncio.sleep(10)

    def stop(self):
        self.running = False

    def _process_message(self, data):
        msg_type = data.get("MessageType")
        meta = data.get("MetaData", {})
        mmsi = str(meta.get("MMSI"))
        
        if not mmsi: return

        vessel_name = meta.get("VesselName", "").strip() or f"REALTIME_{mmsi}"
        
        if msg_type in ["PositionReport"]:
            payload = data.get("Message", {}).get("PositionReport", {})
            lat = payload.get("Latitude")
            lon = payload.get("Longitude")
            
            if lat and lon:
                ais_msg = {
                    "mmsi": mmsi,
                    "name": vessel_name,
                    "type": self._vessel_meta.get(mmsi, {}).get("type", "Cargo"),
                    "flag": meta.get("Flag", "UN"),
                    "lat": lat,
                    "lon": lon,
                    "sog": payload.get("Sog", 0),
                    "cog": payload.get("Cog", 0),
                    "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
                }
                ingest_live_message(ais_msg)

        elif msg_type == "ShipStaticData":
            payload = data.get("Message", {}).get("ShipStaticData", {})
            self._vessel_meta[mmsi] = {"type": str(payload.get("Type", "Cargo"))}
