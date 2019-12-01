class TabelaDeSimbolos:
    def __init__(self):
        self.data = {}

    def add(self, x, y):
        self.data[x] = y

    def search(self, x):     
        if x in self.data:
            return self.data[x]
