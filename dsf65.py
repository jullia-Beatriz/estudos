resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'Ss': 
    num = int(input('Digite um numero:  '))
    soma += num
    quant += 1 
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor :
            menor = num
    resp = str(input('quer continuar? [S/N]  ')).upper().strip()[0]

media = soma / quant
print(f'Voce digitou {quant} numeros e a media foi {media:.1f}')
print(f'O maior valor foi {maior}! e o menor valor foi {menor}!')