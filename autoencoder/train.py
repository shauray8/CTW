import torch
import torchvision
from torchvision import transforms, datasets, models
from model import encoder, decoder

transform = transforms.Compose([
        transforms.RandomSizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5,0.5,0.5],
                             std=[0.5, 0.5, 0.5])
])

dataset = datasets.MNIST(root='./data',transform=transform, download=True)
dataset_loader = torch.utils.data.DataLoader(dataset,
                                             batch_size=batch_size, shuffle=True,)

EPOCH = 50
input_nc = 3
batch_size= 64

enc = encoder()
dec = decoder()

optimizer = optim.Adam(net.parameters())
loss_function = nn.MSELoss()

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
