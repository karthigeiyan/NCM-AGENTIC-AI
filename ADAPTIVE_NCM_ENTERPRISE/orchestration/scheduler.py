class TaskScheduler:
    def __init__(self):
        self.queue = []

    def schedule(self, task: dict, priority: int = 1):
        self.queue.append({"task": task, "priority": priority})
        self.queue.sort(key=lambda x: x["priority"], reverse=True)
