from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class ContractRequest(BaseModel):
    contract_code: str

@app.post("/submit")
async def submit_contract(req: ContractRequest):
    # ✅ Dummy response for now (simulate successful deployment)
    print("🚀 Received contract code:")
    print(req.contract_code[:100])  # Only print part to avoid huge logs
    return {
        "status": "success",
        "contractIndex": 1,
        "message": "Contract deployed successfully (simulated)"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8005)
