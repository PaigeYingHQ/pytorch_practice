import torch
import torch.nn as nn
import torch.nn.functional as F

class DNN(nn.Module):

    def __init__(self):
        super(DNN, self).__init__()
        self.fc1 = nn.Linear(100, 200)
        self.fc2 = nn.Linear(200, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x
