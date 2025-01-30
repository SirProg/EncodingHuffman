from Huffman_queue.HuffmanNode import HuffmanNode
from PIL import Image
from collections import defaultdict
from bitarray import bitarray
import heapq

def create_huffman_tree(frequencies: defaultdict):
    #Frecuencies es un diccionario, donde las claves son los pixeles y los valores su frecuencia
    #Creacion de nodos iniciales y se crea un nodo con HuffmanNode
    heap = [HuffmanNode(symbol, freq) for symbol, freq in frequencies.items()]
    #Se convierte en cola de prioridad, en la cual el nodo con la frecuencia más baja se encuentre en la parte superior
    heapq.heapify(heap)
    #Combinacion de los nodos hasta formar el Árbol
    while len(heap) > 1:
        first_node = heapq.heappop(heap)
        second_node = heapq.heappop(heap)
        merged = HuffmanNode(None, first_node.frecuency + second_node.frecuency)
        merged.left = first_node
        merged.right = second_node
        heapq.heappush(heap, merged)
    #Retorna la raiz del Árbol
    return heap[0]

def create_huffman_code(root: list):
    code_map = {} #Mapa de codigos

    def traverse(node: list, code: str):
        #Si el nodo actual contiene un símbolo (es una hoja), se almacena el código generado en code_map
        if node.symbol is not None:
            code_map[node.symbol] = code
            return
        #Si el nodo no contiene un símbolo (es un nodo interno)
        # se continúa el recorrido por los hijos izquierdo y derecho, añadiendo "0" o "1" al código
        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, '')#Encargado de iniciar el recorrido

    return code_map #Retorna el mapa de códigos

