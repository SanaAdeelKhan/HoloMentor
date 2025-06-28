from uagents import Agent, Context
from pydantic import BaseModel

class PingMessage(BaseModel):
    text: str

class EchoMessage(BaseModel):
    text: str

agent = Agent(
    name="EchoAgent",
    port=8000,import logging
from uagents import Agent, Context, Model

logging.basicConfig(level=logging.INFO)

class Message(Model):
    message: str

TEST_AGENT_ADDRESS = "agent1qvc9h0nsndzzq4s5suzw33n7x2kya7ull77z7mlrysql7tlsgptuwf65nqu"

explain_agent = Agent(
    name="explain_agent",
    seed="explain_agent recovery phrase",
    port=8001,
    endpoint=["http://localhost:8001/submit"]
)

replied = False

@explain_agent.on_message(model=Message)
async def explain_agent_message_handler(ctx: Context, sender: str, msg: Message):
    global replied
    ctx.logger.info(f"💬 Received message from {sender}: {msg.message}")
    if not replied:
        ctx.logger.info("Replying to TEST_AGENT...")
        await ctx.send(TEST_AGENT_ADDRESS, Message(message="hello there TEST_AGENT"))
        replied = True

if __name__ == "__main__":
    explain_agent.run()

    endpoint=["http://127.0.0.1:8000"],
    allowed_hosts=["*"]  # 👈 this is key!
)

@agent.on_message(model=PingMessage)
async def reply(ctx: Context, msg: PingMessage):
    print(f"📩 Received: {msg.text}")
    await ctx.send(ctx.sender, EchoMessage(text=f"You said: {msg.text}"))

if __name__ == "__main__":
    with open("echo_agent_address.txt", "w") as f:
        f.write(agent.address)
    print(f"🆔 EchoAgent Address: {agent.address}")
    agent.run()
