import torch.nn as nn
import torch 

from model import Model
from data import train_loader

model = Model()
model.cuda()

epochs = 10
learning_rate = 1e-2
log_interval = 10
momentum = 0.5

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate, momentum=momentum)

def train(model):
  for epoch in range(epochs):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
      data = data.cuda()
      target = target.cuda()

      optimizer.zero_grad()

      outputs = model(data)

      loss = criterion(outputs, target)

      loss.backward()
      optimizer.step()
      if (batch_idx % log_interval == 0):
        print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
        epoch, batch_idx * len(data), len(train_loader.dataset),
        100. * batch_idx / len(train_loader), loss.item()))

train(model)

torch.save(model.state_dict(), 'model.pth')