from time import sleep
numero = int(input('Digite um numero que voce deseja converter: '))
print('Escolha uma das bases para conversao: \n[1] para BINARIO \n[2] para OCTAL \n[3] para HEXADECIMAL')
resp = int(input('Digite a sua resposta: '))
if resp == 1:
    print('O numero convertido para BINARIO e igual a:', bin(numero))
elif resp == 2:
    print('O numero convertido para OCTAL e igual a:', oct(numero))
elif resp == 3:
    print('O numero convertido para HEXADECIMAL e igaul a:', hex(numero))
else:
    print('Opcao invalida! tente novamente em 5 segundos.')
    sleep(5)