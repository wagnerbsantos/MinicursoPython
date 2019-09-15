class Ponto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, ponto):
        return ((ponto.x - self.x)**2 + (ponto.y - self.y)**2)**0.5

    def soma(self, ponto):
        pass

    def subtracao(self, ponto):
        pass

    def avacalhador_de_listas(lista):
        for i in range(len(lista)):
            lista[i] = 0
        return lista
        
if __name__ == '__main__':
    print("ta executando a classe ponto")