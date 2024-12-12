class HuffmanNode:
    def __init__(self, symbol, frencuency):
        self.symbol = symbol
        self.frecuency = frencuency
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.frecuency < other.frecuency