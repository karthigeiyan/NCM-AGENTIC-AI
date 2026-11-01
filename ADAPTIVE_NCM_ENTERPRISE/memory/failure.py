class FailureMemory:
    def __init__(self):
        self.failures = []

    def log_failure(self, task_id: str, error_context: dict):
        self.failures.append({"task_id": task_id, "error": error_context})
