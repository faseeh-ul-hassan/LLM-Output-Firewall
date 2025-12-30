class LLMOutputFirewall:
    def __init__(self, judge):
        self.judge = judge

    def enforce(self, ai_output: str) -> dict:
        decision = self.judge.evaluate(ai_output)

        verdict = decision.get("verdict", "BLOCK")

        if verdict == "ALLOW":
            return {
                "status": "ALLOWED",
                "final_output": ai_output,
                "security_decision": decision
            }

        if verdict == "REDACT":
            redacted_output = ai_output
            for segment in decision.get("sensitive_segments", []):
                redacted_output = redacted_output.replace(segment, "[REDACTED]")

            return {
                "status": "REDACTED",
                "final_output": redacted_output,
                "security_decision": decision
            }

        return {
            "status": "BLOCKED",
            "final_output": None,
            "security_decision": decision
        }
