import logging
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

# ✅ Don't use `Field()` with Pydantic v1 + uAgents
class Prompt(Model):
    message: str

EXPLAIN_AGENT_ADDRESS = "agent1qwzqqzzqv0rehj8kp8p9uqfu0pd57c9np7zc3x7c5jmhq0dcu3qtq90vsj3"

client_agent = Agent(
    name="client_agent",
    seed="client-agent fixed seed phrase for HoloMentor",
    port=8002,
    endpoint=["http://localhost:8002/submit"]
)

fund_agent_if_low(client_agent.wallet.address())

@client_agent.on_interval(period=5.0)
async def send_prompt_to_explainer(ctx: Context):
    ctx.logger.info("✅ Sending prompt to explainer...")
    await ctx.send(EXPLAIN_AGENT_ADDRESS, Prompt(message="contract Sample { int x; void set(int a) { x = a; } }"))

@client_agent.on_message(model=Prompt)
async def on_explainer_reply(ctx: Context, sender: str, msg: Prompt):
    ctx.logger.info(f"📩 Got reply from explainer:\n{msg.message}")

if __name__ == "__main__":
    client_agent.run()
