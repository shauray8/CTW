# Context Tree Weighting
Investigating and exploring context-tree weighting

*Explaining CTW is a little tough*  
[project presentation](https://docs.google.com/presentation/d/1tnYMo08lWsNUUokcjIjjhkn97guwpLnifMzcUaRDQMo/edit?usp=sharing)
  
btw here's the code for [CTW](/CTW) ! 

## Huffman Coding just to create a baseline

### An example of how huffman coding works 

Characters | ASCII | Frequency | HUFFMAN | bits
-----------|-------|-----------|---------|-----
'A' | 065 | 1 | 00 | 01000001 
'g' | 103 | 1 | 01 | 01100111 
'i' | 108 | 1 | 11 | 01101100 
'o' | 111 | 1 | 10 | 01101111 

### This is an image illustrating how huffman coding works (source: WIKI)
![huffman coding](/img/huffman.png)

And here's the code for Huffman Coding [compressor and decompressor](/huffman)

### Results for the compression are 
algorithms | size(bytes)
-----------|-------------
ORIGINAL | 100326
GZIP | 26780
HUFFMAN | 53967
7ZIP | 23806

## AutoEncoder (for image compression)
*Assume that there is an explaination for autoencoder here*

### results for compression with AutoEncoder
*assume that there is a table of results here*
  
here is the code for [AutoEncoder](/autoencoder) and the [PreTrained Model](/autoencoder/pretrained)

### Applications
---
[Using compression tool to study mammalian evolution and construct the phylogeny of the SARS virus can be found here](https://docs.google.com/presentation/d/1LUbo-6mLpYTwcELOLlRR4ohku9j2kCiQj_2sYPh0uWA/edit#slide=id.p).

### BARF this thing compresses your data to less than 1 byte (i don't know how)
---
The Barf Thingy can be found [here](http://mattmahoney.net/dc/barf.html).

### References
---
* [An Autoencoder-based Learned Image Compressor: Description of Challenge Proposal by NCTU](https://arxiv.org/pdf/1902.07385.pdf)
* [Text Encryption with Huffman Compression](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.258.8140&rep=rep1&type=pdf)
* [The context-tree weighting method: basic properties](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.14.352&rep=rep1&type=pdf)
* [Context Tree Switching](https://arxiv.org/pdf/1111.3182.pdf)

### TODO
* Hutter prize
* improve the compression 
* manupulate the huffman thing for the project !


### Huffman TODO
* read the compression part
* decompress does not work maybe 
* make it visual with some python lib

