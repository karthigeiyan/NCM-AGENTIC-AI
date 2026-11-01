class ResourceAllocator:
    """Dynamically allocates computing compute budget (token count, reasoning iterations, latency)."""
    @staticmethod
    def allocate(uncertainty: float) -> dict:
        if uncertainty > 0.6:
            return {"max_iterations": 5, "temperature": 0.2, "enable_reflection": True, "timeout": 30}
        elif uncertainty > 0.3:
            return {"max_iterations": 3, "temperature": 0.4, "enable_reflection": False, "timeout": 15}
        else:
            return {"max_iterations": 1, "temperature": 0.7, "enable_reflection": False, "timeout": 5}
