from typing import Dict, Any, List

class SystemState:
    """Tracks dynamic system cognitive state, active node contexts, and agent history."""
    def __init__(self, task_id: str):
        self.task_id = task_id
        self.step_counter = 0
        self.history: List[Dict[str, Any]] = []
        self.current_uncertainty = 0.5
        self.current_confidence = 0.5
        self.blackboard: Dict[str, Any] = {}

    def update_state(self, step_name: str, result: Dict[str, Any], uncertainty: float):
        self.step_counter += 1
        self.current_uncertainty = uncertainty
        self.history.append({
            "step": self.step_counter,
            "action": step_name,
            "uncertainty": uncertainty,
            "result_summary": str(result)[:100]
        })
        self.blackboard[step_name] = result
