from fastapi import FastAPI
from pydantic import BaseModel
from app.brain import responder

app = FastAPI()

class MessageIn(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "API rodando"}

@app.post("/webhook")
def webhook(data: MessageIn):
    reply = responder(data.message)
    return {"reply": reply}
