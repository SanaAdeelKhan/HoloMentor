import sys
import os

# ✅ Add src/ to path for `messages`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ✅ Add root (HoloMentor/) to path for `qubic`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from uagents import Agent, Context, Model
from fastapi import FastAPI, Request
import uvicorn
import threading
import time
from typing import Optional, List

from messages.client import ClientMessage
from messages.response import ResponseMessage
from qubic.track import track_contract

# 🔹 Shared state
latest_contract_message: Optional[str] = None
latest_contract_name: Optional[str] = None
latest_explanation: Optional[str] = None
latest_audit_result: Optional[str] = None
latest_test_result: Optional[List[str]] = None

# 🔹 Message models
class Message(Model):
    message: str

class AuditResponse(Model):
    issues: str

class TestResponse(Model):
    test_cases: List[str]

# 🔹 Agent definition
client_agent = Agent(
    name="client_agent",
    seed="client recovery phrase",
    port=8002,
    endpoint=["http://localhost:8002/submit"]
)

# 🔹 FastAPI app
app = FastAPI()

@app.post("/submit")
async def submit_contract(request: Request):
    global latest_contract_message, latest_contract_name
    data = await request.json()
    contract_code = data.get("contract_code", "").strip()
    contract_name = data.get("contract_name", "UnnamedContract")
    if contract_code:
        latest_contract_message = contract_code
        latest_contract_name = contract_name
        return {"status": "success", "message": "Contract submitted to agent."}
    return {"status": "error", "message": "No contract_code provided."}

@app.get("/result")
async def get_result():
    if latest_explanation:
        return {"status": "success", "explanation": latest_explanation}
    return {"status": "pending", "message": "Explanation not received yet."}

@app.get("/audit_result")
async def get_audit_result():
    if latest_audit_result:
        return {"status": "success", "audit": latest_audit_result}
    return {"status": "pending", "message": "Audit result not received yet."}

@app.get("/test_result")
async def get_test_result():
    if latest_test_result:
        return {
            "status": "success",
            "tests": "\n".join(latest_test_result)
        }
    return {"status": "pending", "message": "Test result not received yet."}

# 🔹 Periodic broadcast to all agents + Track contract
@client_agent.on_interval(period=5.0)
async def try_sending(ctx: Context):
    global latest_contract_message, latest_contract_name
    if latest_contract_message:
        ctx.logger.info("🚀 Sending contract to all agents...")

        # Track contract
        track_result = track_contract(
            latest_contract_message,
            latest_contract_name or "UnnamedContract"
        )
        ctx.logger.info(f"✅ Tracked contract: {track_result['contract_name']}")

        # Send contract to target agents
        await ctx.send(EXPLAIN_AGENT_ADDRESS, Message(message=latest_contract_message))
        await ctx.send(AUDIT_AGENT_ADDRESS, Message(message=latest_contract_message))
        await ctx.send(TEST_AGENT_ADDRESS, Message(message=latest_contract_message))

        # Reset buffer
        latest_contract_message = None
        latest_contract_name = None

# 🔹 Receive explanation response
@client_agent.on_message(model=Message)
async def receive_explanation(ctx: Context, sender: str, msg: Message):
    global latest_explanation
    latest_explanation = msg.message
    ctx.logger.info(f"📥 Received explanation:\n{msg.message}")

# 🔹 Receive audit result
@client_agent.on_message(model=AuditResponse)
async def handle_audit_result(ctx: Context, sender: str, msg: AuditResponse):
    global latest_audit_result
    latest_audit_result = msg.issues
    ctx.logger.info(f"🛡️ Received audit response:\n{msg.issues}")

# 🔹 Receive test results
@client_agent.on_message(model=TestResponse)
async def handle_test_result(ctx: Context, sender: str, msg: TestResponse):
    global latest_test_result
    latest_test_result = msg.test_cases
    ctx.logger.info("🧪 Received test cases:")
    for test in msg.test_cases:
        ctx.logger.info(f"- {test}")

# 🔹 Target agent addresses (hardcoded for now)
EXPLAIN_AGENT_ADDRESS = "agent1qwzqqzzqv0rehj8kp8p9uqfu0pd57c9np7zc3x7c5jmhq0dcu3qtq90vsj3"
AUDIT_AGENT_ADDRESS   = "agent1qw7f2fdy95qtf8z59rl88zxudej39usxswhzrajfdessd8rwtr0jvn947r8"
TEST_AGENT_ADDRESS    = "agent1qgk69l4zc0watehgyce8h30cjw9lylz07yqm2evlemh9jalt6fwp7z3laqp"

# 🔹 Run agent and FastAPI server
if __name__ == "__main__":
    threading.Thread(target=client_agent.run, daemon=True).start()
    threading.Thread(target=lambda: uvicorn.run(app, host="0.0.0.0", port=8005), daemon=True).start()
    while True:
        time.sleep(1)
