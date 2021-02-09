#enwik4 : 100326 bits

import os
import collections

with open("../enwik4",'r') as f:
    data = f.read()

freq = collections.Counter(data)
print(freq)
print(len(freq))
