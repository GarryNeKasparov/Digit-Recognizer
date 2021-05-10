import PIL
import numpy as np
import torch.nn.functional as F
from torchvision import transforms
from neural_model import get_model
transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5,), (0.5,)),])

def predict(img):
    model = get_model()
    img = PIL.ImageOps.invert(img)
    img = img.resize((28, 28), PIL.Image.BICUBIC)

    img = transform(img)
    img = np.reshape(img, (1, 1, 28, 28))
    
    pred = model(img)
    res = F.softmax(pred, dim=1)
    l, m = 0, 0
    for label, p in enumerate(res.cpu().detach().numpy()[0]):
        if (p > m):
            m = float(p)
            l = label
        print(l)
