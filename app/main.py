from fastapi import FastAPI
from pydantic import BaseModel
from app.brain import responder

app = FastAPI()

class MessageIn(BaseModel):
    from_number: str
    text: str

@app.get("/")
def home():
    return {"status": "API rodando"}

@app.post("/webhook")
def webhook(data: MessageIn):
    reply = responder(
        user_id=data.from_number,
        message=data.text
    )
    return {"reply": reply}
