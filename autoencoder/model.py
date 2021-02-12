import torch
import math
import numpy
import torch.nn as nn
from torchvision import transforms, datasets

transform = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
])

batch_size=32

dataset = datasets.MNIST(root='./data',transform=transform, download=True)
dataset_loader = torch.utils.data.DataLoader(dataset,
                                             batch_size=batch_size, shuffle=True,)

class encoder(nn.Module):
    def __init__(self):
        super(encoder, self).__init__()
        self.conv1 = nn.Conv2d(1,64, kernel_size=5, stride=2)
        self.act = nn.ReLU()
        pass
    def forward(self, x):
        x = self.conv1(x)
        x = self.act(x)
        x = self.conv1(x)
        x = self.act(x)
        pass

class decoder(nn.Module):
    def __init__(self):
        super(decoder, self).__init__()
        pass


    def forward(self, x):
        pass

class resnet(nn.Module):
    def __init__(self):
        super(resnet).__init__()
        pass
    def forward(self, x):
        pass

    #because i think that i will need one lets see

EPOCH = 50
encoder = encoder()
print(encoder)
for epoch in range(EPOCH):
    pass


# the basic structure for the autoencoder 
