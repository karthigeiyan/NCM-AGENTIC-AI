import asyncio
import logging
from orchestration.orchestrator import CognitiveOrchestrator
from cognitive_engine.state_manager import SystemState

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("NCM-Main")

async def run_enterprise_demo():
    logger.info("Initializing Uncertainty-Guided Adaptive NCM Enterprise System...")
    
    orchestrator = CognitiveOrchestrator()
    
    complex_enterprise_task = {
        "task_id": "TASK-ENT-9021",
        "description": "Analyze financial compliance risk for cross-border transaction anomalies and auto-generate mitigation policies.",
        "context": {"priority": "HIGH", "domain": "FINANCIAL_COMPLIANCE", "latency_budget_ms": 1500}
    }
    
    logger.info(f"Submitting Task: {complex_enterprise_task['task_id']}")
    result = await orchestrator.execute_task(complex_enterprise_task)
    
    logger.info("================ Task Execution Summary ================")
    logger.info(f"Task Status: {result['status']}")
    logger.info(f"Final Output: {result['output']}")
    logger.info(f"Uncertainty Metric: {result['uncertainty']:.4f}")
    logger.info(f"Cognitive Path Taken: {result['execution_path']}")
    logger.info(f"Recovery Actions Executed: {result.get('recoveries_triggered', 0)}")
    logger.info("========================================================")

if __name__ == "__main__":
    asyncio.run(run_enterprise_demo())
