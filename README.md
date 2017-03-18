# Huffman Encoding Algorithm
## Introduction
This program was originally completed as an assignment for CSCI 3104 Algorithms at the University of Colorado Boulder.  The assignment was to use the Huffman Encoding Algorithm to encode a poem by Robert Frost.

## Background
Huffman encoding is an algorithm for generating an optimal prefix free code for data compression.

## Notes
There is a unresolved bug in the code that prevents it from generating an optimal encoding.  The minimum encoding possible for this particular poem by Robert Frost is 3175 bits.  My algorithm is generating an encoding with 3224 bits.  

If my school and work workload permits, I will revisit this when I have time.

## Requirements
```
Python 2.7.10 
```
## Running
In the terminal, run huffman.py
```
~ $ python huffman.py
```
The binary encoding will appear below in the terminal, followed by the codebook for decoding the message.
