from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import re
import base64
from neural_model import get_model
from io import BytesIO
from PIL import Image, ImageOps
import numpy as np
import torch.nn.functional as F
from torchvision import transforms


@csrf_exempt
def index(request):
    if (request.method == "GET"):
        return render(request,'index.html')


    if (request.method == "POST"):
        #print(type(request.POST['data']))
        pass
        
        image_data = request.POST['data']
        image_data = re.sub("^data:image/png;base64,", "", image_data)
        image_data = base64.b64decode(image_data)
        image_data = BytesIO(image_data)
        im = Image.open(image_data)
        print(type(im))
        
        return


transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5,), (0.5,)),])
def predict(img):
    model = get_model()
    img = ImageOps.invert(img)
    img = img.resize((28, 28), Image.BICUBIC)

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