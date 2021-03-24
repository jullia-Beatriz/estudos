num = int(input('Digite um numero:  '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print(f'O numero {num} e um numero primo!')
else:
    print(f'O numero {num} nao e um numero primo!')