lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print(' ') #metodo mais simples mostrar itens da tupla

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')
print(' ') #mostrar posicao dos itens na tupla

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
print(' ') # metodo mais longo de mostrar a posicao dos itens

print(sorted(lanche))
print(lanche)
print(lanche.index(pizza)) # index . em que posicao esta tal item
print(lanche.count(pizza)) #quantas vezes aparece

print('Comi pra caramba!')

