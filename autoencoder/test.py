import torch
from model import Encode, Decode

input_nc = 1
output_nc = 1
enc = Encoder(input_nc, output_nc)
enc.load_state_dict(torch.load(pretrained/encoder))

enc.eval()

