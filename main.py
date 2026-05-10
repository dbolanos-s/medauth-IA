from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="MedAuth Proxy")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

DIFY_API_KEY = os.getenv("DIFY_API_KEY")
DIFY_URL     = os.getenv("DIFY_URL", "https://api.dify.ai/v1").rstrip("/")

class ChatRequest(BaseModel):
    query: str
    conversation_id: str = ""

@app.post("/chat")
async def chat(req: ChatRequest):
    if not DIFY_API_KEY:
        raise HTTPException(500, "API Key no configurada en el servidor.")

    payload = {
        "inputs": {},
        "query": req.query,
        "response_mode": "streaming",
        "conversation_id": req.conversation_id,
        "user": "medauth-tester",
    }

    full_answer = ""
    conversation_id = req.conversation_id

    async with httpx.AsyncClient(timeout=120) as client:
        async with client.stream(
            "POST",
            f"{DIFY_URL}/chat-messages",
            headers={
                "Authorization": f"Bearer {DIFY_API_KEY}",
                "Content-Type": "application/json",
            },
            json=payload,
        ) as resp:
            if resp.status_code != 200:
                body = await resp.aread()
                raise HTTPException(resp.status_code, body.decode())

            async for line in resp.aiter_lines():
                if not line.startswith("data:"):
                    continue
                data_str = line[5:].strip()
                if data_str == "[DONE]":
                    break
                try:
                    data = json.loads(data_str)
                except Exception:
                    continue

                event = data.get("event", "")

                # Captura el conversation_id
                if "conversation_id" in data and not conversation_id:
                    conversation_id = data["conversation_id"]

                # Acumula el texto de la respuesta
                if event == "message" or event == "agent_message":
                    full_answer += data.get("answer", "")

                # Mensaje final completo (algunos agentes lo mandan aquí)
                elif event == "message_end":
                    if not full_answer:
                        full_answer = data.get("answer", "")

    if not full_answer:
        full_answer = "El agente no devolvió respuesta. Verifica tu configuración en Dify."

    return {
        "answer": full_answer,
        "conversation_id": conversation_id,
    }
