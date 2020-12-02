class Pilha:
    # Definir Váriaveis iniciais
    def __init__(self):
        self.vet = []

    # Retorna o Item que estiver no topo
    def peek(self):
        return self.vet[-1]
    
    # Insere na pilha
    def push(self, item):
        self.vet.append(item)
    
    # Remove o topo e retorna o item para o usuário
    def pop(self):
        if not self.is_empty():
            return self.vet.pop()
        print("Pilha Vazia!")

    # Verifica se a pilha está vazia
    def is_empty(self):
        if len(self.vet) == 0:
            return True
        return False
    
    # Retorna o tamanho da Pilha
    def __len__(self):
        return len(self.vet)
    
    # Retornar a Pilha como String
    def __str__(self):
        return str(self.vet)