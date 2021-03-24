from time import sleep

print('Ola seja bem vindo(a)!')
sexo = str(input('Digite seu sexo para ser registrado no servidor: [M]/[F]  ')).strip().upper() [0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos! por favor informe seu sexo: [M]/[F]  ')).strip().upper() [0]
print(f'Sexo [{sexo}] registrado com sucesso! ')