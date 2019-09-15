print('Quantos valores quer colocar na lista')

n = int(input())
lista = [] #Lista vazia
conjunto = set() #Conjunto vazio
dicionario = {} #Dicionario vazio

for i in range(n):
    print('Entre com o valor '+ str(i))
    valor = int(input())
    lista.append(valor)
    conjunto.add(valor)
    print('Entre com um nome para o dicionario')
    nome = input()
    dicionario[nome] = valor

print(lista)
print('-----------------------------')
print(conjunto)
print('-----------------------------')
print(dicionario)
print('-----------------------------')

contador = 0
while contador < len(lista):
    print(lista[contador])
    contador += 1

print('Escolha um nome do dicionario')
nome = input()
conjunto.
if nome in dicionario.keys():
    print(dicionario[nome])