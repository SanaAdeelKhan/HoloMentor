from uagents import Agent

# Derive explain agent address
explain_agent = Agent(seed="explain-agent fixed seed phrase for holomentor")
print("Explain Agent Address:", explain_agent.address)

# Derive audit agent address
audit_agent = Agent(seed="audit-agent fixed seed phrase")
print("Audit Agent Address:", audit_agent.address)
