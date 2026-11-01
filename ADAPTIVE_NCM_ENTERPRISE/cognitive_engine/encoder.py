import torch
import torch.nn as nn
import numpy as np

class ContextEncoder(nn.Module):
    """Encodes state, context, and query representations into unified latent embeddings."""
    def __init__(self, input_dim=128, hidden_dim=256, latent_dim=64):
        super(ContextEncoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Dropout(p=0.1),
            nn.Linear(hidden_dim, latent_dim),
            nn.LayerNorm(latent_dim)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.encoder(x)

    def encode_text_dummy(self, text: str) -> np.ndarray:
        hash_val = hash(text) % 10000 / 10000.0
        vec = np.ones(128, dtype=np.float32) * hash_val
        return vec
