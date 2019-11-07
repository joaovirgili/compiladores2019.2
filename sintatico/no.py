class No:
    filhos: []
    chave: str
    def __init__(self, chave, nome, filhos = []):
        self.chave = chave
        self.nome = nome
        self.filhos = filhos
