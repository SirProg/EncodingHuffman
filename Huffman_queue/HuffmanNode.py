class HuffmanNode:
    def __init__(self, symbol, frencuency):
        self.symbol = symbol
        self.frecuency = frencuency
        self.left = None
        self.right = None
    
    #Define el comportamiento de dos nodos, de esta manera se ordenan en un heap 
    # basandose en la frecuencia
    def __lt__(self, other):
        return self.frecuency < other.frecuency