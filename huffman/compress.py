#enwik4 : 100326 bits

import os
import collections
from queue import PriorityQueue

with open("../enwik4",'r') as f:
    data = f.read()

freq = collections.Counter(data)

q = PriorityQueue()

class Node(object):
    ''' This class represents a node in the binary tree '''
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        ''' Sorting criterion for inserting to priority queue '''
        return (self.freq < other.freq)

    def __str__(self):
        return f'({self.char}: {self.freq})'

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



