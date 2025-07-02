# test_agent.py

from uagents import Agent, Context, Model
from typing import List

# 🔹 Message model
class Message(Model):
    message: str

class TestResponse(Model):
    test_cases: List[str]

# 🔹 Define the agent
test_agent = Agent(
    name="test_agent",
    seed="test-agent fixed seed phrase",
    port=8004,
    endpoint=["http://localhost:8004/submit"]
)

@test_agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info(f"🧪 test_agent address: {ctx.agent.address}")

@test_agent.on_message(model=Message)
async def handle_test_request(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"📥 Received contract for test generation:\n{msg.message}")

    contract = msg.message
    test_scenarios = []

    # 🔹 Basic heuristic to suggest test cases
    if "function get()" in contract:
        test_scenarios.append("✅ Test that calling `get()` returns 1.")
        test_scenarios.append("⚠️ Check if `get()` is publicly accessible.")
        test_scenarios.append("🧪 Validate gas usage of calling `get()`.")
    else:
        test_scenarios.append("❓ No callable function detected for testing.")

    # 🔹 Respond to client
    await ctx.send(sender, TestResponse(test_cases=test_scenarios))
    ctx.logger.info(f"✅ Sent test scenarios to {sender}")

# 🔹 Run the agent
if __name__ == "__main__":
    test_agent.run()
