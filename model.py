import torch.nn as nn


class Model(nn.Module):
  def __init__(self):
    super().__init__()
    self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)
    self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
    self.maxPolling = nn.MaxPool2d(kernel_size=2, stride=2)
    self.linear1 = nn.Linear(in_features=64 * 7 * 7, out_features=128)
    self.linear2 = nn.Linear(in_features=128, out_features=10)
    self.relu = nn.ReLU()
    self.dropout = nn.Dropout()

  def forward(self, x):
    x = self.conv1(x)
    x = self.relu(x)
    x = self.maxPolling(x)
    x = self.conv2(x)
    x = self.relu(x)
    x = self.maxPolling(x)
    x = x.reshape(x.size(0), -1)
    x = self.linear1(x)
    x = self.relu(x)
    x = self.dropout(x)

    pred = self.linear2(x)

    return pred
        
