# explain_agent.py

from uagents import Agent, Context, Model
import os
import httpx

# 🔹 Define Message model
class Message(Model):
    message: str

# 🔹 Define agent
explain_agent = Agent(
    name="explain_agent",
    seed="explain-agent fixed seed phrase for holomentor",
    port=8001,
    endpoint=["http://localhost:8001/submit"]
)

@explain_agent.on_event("startup")
async def show_address(ctx: Context):
    ctx.logger.info(f"📢 explain_agent address: {ctx.agent.address}")

@explain_agent.on_message(model=Message)
async def explain_code(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"💬 Received smart contract from {sender}:\n{msg.message}")

    prompt = f"Explain this smart contract simply:\n\n{msg.message}"
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        ctx.logger.error("❌ GROQ_API_KEY is missing.")
        await ctx.send(sender, Message(message="❌ Missing GROQ API key"))
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
                        {"role": "system", "content": "You are a helpful smart contract explainer."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7
                }
            )

        res_json = response.json()
        if response.status_code == 200 and "choices" in res_json:
            explanation = res_json["choices"][0]["message"]["content"]
            await ctx.send(sender, Message(message=explanation))
            ctx.logger.info("✅ Sent explanation back to client_agent.")
        else:
            ctx.logger.error(f"❌ Bad Groq response: {res_json}")
            await ctx.send(sender, Message(message="❌ Failed to explain."))

    except Exception as e:
        ctx.logger.error(f"❌ Exception during explanation: {e}")
        await ctx.send(sender, Message(message="❌ Internal error."))

if __name__ == "__main__":
    explain_agent.run()
