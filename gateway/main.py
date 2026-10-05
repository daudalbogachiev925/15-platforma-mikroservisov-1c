from fastapi import FastAPI
import httpx

app = FastAPI()

@app.post("/1c/document")
async def create_doc(payload: dict):
    async with httpx.AsyncClient() as c:
        r = await c.post("http://1c-server/hs/api/document", json=payload)
    return {'status': r.status_code, 'body': r.text}
