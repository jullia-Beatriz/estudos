print('''
         Ola! Seja bem vindo(a)! 
Digite [0] a qualquer momento para sair!        ''')

lista = []
while True:
    num = int(input('Digite um valor:  '))
    lista.append(num)
    if num == 0:
        break

if 5 in lista:
    print(f'O numero 5 esta na lista!')
else:
    print('O numero 5 nao esta na lista!')

print(f'A lista tem {len(lista)} elementos :',end='' )
print(sorted(lista))