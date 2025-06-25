# explain_agent.py
# Explains C++ contract code using LLM (OpenAI or ASI:One)

from uagents import Agent, Context

agent = Agent(name="ExplainAgent")

@agent.on_message()
async def handle_explain(ctx: Context, msg: str):
    code = msg
    prompt = f"Explain this C++ smart contract line-by-line:\n\n{code}"
    response = f"[LLM RESPONSE FOR]: {prompt}"  # Replace with real LLM call
    await ctx.send(ctx.sender, response)
