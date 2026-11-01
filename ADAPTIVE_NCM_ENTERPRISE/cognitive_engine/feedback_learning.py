class FeedbackLearner:
    """Updates adaptive policy weights based on execution outcome rewards."""
    def __init__(self):
        self.learning_rate = 0.05

    def reward_feedback(self, task_success: bool, elapsed_time: float, uncertainty_reduction: float) -> float:
        base_reward = 1.0 if task_success else -1.5
        efficiency_bonus = max(0.0, 2.0 - elapsed_time)
        return base_reward + (0.5 * uncertainty_reduction) + (0.1 * efficiency_bonus)
