# 🧠 HoloMentor: The Qubic AI Knowledge Guider

An AI-powered holographic mentor that teaches, audits, and helps you interact with decentralized C++ smart contracts on the Qubic Network using agent-based architecture powered by Fetch.ai, Groq, and ASI:One.

---

## 🌟 What is HoloMentor?

HoloMentor is an intelligent, agentic assistant designed to empower developers, auditors, and learners in the blockchain ecosystem.

It acts as a sci-fi librarian that enables users to:

- 🔍 Understand C++ smart contract code line-by-line  
- 🔐 Audit logic for vulnerabilities and risky patterns  
- 🧪 Generate test cases with AI assistance  
- 🌐 Interact with tick-based Qubic smart contracts  
- 🤖 Deploy and register agents using Fetch.ai uAgents and ASI:One  
- 🧬 Get fast reasoning via Groq + LLaMA  
- 🪩 Experience it all through a futuristic holographic UI  

---

## 🛠️ Core Features

| Feature         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| 🧠 ExplainAgent | Explains uploaded Qubic C++ contracts step-by-step using LLaMA (via Groq)   |
| 🛡️ AuditAgent   | Analyzes contract logic and identifies common vulnerabilities               |
| 🧪 TestAgent    | Suggests or generates unit test cases                                       |
| 🌐 Agentverse   | ASI:One decentralized agent registration and discovery                      |
| 📊 Qubic Explorer | Queries tick-based contract states, balances, and metadata                |
| 🎮 Sci-Fi UI    | Built using React + TailwindCSS for glowing, holographic effects            |

---

## 👨‍💻 Tech Stack

| Layer       | Stack                                                                         |
|-------------|-------------------------------------------------------------------------------|
| Frontend    | React, TailwindCSS, Vite                                                      |
| Backend     | FastAPI, Python                                                               |
| Agents      | Fetch.ai uAgents, ASI:One, Agentverse                                         |
| AI Models   | Groq + LLaMA (primary), OpenAI/Gemini (optional fallback)                     |
| Smart Contracts | C++ on Qubic Testnet                                                      |
| Optional    | MCP, Coral Protocol, Groq Cloud API                                           |

---

## 🧠 Example Use Cases

### ✅ Option 1: Direct via Groq + LLaMA

- User uploads a contract via the UI.  
- Backend FastAPI calls Groq’s LLaMA API directly.  
- The explanation is rendered in the UI instantly.

### ✅ Option 2: ExplainAgent via Fetch.ai (uAgents + ASI:One)

- User uploads a smart contract via the Holo UI.  
- Frontend sends it to a local TestAgent, which relays it to ExplainAgent.  
- ExplainAgent, registered on ASI:One and running with uAgents, receives the contract.  
- It internally calls the Groq + LLaMA API for explanation.  
- Response is returned via agent messaging and shown in the UI.

---

## ✅ Benefits

- 🔗 Connected to ASI:One for decentralized identity  
- 🛡️ Modular, composable — can trigger AuditAgent or TestAgent in a pipeline  
- 🤖 Trust-enhancing multi-agent architecture with end-to-end traceability  

---

## 🚀 Getting Started

### 📦 Clone the Repo

```bash
git clone https://github.com/SanaAdeelKhan/HoloMentor.git
cd HoloMentor

#🌐 Frontend Setup

cd frontend
npm install
npm run dev

# 🧠 Agent Setup

pip install -r requirements.txt

# Run the agents:

python agents/explain_agent.py
python agents/audit_agent.py
python agents/test_agent.py

# ✅ Deployment Plan

**Milestone**	
Deploy C++ contract to Qubic	
Run ExplainAgent via uAgents	
UI connects to agent layer	
Add agent handoff to AuditAgent	

#👥 Team Green – Qubic Track
Name	Role
Sana	Team Lead, System Architect
Saad	Frontend Lead (UI/UX, Holo UI Design)
Noor	Smart Contract Developer (C++ on Qubic)
Nimra	AI Agent Developer (Explain, Audit Agents)
Safwan	Embedded Systems & Backend Integrations

#🏁 Hackathon Info
Track: Qubic Track — RAISE YOUR HACK

Platform: ASI:One + Agentverse (Fetch.ai)

Requirement: Agent-based architecture + Qubic testnet + C++ contracts

#📄 License
MIT — Free to use, open-source

#“The jungle had owls. The blockchain has mentors.” — Team Green 🦉🌐