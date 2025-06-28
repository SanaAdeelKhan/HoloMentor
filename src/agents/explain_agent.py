import logging
import os
import httpx
from dotenv import load_dotenv
from uagents import Agent, Context, Model

# 🔐 Load API Key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

logging.basicConfig(level=logging.INFO)

class Message(Model):
    message: str

EXPLAIN_AGENT_ADDRESS = "agent1q0pvyzmsls48wzpqvlk2nuk3knjz7ql0sy6exctjxyc9zkeufxpspguadsg"

explain_agent = Agent(
    name="explain_agent",
    seed="explain-agent fixed seed phrase for holomentor",
    port=8001,
    endpoint=["http://localhost:8001/submit"]
)

@explain_agent.on_message(model=Message)
async def handle_explain_request(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"💬 Received message from {sender}: {msg.message}")

    prompt = f"Explain this smart contract:\n\n{msg.message}"

    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [{"role": "user", "content": prompt}]
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            reply = data["choices"][0]["message"]["content"]

        await ctx.send(sender, Message(message=reply))

    except Exception as e:
        ctx.logger.error(f"❌ Error: {str(e)}")
        await ctx.send(sender, Message(message=f"🚨 Groq Error: {str(e)}"))

if __name__ == "__main__":
    explain_agent.run()
