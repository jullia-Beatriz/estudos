print(''' 
       10 TERMOS DE UMA PA 
''')
pri = int(input('Primeiro termo:  '))
raz = int(input('Razao:  '))
dec = pri + (10 - 1) * raz
for c in range(pri, dec, raz):
    print(c, end =' \ ')
print('ACABOU!', end='')