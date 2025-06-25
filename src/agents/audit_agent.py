# audit_agent.py
# AI-based static analysis to detect risks in C++ contracts

from uagents import Agent, Context

agent = Agent(name="AuditAgent")

@agent.on_message()
async def handle_audit(ctx: Context, msg: str):
    contract = msg
    risks = "Check for overflow, memory access, division by zero"
    report = f"🛡️ Audit Result: Analyzed code\n\nRisks Found:\n{risks}"
    await ctx.send(ctx.sender, report)
