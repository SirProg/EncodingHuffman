from collections import defaultdict
from PIL import Image 

def descompress_image_func(compress_data: dict):
    #Extraccion de los datos comprimidos
    width = compress_data['width']
    height = compress_data['height']
    huffman_codes = compress_data['huffman_codes']
    encode_data = compress_data['encode_data']
    #Se crea un diccionario inverso donde las claves son los códigos de Huffman y los valores son los píxeles correspondientes
    reverse_code = {code: char for char, code in huffman_codes.items()}
    decoded_pixels = []
    current_code = ''

    #Se decodifican los datos codificados utilizando el diccionario inverso de códigos de Huffman
    for bit in encode_data:
        current_code += '1' if bit else '0' 

        #Cuando current_code coincide con un código en reverse_code, 
        # se añade el píxel correspondiente a decoded_pixels y se reinicia current_code
        if current_code in reverse_code: 
            decoded_pixels.append(reverse_code[current_code])
            current_code = ""
    
    #Reconstruye la imagen
    image = Image.new('RGB', (width, height))
    image.putdata(decoded_pixels)
    return image

