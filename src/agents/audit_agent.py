from uagents import Agent, Context, Model
import os
import httpx

# 🔹 Define message models
class Message(Model):
    message: str

class AuditResponse(Model):
    issues: str

# 🔹 Define agent
audit_agent = Agent(
    name="audit_agent",
    seed="audit-agent fixed seed phrase",
    port=8003,
    endpoint=["http://localhost:8003/submit"]
)

@audit_agent.on_event("startup")
async def show_address(ctx: Context):
    ctx.logger.info(f"📢 audit_agent address: {ctx.agent.address}")

@audit_agent.on_message(model=Message)
async def audit_code(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"💬 Received smart contract from {sender}:\n{msg.message}")

    prompt = f"Audit this smart contract simply:\n\n{msg.message}"
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        ctx.logger.error("❌ GROQ_API_KEY is missing.")
        await ctx.send(sender, AuditResponse(issues="❌ Missing GROQ API key"))
        return

    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "meta-llama/llama-4-scout-17b-16e-instruct",
                    "messages": [
                        {"role": "system", "content": "You are a helpful smart contract auditer."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7
                }
            )

        res_json = response.json()
        if response.status_code == 200 and "choices" in res_json:
            audit_text = res_json["choices"][0]["message"]["content"]
            await ctx.send(sender, AuditResponse(issues=audit_text))  # ✅ Send as AuditResponse
            ctx.logger.info("✅ Sent audit response back to client_agent.")
        else:
            ctx.logger.error(f"❌ Bad Groq response: {res_json}")
            await ctx.send(sender, AuditResponse(issues="❌ Failed to audit."))

    except Exception as e:
        ctx.logger.error(f"❌ Exception during audit: {e}")
        await ctx.send(sender, AuditResponse(issues="❌ Internal error during audit."))

if __name__ == "__main__":
    audit_agent.run()
