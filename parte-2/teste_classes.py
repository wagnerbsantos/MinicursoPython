from ponto import Ponto
from quadrado import Quadrado

if __name__ == '__main__':
    p1 = Ponto(1,2)
    p2 = Ponto(4,4)
    quadrado = Quadrado(p1,p2)
    lista = [1, 2, 3, 4]


    print(quadrado.area())
    print(lista)
    #l1 = Ponto.avacalhador_de_listas(tuple(lista))
    #print(lista)
    #l1 = Ponto.avacalhador_de_listas(lista.copy())
    #print(lista)
    l1 = Ponto.avacalhador_de_listas(lista)

    print(lista)
    print(l1)