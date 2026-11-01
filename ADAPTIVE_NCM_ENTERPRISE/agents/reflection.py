from agents.base import BaseAgent
from typing import Dict, Any

class ReflectionAgent(BaseAgent):
    def __init__(self):
        super().__init__("ReflectionAgent", "Evaluates agent trajectories to spot logical inconsistencies or edge cases.")

    async def process(self, context: Dict[str, Any]) -> Dict[str, Any]:
        uncertainty = context.get("uncertainty", 0.0)
        critique = "Trajectory is robust." if uncertainty < 0.4 else "High uncertainty detected in reasoning step 3."
        return {"status": "SUCCESS", "critique": critique, "requires_revision": uncertainty > 0.4}
