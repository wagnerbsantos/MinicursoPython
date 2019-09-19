from math import pi
from ponto import Ponto

class Circulo:
    
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
    def area(self):
        return pi * raio **2

    def perimetro(self):
        return 2 * pi * raio

if __name__ == '__main__':
    ponto1 = Ponto(0, 0)
    raio = 2
    circulo = Circulo(ponto1, raio)
    print("%.2f" % circulo.area())
    print("{0:.2f}".format( circulo.area()))

#area = pi * r
