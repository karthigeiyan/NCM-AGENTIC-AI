class EnterpriseSimulationEnv:
    def reset(self):
        return {"system_load": 0.1, "network_latency_ms": 20}

    def step(self, action: str):
        return {"obs": "next_state", "reward": 1.0, "done": True}
