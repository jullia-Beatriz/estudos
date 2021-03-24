print('Ola! seja bem vindo ao meu programa!')
n = int(input('Digite o numero final:  \nVou te mostrar todos os numeros pares!  '))

for n in range(0,n+1):
    p = n%2
    if p == 0:
        print(n , end=' ')