print('''
            Ola! Seja bem vindo(a)!
             ''')

num = []
par = []
impar = []
while True:
    lista = int(input('Digite um numero: '))
    num.append(lista)
    cont = input('Deseja continuar? [S/N]  ')
    if cont in 'Nn':
        break
    else:
        continue
    
for n in range(0,len(num)):
    if num[n] % 2 == 0:
        par.append(num[n])
    else:
        impar.append(num[n])

print('=-' * 30)
print(f' Os numeros digitados foram: {num} \n Os numeros pares sao {par}\n Os numeros impares sao {impar}')