import torch
import numpy

import torch.nn as nn
from torchvision import transforms, datasets
import torch.optim as optim
import matplotlib.pyplot as plt

transform = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5],
                             std=[0.5])
])

batch_size=32

dataset = datasets.MNIST(root='./data',transform=transform, download=True)
dataset_loader = torch.utils.data.DataLoader(dataset,
                                             batch_size=batch_size, shuffle=True,)

class encoder(nn.Module):
    def __init__(self, input, channels):
        super(encoder, self).__init__()
        self.conv1 = nn.Conv2d(input,channels, kernel_size=5, stride=2)
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
input = 1
channels = 64
encoder = encoder(input, channels)
decoder = decoder()
print(encoder)
print(decoder)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def train():
    for epoch in range(EPOCH):
        for id, (images,_) in enumerate(dataset_loader):
            #images = images.to(device)
            plt.imshow(images[0].view(28,28), cmap="gray")
            plt.show()
            print("done bitches")
            break 
        break

train()
# the basic structure for the autoencoder 
