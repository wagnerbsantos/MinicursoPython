#crie uma classe circulo que calcula area e perimetro
#e nesse arquivo execute um c�digo que l� inputs do usu�rio, cria circulos e salva eles em um arquivo

from ponto import Ponto
from circulo import Circulo

if __name__ == '__main__':

    f = open('circulos.dat', 'w+') # w = escrita; + = cria um arquivo se n�o existir
    f.write('') #escreve uma linha no arquivo



    f.close()