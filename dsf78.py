valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um numero para a posicao {cont}:  ')))

print(f'O maior valor digitado foi {max(valores)}! na posicao {valores.index(max(valores))}!')
print(f'O menor valor digitado foi {min(valores)}! na posicao {valores.index(min(valores))}!')