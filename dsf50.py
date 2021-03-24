soma = 0
cont = 0

for item in range (1, 7):
    num = int(input('Digite um valor: '))
    if num %2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'voce informou {cont} numeros PARES! e a soma foi {soma}!')