import logging
from uagents import Agent, Context, Model

logging.basicConfig(level=logging.INFO)

class Message(Model):
    message: str

test_agent = Agent(
    name="test_agent",
    seed="test_agent recovery phrase",
    port=8000,
    endpoint=["http://localhost:8000/submit"]
)

EXPLAIN_AGENT_ADDRESS = "agent1q0pvyz0zx7j2zqjee39dcpt6854uyvghp493vzhfyz5v27d2m9907u4yfkq"
replied = False

@test_agent.on_interval(period=3.0)
async def send_message(ctx: Context):
    global replied
    if not replied:
        ctx.logger.info("Sending message to EXPLAIN_AGENT...")
        await ctx.send(EXPLAIN_AGENT_ADDRESS, Message(message="Hello there, EXPLAIN_AGENT!"))
        replied = True

@test_agent.on_message(model=Message)
async def test_agent_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"💬 Received message from {sender}: {msg.message}")

if __name__ == "__main__":
    test_agent.run()
