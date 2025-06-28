import os
import httpx
from dotenv import load_dotenv
from src.agents.explain_agent import explain_agent, EXPLAIN_AGENT_ADDRESS

# 🔐 Load API key from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ✅ Declare this BEFORE the function
USE_GROQ = False  # Toggle this to False to fallback to uAgent

# 🔍 Dummy contract resolver for demo/testing
async def fetch_contract_by_address(address: str) -> str:
    MOCK_CONTRACTS = {
        "agent1q0pvyzmsls48wzpqvlk2nuk3knjz7ql0sy6exctjxyc9zkeufxpspguadsg":
            "contract Vote { bool voted = false; void cast() { voted = true; } }"
    }
    return MOCK_CONTRACTS.get(address, None)

# 🧠 Core logic for agent or Groq-based contract explanation
async def send_message_to_agent(input_mode: str, user_input: str):
    try:
        # Build prompt
        if input_mode == "code":
            prompt = f"🔍 Explain this smart contract:\n\n{user_input}"
        elif input_mode == "address":
            contract_code = await fetch_contract_by_address(user_input)
            if not contract_code:
                return f"⚠️ No contract found for address `{user_input}`."
            prompt = f"🔍 Explain the smart contract deployed at `{user_input}`:\n\n{contract_code}"
        else:
            return "❌ Invalid input mode. Use `code` or `address`."

        # 🧪 Debug (you can comment these later)
        print(f"🌐 Mode: {input_mode}")
        print(f"📩 Prompt:\n{prompt}")

        # 🌐 Use Groq LLaMA API
        if USE_GROQ:
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
                return data["choices"][0]["message"]["content"]

        # 🛰️ Fallback to local uAgent
        else:
            result = await explain_agent.query(EXPLAIN_AGENT_ADDRESS, prompt)
            return result["data"]

    except Exception as e:
        return f"🚨 Error: {str(e)}"
