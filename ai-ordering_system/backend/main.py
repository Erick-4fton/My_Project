from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai_chain import ask_ai
from product_data import products

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    message: str

@app.post("/ask")
def ask(user_input: UserInput):
    answer = ask_ai(user_input.message, products)
    return {"reply": answer}
