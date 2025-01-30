from collections import defaultdict
from PIL import Image
from bitarray import bitarray
from Huffman_queue import HuffmanTree

import networkx as nx
import matplotlib.pyplot as plt


def compress_image_func(image: Image):
    width, height = image.size #Obtiene el tamaño de la imagen
    pixels = list(image.getdata())  #Obtiene los pixeles de la imagen

    #Se calcula la frecuencia de cada pixel
    freq_dict = defaultdict(int)
    for pixel in pixels:
        freq_dict[pixel] += 1
    
    root = HuffmanTree.create_huffman_tree(freq_dict) #En base a la frecuecia se crea el arbol de huffman
    huffman_codes = HuffmanTree.create_huffman_code(root) #En base a la raiz del arbol de hufman se genera los codigos para cada pixel.
    plot_huffman_tree(root) #visualizacion del arbol completo
    encode_data = bitarray()
    #Procede a codificar los pixeles, haciendo uso de los codigos de huffman generados
    for pixel in pixels:
        encode_data.extend(huffman_codes[pixel])
    
    #Datos comprimidos
    compress_data = {
        'width' : width,
        'height' : height,
        'huffman_codes' : huffman_codes,
        'encode_data' : encode_data
    }

    return compress_data
    
def plot_huffman_tree(tree):
    #Se inicializa el Arbol y su estructura de datos
    G = nx.DiGraph() #Representa el Árbol
    pos = {} #Posiciones de los nodos
    labels = {} #Etiquetas de los nodos

    #Función recursiva que recorre el árbol de Huffman y agrega nodos y aristas al grafo.
    def add_edges(node, x=0, y=0, layer=1):
        if node is not None:
            pos[id(node)] = (x, y) #Asignación de la posición del nodo
            #Si el nodo es interno (node.symbol is None), la etiqueta es su frecuencia
            #Si el nodo es una hoja, la etiqueta incluye el símbolo y la frecuencia
            labels[id(node)] = f"{node.frecuency}" if node.symbol is None else f"{node.symbol}:{node.frecuency}" 
            if node.left:
                G.add_edge(id(node), id(node.left))
                l = x - 1 / (2 ** layer)
                add_edges(node.left, x=l, y=y - 1, layer=layer + 1)
            if node.right:
                G.add_edge(id(node), id(node.right))
                r = x + 1 / (2 ** layer)
                add_edges(node.right, x=r, y=y - 1, layer=layer + 1)

    add_edges(tree)
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=2000, node_color="lightblue")
    plt.show()