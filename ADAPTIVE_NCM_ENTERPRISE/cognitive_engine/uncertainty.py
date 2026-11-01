import torch
import numpy as np
from typing import Dict, Tuple

class UncertaintyEstimator:
    """Calculates epistemic and aleatoric uncertainty via MC Dropout and Ensembling."""
    def __init__(self, num_samples: int = 10):
        self.num_samples = num_samples

    def estimate_uncertainty(self, logits_samples: np.ndarray) -> Dict[str, float]:
        probs = 1.0 / (1.0 + np.exp(-logits_samples))
        mean_probs = np.mean(probs, axis=0)
        total_variance = np.var(probs, axis=0)
        epistemic = float(np.mean(total_variance))
        aleatoric = float(np.mean(mean_probs * (1.0 - mean_probs)))
        normalized_epistemic = float(np.clip(epistemic * 4.0, 0.0, 1.0))
        return {
            "epistemic_uncertainty": normalized_epistemic,
            "aleatoric_uncertainty": float(aleatoric),
            "total_uncertainty": float(normalized_epistemic + 0.5 * aleatoric)
        }
