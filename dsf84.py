pessoas = list()
contp = 0


while True:
    pessoas.append(str(input('Nome:  ')))
    pessoas.append(int(input('Peso:  ')))
    stop = input('Deseja continuar? [S/N]  ')
    contp += 1
    if stop in 'Ss':
        continue
    else:
        break
print(f'Ao todo voce cadastrou {contp} pessoas.')
print(pessoas)