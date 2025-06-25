# testgen_agent.py
# Generates C++ test cases for contracts

from uagents import Agent, Context

agent = Agent(name="TestGenAgent")

@agent.on_message()
async def handle_testgen(ctx: Context, msg: str):
    contract = msg
    test = "int test_result = main(); assert(test_result == 21);"
    await ctx.send(ctx.sender, f"🧪 Suggested test:\n{test}")
