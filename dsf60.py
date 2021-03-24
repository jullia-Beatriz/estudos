'''from math import factorial
n = int(input('Digite um numero para ver o seu fatorial:  '))
f = factorial(n)
print(f'o fatorial de {n}! e {f} ')'''

n = int(input('Digite um numero para ver seu fatorial:  '))
c = n
f = 1
print(f' Calculando {n}!')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else' = ' , end='')
    f *= c
    c -= 1
print(f)