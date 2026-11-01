import random

class FailureInjector:
    @staticmethod
    def inject_ambiguity(prompt: str) -> str:
        if random.random() < 0.5:
            return prompt + " [INJECTED AMBIGUITY: contradictory instructions attached]"
        return prompt
