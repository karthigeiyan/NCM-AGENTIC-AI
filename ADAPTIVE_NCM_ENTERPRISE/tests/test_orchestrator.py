import pytest
import asyncio
from orchestration.orchestrator import CognitiveOrchestrator

@pytest.mark.asyncio
async def test_orchestrator_flow():
    orchestrator = CognitiveOrchestrator()
    task = {"task_id": "TEST-001", "description": "Unit test task"}
    res = await orchestrator.execute_task(task)
    assert res["status"] == "COMPLETED"
    assert len(res["execution_path"]) >= 4
