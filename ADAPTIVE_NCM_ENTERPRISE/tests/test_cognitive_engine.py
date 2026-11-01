import unittest
import numpy as np
from cognitive_engine.uncertainty import UncertaintyEstimator
from cognitive_engine.confidence import ConfidenceCalculator

class TestCognitiveEngine(unittest.TestCase):
    def test_uncertainty_estimation(self):
        estimator = UncertaintyEstimator(num_samples=5)
        samples = np.random.randn(5, 3)
        res = estimator.estimate_uncertainty(samples)
        self.assertIn("epistemic_uncertainty", res)
        self.assertTrue(0.0 <= res["epistemic_uncertainty"] <= 1.0)

    def test_confidence_calculation(self):
        conf = ConfidenceCalculator.compute_confidence(0.2, 0.95)
        self.assertGreater(conf, 0.7)

if __name__ == '__main__':
    unittest.main()
