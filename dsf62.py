print(''' 
       10 TERMOS DE UMA PA 
''')
pri = int(input('Primeiro termo:  '))
raz = int(input('Razao:  '))
termo = pri
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} > ',end='')
        termo += raz
        cont += 1 
    print('PAUSA!')
    mais = int(input('Quantos termos mais voce quer mostrar?  '))

print(f'Progressao finalizada com {total} termos!')