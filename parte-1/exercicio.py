import random

play = True
n = random.randint(0,100)
while play:
    usu = input()
    if usu == '':
        break
    num = int(usu)
    if (num == n):
        print('voce ganhou')
        n = random.randint(0,100)
    elif (num < n):
        print('o seu numero e menor')
    else:
        print('o seu numero e maior')