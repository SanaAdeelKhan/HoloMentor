from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.utils import send_message_to_agent

app = FastAPI()

class Prompt(BaseModel):
    input_mode: str  # "code" or "address"
    user_input: str

@app.post("/ask-explainer/")
async def ask_explainer(data: Prompt):
    response = await send_message_to_agent(data.input_mode, data.user_input)
    return {"response": response}
