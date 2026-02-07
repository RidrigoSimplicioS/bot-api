from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from app.brain import responder

app = FastAPI()
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from app.brain import responder

class MessageIn(BaseModel):
    from_number: Optional[str] = None
    text: Optional[str] = None
    from_: Optional[str] = None
    message: Optional[str] = None

@app.get("/")
def home():
    return {"status": "API rodando"}

@app.post("/webhook")
def webhook(data: MessageIn):

    number = data.from_number or data.from_
    text = data.text or data.message

    if not number or not text:
        return {"error": "Campos inválidos"}

    reply = responder(number, text)

    return {
        "to": number,
        "reply": reply
    }
