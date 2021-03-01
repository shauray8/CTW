import torch
from torchvision import transforms, datasets, models
from torchvision.utils import save_image
from model import Encoder, Decoder

input_nc = 1
output_nc = 1
enc = Encoder(input_nc, output_nc)
dec = Decoder(input_nc, output_nc)
enc.load_state_dict(torch.load("pretrained/enc.pth"))
dec.load_state_dict(torch.load("pretrained/dec.pth"))

enc.eval()
dec.eval()

transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5],
                             std=[0.5])
])

dataset = datasets.MNIST(root='./data',transform=transform, download=True, train=False)
dataset_loader = torch.utils.data.DataLoader(dataset,
                                             batch_size=64, shuffle=True,)

for i,(image, _) in enumerate(dataset_loader):
    encoded = enc(image)
    decoded = dec(encoded)
    encoded = encoded.view(64,1,4,8)
    save_image(image, "output/A_orig.png")
    save_image(encoded, "output/A_encoded.png")
    save_image(decoded, "output/A_decoded.png")
    break
    

