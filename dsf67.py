cont = 0

while True:
    num = int(input('Digite o numero da tabuada que voce deseja cosultar:  [valor negativo para sair]  '))
    if num < 0:
        break
    print('-' * 30)
    for c in range(1 , 11):
        print(f'{num} X {c} = {num * c}')
    print('-' * 30)
print('Programa de tabuada encerrado! volte sempre!')