# src/agents/shared_models.py

from uagents import Model

class ContractCode(Model):
    code: str

class Explanation(Model):
    summary: str

class AuditReport(Model):
    report: str
