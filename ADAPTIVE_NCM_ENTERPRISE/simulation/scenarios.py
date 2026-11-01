class ScenarioGenerator:
    @staticmethod
    def get_benchmark_scenarios():
        return [
            {"name": "High Uncertainty Domain Shift", "complexity": "EXTREME"},
            {"name": "Malformed Input Recovery", "complexity": "HIGH"},
            {"name": "Nominal Regulatory Process", "complexity": "LOW"}
        ]
