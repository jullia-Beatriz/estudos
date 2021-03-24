print('ola seja bem vindo! ', end=' ')
nome=input('qual e o seu nome? ')
from time import sleep
n=int(input('escolha um numero: '))
d=n*2
t=n*3
r=n**(1/2)
rt=n**(1/3)
print('seu numero e {}, \n seu dobro e {},\n seu triplo e {},\n sua raiz quadrada: {:.3f},\n sua raiz cubica: {:.3f}'.format(n, d, t, r, rt))