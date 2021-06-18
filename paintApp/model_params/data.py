from torchvision.datasets import MNIST
from torchvision import datasets, transforms
import torch

batch_size = 32
random_seed = 1

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5,), (0.5,)),])

train_data = MNIST(root = './', train=True, download=True, transform=transform)
val_data = MNIST(root = './', train=False, download=True, transform=transform)

train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(val_data, batch_size=batch_size, shuffle=True)