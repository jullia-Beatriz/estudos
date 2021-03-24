menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p} pessoa:  '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'''O maior peso encontrado foi de {maior}kg!
O menor peso encontrado foi de {menor} kg! ''')