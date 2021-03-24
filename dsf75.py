n = (int(input('Digite um numero:  ')), int(input('Digite um numero:  ')),
int(input('Digite um numero:  ')), int(input('Digite um numero:  ')))

print(f'Voce digitou os valores: {n}!')
print(f'O numero 9 apareceu {n.count(9)} vezes !')
if 3 in n:
    print(f'O numero 3 foi digitado na posicao: {n.index(3)}!')
else:
    print('O numero 3 nao foi digitado !')
print('Os valores pares digitados foram: ',end='')
for num in n:
    if num % 2 == 0:
        print(num , end='. ' )