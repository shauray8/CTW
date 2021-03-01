import torch
import numpy

import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

class Residual_block(nn.Module):
    def __init__(self, input_nc):
        super(Residual_block, self).__init__()

        model = [nn.Conv2d(input_nc, input_nc, kernel_size=3, stride=1, padding=1, bias=False),
                nn.InstanceNorm2d(input_nc, affine=True, track_running_stats=True),
                nn.ReLU(inplace=False),
                nn.Conv2d(input_nc, input_nc, kernel_size =3, stride=1, padding=1, bias=False),
                nn.InstanceNorm2d(input_nc, affine=True, track_running_stats=True)]

        self.model = nn.Sequential(*model)

    def forward(self, x):
        return self.model(x)

class Encoder(nn.Module):
    def __init__(self, input_nc, output_nc, resblocks=6):
        super(Encoder, self).__init__()
        
        model = [nn.Conv2d(input_nc, 64, kernel_size=3, stride=3, padding=3),
                nn.ReLU(inplace=False),
                nn.MaxPool2d(2, stride=2),]
        
        in_features = 64
        out_features = in_features*2

        for i in range(resblocks):
            model += [Residual_block(in_features)]

        model += [nn.Conv2d(in_features, 8, kernel_size=3, stride=2, padding=1),
                nn.ReLU(inplace=False),
                nn.MaxPool2d(2, stride=1)]
        
        self.model = nn.Sequential(*model)

    def forward(self, x):
        torch.autograd.set_detect_anomaly(True)
        return self.model(x)


class Decoder(nn.Module):
    def __init__(self, input_nc, output_nc, resblocks=6):
        super(Decoder, self).__init__()

        in_features = 64
        out_features = in_features*2
        model = [nn.ConvTranspose2d(8, in_features, kernel_size=3, stride=2 ),
                nn.ReLU(inplace=False)]

        for _ in range(resblocks):
            model += [Residual_block(in_features)]

        model += [nn.ConvTranspose2d(in_features, 8, kernel_size=5, stride=3, padding=1),
                nn.ReLU(inplace=False),
                nn.ConvTranspose2d(8, output_nc, kernel_size=2, stride=2, padding=1),
                nn.Tanh()]

        self.model = nn.Sequential(*model)

    def forward(self, x):
        torch.autograd.set_detect_anomaly(True)
        return self.model(x)


if __name__ == "__main__":
    D = Decoder(3,3)
    E = Encoder(3,3)
    print(D,E)

