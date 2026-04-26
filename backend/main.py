from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="NEXUS v2.0", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {
        "status": "NEXUS ONLINE",
        "version": "2.0.0",
        "databases": {
            "redis": "localhost:6379",
            "postgres": "localhost:5432",
            "neo4j": "localhost:7687",
            "qdrant": "localhost:6333"
        }
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("NEXUS v2.0 WebSocket ONLINE")
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"NEXUS: {data}")
