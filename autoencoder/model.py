import torch
import numpy

import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

class resnet(nn.Module):
    def __init__(self):
        super(resnet).__init__()
        pass
    def forward(self, x):
        pass

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

class decoder(nn.Module):
    def __init__():
        super(decoder, self).__init__()
        pass

    def forward(self, x):
        pass
