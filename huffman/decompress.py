import os
import pickle
from queue import PriorityQueue
from compress import Node
from operator import attrgetter

with open("compressed_file",'rb') as f:
    data = pickle.load(f)
    
frequency, bytes = data


def build_tree(nodes):
    length = len(nodes)
    if length == 1:
        return nodes[0]

    index = split(nodes)
    left = build_tree(nodes[0:index])
    right = build_tree(nodes[index:])
    return Node('', left.freq + right.freq, left, right)

def create_nodes_from_frequencies(frequencies):
    nodes = []
    for k, v in frequencies.items():
        nodes.append(Node(k, v))
    nodes.sort(key=attrgetter('freq', 'char'), reverse=True)
    return nodes

nodes = create_nodes_from_frequencies(frequency)

def split(nodes):
    length = len(nodes)
    total = sum([n.freq for n in nodes])
    second_half_total = 0
    index = length

    while (index >= 0) and (second_half_total < (total - second_half_total)):
        index -= 1
        second_half_total += nodes[index].freq

    diff1 = second_half_total - (total - second_half_total)
    diff2 = abs(diff1 - 2 * nodes[index].freq)
    if diff2 < diff1:
        index += 1
    return index

def convert_bytes_to_bit_str(byte_array):
    bin_format = '{0:08b}'
    bit_data = []
    for b in byte_array:
        data = bin_format.format(b)
        bit_data.append(data)
    return ''.join(bit_data)

def remove_padding(padded_encoded_str):
    extra_zero_info = padded_encoded_str[:8]
    extra_zero = int(extra_zero_info, 2)
    padded_encoded_str = padded_encoded_str[8:]
    encoded_str = padded_encoded_str[extra_zero:]
    return encoded_str

def get_decoded_str(root, encoded_str):
    decoded_data = []
    current = root
    for code in encoded_str:
        if code == "0":
            current = current.left
        else:
            current = current.right

        if current.is_leaf():
            char = current.char
            decoded_data.append(char)
            current = root
    return ''.join(decoded_data)

root = build_tree(nodes)
bit_str = convert_bytes_to_bit_str(bytes)
encoded_str = remove_padding(bit_str)
decoded_str = get_decoded_str(root, encoded_str)

with open("output_file", 'w') as out:
    out.write(decoded_str)


