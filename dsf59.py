from time import sleep

print('Ola seja bem vindo(a)!')
v1 = int( input('Digite o primeiro valor: '))
v2 = int( input('Digite o segundo valor:  '))
opcao = 0
soma = (v1 + v2)
mult = (v1 * v2)

while opcao != 5:
    print("""Ok! vou mostrar na tela as opcoes: 
[1] Somar
[2] Multiplicar
[3] maior valor
[4] Novos numeros
[5] Sair do programa""")
    opcao = int( input('digite sua resposta:  '))
    if opcao == 1:
        print(f'O resultado entre {v1} + {v2} e: {soma}!')
    elif opcao == 2:
        print(f'O resultado entre {v1} X {v2} e: {mult}!')
    elif opcao == 3:
        if v1 > v2:
            print(f'O maior valor e: {v1}!')
        if v2 > v1:
            print(f'O maior valor e: {v2}!')
    elif opcao == 4:
        v1 += int(input('Digite o novo primeiro valor:  '))
        v2 += int(input('digite o novo segundo valor:  '))
    elif opcao == 5:
        print('finalizando ...')
        sleep(2)
        break
    else:
        print('opcao invalida, tente novamente!')
        
print('Fim do programa! Volte sempre!')