import torch
import numpy

import torch.nn as nn
from torchvision import transforms, datasets, models
import torch.optim as optim
import matplotlib.pyplot as plt


transform = transforms.Compose([
        transforms.RandomSizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5,0.5,0.5],
                             std=[0.5, 0.5, 0.5])
])
batch_size=32

dataset = datasets.MNIST(root='./data',transform=transform, download=True)
dataset_loader = torch.utils.data.DataLoader(dataset,
                                             batch_size=batch_size, shuffle=True,)

#dataset = datasets.ImageFolder(root='../../data/Cat',transform=transform)
#dataset_loader = torch.utils.data.DataLoader(dataset,
#                                             batch_size=batch_size, shuffle=True,)
#resnet = models.segmentation.fcn_resnet101(pretrained=False, progress=True, num_classes=21)

class autoencoder_compression(nn.Module):
    def __init__(self, input, channels):
        super(autoencoder_compression, self).__init__()
        
        #ENCODER

        resnet_E = models.resnet18(pretrained=True)
        self.conv1_E = nn.Conv2d(input,channels, kernel_size=5, stride=2)
        self.act_E = nn.ReLU()
        modules_E = list(resnet_E.children())[:-1]
        self.resnet_E = nn.Sequential(*modules_E)
        self.conv2_E = nn.Conv2d(resnet_E.fc.in_features,16, kernel_size=5, stride=2)

        #DECODER

        self.conv1_D = nn.Conv2d(16, 128, kernel_size=5, stride=2)
        self.act_D = nn.ReLU()
        resnet_D = models.resnet18(pretrained=True)
        modules_D = list(resnet_D.children())[:-1]
        self.resnet_D = nn.Sequential(*modules_D)
        self.conv2_D = nn.Conv2d(resnet_D.fc.in_features, 64, kernel_size=5, stride=2)
        self.act2_D = nn.ReLU()
        self.conv3_D = nn.Conv2d(64, 1, kernel_size=5, stride=2)
        

    def decode(self, x):
        x = self.conv1_D(x)
        x = self.act_D(x)
        for i in range(6):
            x = self.resnet_D(x)
        x = self.conv2_D(x)
        x = self.act2_D(x)
        x = self.conv3_D(x)
        x = resnet_D(x)
        return x
        
    def encode(self, x):
        for i in range(1):
            x = self.conv1_E(x)
            x = self.act_E(x)
        for i in range(6):
            x = self.resnet_E(x)
        x = self.conv2_E(x)
        x = self.resnet_E(x)
        return x

    def forward(self, z):
        z = self.encode(z)
        z = self.decode(z)
        return z


class resnet(nn.Module):
    def __init__(self):
        super(resnet).__init__()
        pass
    def forward(self, x):
        pass

    #because i think that i will need one lets see
    #should i just use a pretrainied model or should i train this sucker

EPOCH = 50
input = 1
channels = 64

net = autoencoder_compression(input, channels)

optimizer = optim.Adam(net.parameters())
loss_function = nn.MSELoss()

print(net)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def train():
    for epoch in (i := range(EPOCH)):
        for id, (images,_) in enumerate(dataset_loader):
            x = images.to(device)
            x_output = net(x)
            loss = loss_function(x_output,x.data)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            break
        i.set_description(f'epoch [{epoch + 1}/{epochs}], loss:{loss.item():.4f}')
        break

train()
# the basic structure for the autoencoder 
