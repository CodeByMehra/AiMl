import torch
import torch.nn as nn

class DQN(nn.Module):
    # input dim, output dim, hidden dim
    def __init__(self, state_dim=12, action_dim=2, hidden_dim=256):
        super(DQN, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim)
        )

    def forward(self, x):
        return self.model(x)
    

#     Explanation
# state_dim=12 → The Flappy Bird environment provides 12 state features as input.
# action_dim=2 → Two possible actions:
# 0 = Do nothing
# 1 = Flap
# hidden_dim=256 → Number of neurons in the hidden layer.
# ReLU() → Activation function that helps the neural network learn complex patterns.
# forward() → Defines how input data passes through the network.
# Architecture
# Input Layer (12)
#        │
#        ▼
# Linear (12 → 256)
#        │
#        ▼
# ReLU
#        │
#        ▼
# Linear (256 → 2)
#        │
#        ▼
# Q-values for actions