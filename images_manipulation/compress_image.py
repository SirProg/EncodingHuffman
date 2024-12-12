from collections import defaultdict
from PIL import Image
from bitarray import bitarray
from Huffman_queue import HuffmanTree

def compress_image_func(image: Image):
    width, height = image.size
    pixels = list(image.getdata())
    freq_dict = defaultdict(int)

    for pixel in pixels:
        freq_dict[pixel] += 1
    
    root = HuffmanTree.create_huffman_tree(freq_dict)
    huffman_codes = HuffmanTree.create_huffman_code(root)

    encode_data = bitarray()
    for pixel in pixels:
        encode_data.extend(huffman_codes[pixel])

    compress_data = {
        'width' : width,
        'height' : height,
        'huffman_codes' : huffman_codes,
        'encode_data' : encode_data
    }

    return compress_data
    
