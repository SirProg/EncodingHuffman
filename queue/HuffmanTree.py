import HuffmanNode
from PIL import Image
from collections import Counter
from bitarray import bitarray
import heapq

def create_huffman_tree(frequencies: Counter):
    heap = [HuffmanNode(symbol, freq) for symbol, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        first_node = heapq.heappop(heap)
        second_node = heapq.heappop(heap)
        merged = HuffmanNode(None, first_node.freq + second_node.freq)
        merged.left = first_node
        merged.right = second_node
        heapq.heappush(heap, merged)
    
    return heap[0]

def create_huffman_code(root: list):
    if code_map is None:
        code_map = {}

    def traverse(node: list, code: str):
        if node.symbol is not None:
            code_map[node.symbol] = code
            return
        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, '')

    return code_map

