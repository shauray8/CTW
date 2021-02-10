#enwik4 : 100326 bytes
#Huffman Coding : 53967 bytes

import os
import sys
import collections
from queue import PriorityQueue
import pickle

class Node(object):
    ''' This class represents a node in the binary tree '''
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def __lt__(self, other):
        ''' Sorting criterion for inserting to priority queue '''
        return (self.freq < other.freq)

    def __str__(self):
        return '({}: {})'.format(self.char, self.freq)

with open(sys.argv[1],'r') as f:
    data = f.read()

freq = collections.Counter(data)

q = PriorityQueue()


for k,v in freq.items():
    n = Node(k, v)
    q.put((n.freq, n))

while q.qsize() > 1:
    left = q.get()[1]
    right = q.get()[1]
    new_node = Node('',left.freq + right.freq, left, right)
    q.put((new_node.freq, new_node))

root = q.get()[1]
print(root)


code = []
codes = {}
def assign(root, codes, code):
    if root.is_leaf():
        key = root.char
        codes[key] = ''.join(code)
        return

    if root.left:
        code.append('0')
        assign(root.left, codes, code)
        code.pop()

    if root.right:
        code.append('1')
        assign(root.right, codes, code)
        code.pop()

assign(root, codes, code)

compressed_data = []
for d in data:
    compressed_data.append(codes[d])

encoded = "".join(compressed_data)

extra = 8 - len(encoded) % 8
padded_encoded = '0' * extra + encoded
extra_zero = '{0:08b}'.format(extra)
padded_encoded = extra_zero + padded_encoded

b = bytearray()
length = len(padded_encoded)
for i in range(0, length, 8):
    byte = padded_encoded[i:i+8]
    b.append(int(byte,2))
print(len(b))

with open(sys.argv[1]+" compressed","wb") as out:
    pickle.dump((freq, b), out)

