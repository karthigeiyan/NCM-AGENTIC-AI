class DynamicAgentRouter:
    def route(self, current_agent: str, uncertainty: float) -> str:
        if uncertainty > 0.5:
            return "VERIFICATION_AND_RECOVERY"
        return "NEXT_SEQUENTIAL_STEP"
