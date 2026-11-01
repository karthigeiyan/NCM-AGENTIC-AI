from typing import Dict, Any
from agents.planning import PlanningAgent
from agents.knowledge import KnowledgeAgent
from agents.reasoning import ReasoningAgent
from agents.verification import VerificationAgent
from agents.reflection import ReflectionAgent
from agents.recovery import RecoveryAgent
from cognitive_engine.encoder import ContextEncoder
from cognitive_engine.uncertainty import UncertaintyEstimator
from cognitive_engine.confidence import ConfidenceCalculator
from cognitive_engine.state_manager import SystemState
from cognitive_engine.adaptive_policy import AdaptivePolicy
import numpy as np

class CognitiveOrchestrator:
    def __init__(self):
        self.encoder = ContextEncoder()
        self.uncertainty_estimator = UncertaintyEstimator()
        self.adaptive_policy = AdaptivePolicy()
        
        self.planning_agent = PlanningAgent()
        self.knowledge_agent = KnowledgeAgent()
        self.reasoning_agent = ReasoningAgent()
        self.verification_agent = VerificationAgent()
        self.reflection_agent = ReflectionAgent()
        self.recovery_agent = RecoveryAgent()

    async def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        state = SystemState(task["task_id"])
        path = []
        recoveries_triggered = 0

        path.append("KnowledgeAgent")
        k_res = await self.knowledge_agent.process(task)
        state.update_state("knowledge", k_res, 0.2)

        path.append("PlanningAgent")
        p_res = await self.planning_agent.process(task)
        state.update_state("plan", p_res, 0.25)

        simulated_logits = np.random.normal(loc=0.8, scale=0.35, size=(10, 4))
        u_metrics = self.uncertainty_estimator.estimate_uncertainty(simulated_logits)
        epistemic_u = u_metrics["epistemic_uncertainty"]

        strategy = self.adaptive_policy.select_routing_strategy(np.zeros(128), epistemic_u)

        path.append("ReasoningAgent")
        r_res = await self.reasoning_agent.process({"plan": p_res["plan"]})
        state.update_state("reasoning", r_res, epistemic_u)

        path.append("VerificationAgent")
        v_res = await self.verification_agent.process({"hypothesis": r_res["hypothesis"]})

        if epistemic_u > 0.4 or not v_res["verified"]:
            path.append("ReflectionAgent")
            ref_res = await self.reflection_agent.process({"uncertainty": epistemic_u})
            if ref_res.get("requires_revision"):
                path.append("RecoveryAgent")
                rec_res = await self.recovery_agent.process({"error": "High epistemic risk"})
                recoveries_triggered += 1
                epistemic_u = max(0.05, epistemic_u - rec_res.get("uncertainty_reduction", 0.2))

        confidence = ConfidenceCalculator.compute_confidence(epistemic_u)

        return {
            "status": "COMPLETED",
            "task_id": task["task_id"],
            "output": r_res["hypothesis"],
            "uncertainty": epistemic_u,
            "confidence": confidence,
            "execution_path": path,
            "recoveries_triggered": recoveries_triggered,
            "strategy_used": strategy
        }
