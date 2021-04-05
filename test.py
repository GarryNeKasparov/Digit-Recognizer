from model import Model
from data import test_loader
import torch
from train import criterion

model = Model()
model.cuda()


def test(model):
  model.eval()
  total_val_loss = 0
  total = 0
  for itr, (image, label) in enumerate(test_loader):
      image = image.cuda()
      label = label.cuda()
      pred = model(image)
      loss = criterion(pred, label)
      total_val_loss += loss.item()

      pred = torch.nn.functional.softmax(pred, dim=1)
      for i, p in enumerate(pred):
          if label[i] == torch.max(p.data, 0)[1]:
              total = total + 1

  accuracy = total / len(test_loader.dataset)

  total_val_loss = total_val_loss / (itr + 1)
  print('Total loss : {:.6f}\t Accuracy: {:.4f}%'.format(total_val_loss, accuracy * 100))

test(model)