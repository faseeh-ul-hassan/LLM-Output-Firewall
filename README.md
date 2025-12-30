# LLM Output Firewall

An LLM-based post-generation security layer that enforces AI output safety
using a Model-as-Judge architecture.

## Why This Matters
Traditional rule-based filters fail against semantic attacks.
This firewall uses a second LLM to interpret and enforce security decisions.

## Features
- LLM-based security judgment
- Allow / Redact / Block enforcement
- Prompt & system leakage detection
- Sensitive data protection
- Model-agnostic architecture

## Architecture
User → Generator LLM → Output → Firewall LLM → Final Response

## Use Cases
- Prompt Injection Defense
- AI Agent Safety
- Output Compliance
- Red Team Validation
- Enterprise AI Guardrails

## Installation
```bash
pip install -r requirements.txt
