class ConfidenceCalculator:
    """Converts uncertainty scores and state features into calibrated confidence scores."""
    @staticmethod
    def compute_confidence(uncertainty: float, historical_accuracy: float = 0.95) -> float:
        raw_confidence = (1.0 - uncertainty) * historical_accuracy
        return max(0.01, min(0.99, float(raw_confidence)))
