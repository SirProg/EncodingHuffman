from collections import defaultdict
from PIL import Image
from bitarray import bitarray
from ..queue.HuffmanTree import *

def compress_image(image: Image):
    width, height = image.size
    pixels = list(image.getdata())
    freq_dict = defaultdict(int)

    for pixel in pixels:
        freq_dict[pixels] += 1
    
    root = create_huffman_tree(freq_dict)
    huffman_codes = create_huffman_code(root)

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
    
