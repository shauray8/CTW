import torch
import numpy

import torch.nn as nn
from torchvision import transforms, datasets
import torch.optim as optim

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
        self.conv1 = nn.Conv2d(28*28,64, kernel_size=5, stride=2)
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
        self.conv1 = nn.Conv2d(64, 128, kernel_size=5, stride=2)
        self.act = nn.ReLU()
        pass


    def forward(self, x):
        x = self.conv1(x)
        x = self.act(x)
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
decoder = decoder()
print(encoder)
print(decoder)

def train():
    for epoch in range(EPOCH):
        for id, (images,_) in enumerate(dataset_loader):
            images = images.to('cuda')
            pass
        pass


# the basic structure for the autoencoder 
