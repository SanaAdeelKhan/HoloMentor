import logging
from uagents import Agent, Context, Model

logging.basicConfig(level=logging.INFO)

class Message(Model):
    message: str

sigmar = Agent(
    name="sigmar",
    seed="sigmar recovery phrase",
    port=8000,
    endpoint=["http://localhost:8000/submit"]
)

SLAANESH_ADDRESS = "agent1qddw8cfn685e3p082lcn9dxe63yrqf03s77puv4d0as8a4j7c84s572juzj"
replied = False

@sigmar.on_interval(period=3.0)
async def send_message(ctx: Context):
    global replied
    if not replied:
        ctx.logger.info("Sending message to Slaanesh...")
        await ctx.send(SLAANESH_ADDRESS, Message(message="Hello there, Slaanesh!"))
        replied = True

@sigmar.on_message(model=Message)
async def sigmar_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"💬 Received message from {sender}: {msg.message}")

if __name__ == "__main__":
    sigmar.run()
