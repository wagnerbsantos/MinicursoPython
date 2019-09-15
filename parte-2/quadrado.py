from ponto import Ponto

class Quadrado:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        lado1 = abs(self.p1.x - self.p2.x)
        lado2 = abs(self.p1.y - self.p2.y)
        return lado1 * lado2

    def perimetro(self):
        pass