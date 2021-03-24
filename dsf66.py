cont = soma = 0

while True:
    num = int(input('[999 flag de parada] Digite um numero:  ' ))
    if num == 999:
        break
    cont +=1
    soma += num
print(f'Foram digitados {cont} numeros e a soma dos valores e {soma}.')