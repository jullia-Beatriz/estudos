galera = list()
dado = list()

totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome:  ')))
    dado.append(int(input('Idade:  ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} e MAIOR de idade.')
        totmai += 1 
    else:
        print(f'{p[0]} e MENOR de idade.')
        totmen += 1

print(f'Temos {totmai} MAIORES e {totmen} MENORES de idade.')