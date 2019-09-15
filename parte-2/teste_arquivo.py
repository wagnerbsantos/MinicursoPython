from ponto import Ponto
from quadrado import Quadrado
import pdb

if __name__ == '__main__':
    pdb.set_trace()
    arquivo = open('pontos.dat', 'r')
    quadrados = []
    for linha in arquivo:
        pontos = linha.split(';')
        temp = []
        for p in pontos:
            pos = p.split(',')
            temp.append(Ponto(int(pos[0]), int(pos[1])))
        quadrados.append(Quadrado(temp[0], temp[1]))

    for q in quadrados:
        print(q.area())
    
    arquivo.close()
        