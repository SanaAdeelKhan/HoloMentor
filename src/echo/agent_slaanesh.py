import logging
from uagents import Agent, Context, Model

logging.basicConfig(level=logging.INFO)

class Message(Model):
    message: str

SIGMAR_ADDRESS = "agent1qdtmapxwfljj2xwz8yqpljd75tmnxjjdmrta86q68aqf5r9d7nw7kqyt40p"

slaanesh = Agent(
    name="slaanesh",
    seed="slaanesh recovery phrase",
    port=8001,
    endpoint=["http://localhost:8001/submit"]
)

replied = False

@slaanesh.on_message(model=Message)
async def slaanesh_message_handler(ctx: Context, sender: str, msg: Message):
    global replied
    ctx.logger.info(f"💬 Received message from {sender}: {msg.message}")
    if not replied:
        ctx.logger.info("Replying to Sigmar...")
        await ctx.send(SIGMAR_ADDRESS, Message(message="hello there sigmar"))
        replied = True

if __name__ == "__main__":
    slaanesh.run()
