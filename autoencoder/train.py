import torch
import torch.nn as nn
from tqdm import trange
import torchvision
from torchvision import transforms, datasets, models
import torch.optim as optim
from model import Encoder, Decoder
import matplotlib.pyplot as plt

EPOCH = 50
input_nc = 1
output_nc = 1
batch_size= 64

transform = transforms.Compose([
        #transforms.RandomSizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5],
                             std=[0.5])
])

dataset = datasets.MNIST(root='./data',transform=transform, download=True)
dataset_loader = torch.utils.data.DataLoader(dataset,
                                             batch_size=batch_size, shuffle=True,)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

enc = Encoder(input_nc, output_nc).to(device)
dec = Decoder(input_nc, output_nc).to(device)

enc.load_state_dict(torch.load("pretrained/enc.pth"))
dec.load_state_dict(torch.load("pretrained/dec.pth"))

enc_optimize = optim.Adam(enc.parameters())
dec_optimize = optim.Adam(dec.parameters())

loss_functionE = nn.MSELoss()
loss_functionD = nn.MSELoss()

losses = []
def train():
    for epoch in (i := trange(0, EPOCH)):
        for id, (images,_) in enumerate(dataset_loader):
            x = images.to(device)
            ##### training the Encoder #####
            
            E2E_output = enc(x)
            #D2E_output = dec(E2E_output)
            #loss_E = loss_functionE(D2E_output,x)
            #enc_optimize.zero_grad()
            #loss_E.backward(retain_graph=True)
            #enc_optimize.step()

            ##### training the Decoder #####

            D2D_output = dec(E2E_output)
            loss_D = loss_functionD(D2D_output, x)
            dec_optimize.zero_grad()
            loss_D.backward()
            dec_optimize.step()
            i.set_description(f'epoch [{epoch + 1}/{EPOCH}], loss:{loss_D.item():.4f}')

        torch.save(dec.state_dict(), 'pretrained/dec.pth')
        torch.save(enc.state_dict(), 'pretrained/enc.pth')

train()
