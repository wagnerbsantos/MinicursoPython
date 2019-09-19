print('Insira dois numeros')
numero1 = int(input())
numero2 = int(input())
soma = numero1 + numero2
print('A soma dos dois numeros e: ' + str(soma))

if (soma == 20):
    print('Tu colocou um numero bem grande, vamos fazer ele maior')
    soma = soma + 1000000000
elif(soma > 10):
    print('VISH')
else:
    print('Nao e maior do que 10')

print('O seu novo numero e: '+ str(soma))