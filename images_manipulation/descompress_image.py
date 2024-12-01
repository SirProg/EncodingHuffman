from collections import defaultdict
from PIL import Image
from bitarray import bitarray
from ..queue.HuffmanTree import *

def descompress_image(compress_data: dict):
    width = compress_data['width']
    height = compress_data['height']
    huffman_codes = compress_data['huffman_codes']
    encode_data = compress_data['encode_data']

    reverse_code = {code: char for char, code in huffman_codes.items()}
    decoded_pixels = []
    current_code = ''

    for bit in encode_data:
        current_code += '1' if bit else '0'
        if current_code in reverse_code:
            decoded_pixels.append(reverse_code[current_code])
            current_code = ""
    image = Image.new('RGB', (width, height))
    image.putdata(decoded_pixels)
    return image

