print('Entre com frases separadas por ;')
texto = input()

texto_formatado = texto.title()
print(texto_formatado)

lista = texto.split(';')
#pdb.set_trace()
for frase in lista:
    novo = frase.replace(' ', ' ^_^ ')
    print(frase + ' -> ' + novo)

