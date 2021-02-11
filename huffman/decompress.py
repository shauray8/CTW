import os
import pickle
from queue import PriorityQueue


with open("compressed_file",'rb') as f:
    data = pickle.load(f)
    
freq, bytes = data

def something(nodes):
    length = len(nodes)
    if length == 1:
        return nodes[0]

    index = split(nodes)
    return index

def split(nodes):
    length = len(nodes)
    total = sum([n.freq for n in nodes])
    return total


#l = something(freq)
#print(l)
