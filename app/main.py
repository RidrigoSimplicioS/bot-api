from fastapi import FastAPI
from pydantic import BaseModel
from app.brain import responder

app = FastAPI()

# Payload estilo WhatsApp
class WhatsAppMessage(BaseModel):
    from_number: str
    text: str

@app.get("/")
def home():
    return {"status": "API rodando"}

@app.post("/webhook")
def webhook(data: WhatsAppMessage):
    reply = responder(
        user_id=data.from_number,
        message=data.text
    )
    return {
        "to": data.from_number,
        "reply": reply
    }
