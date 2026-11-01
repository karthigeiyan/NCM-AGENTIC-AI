import numpy as np

class DynamicDatasetGenerator:
    def generate_synthetic_batch(self, batch_size: int = 32):
        X = np.random.randn(batch_size, 128)
        y = np.random.uniform(0, 1, size=(batch_size, 1))
        return X, y
