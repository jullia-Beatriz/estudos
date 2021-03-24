# valores = list()

# while True:
#     num = int(input('Digite um valor:  '))

#     if num in valores:
#         print('Valor duplicado nao adicionado!')
#         cont = str(input('Deseja continuar? [S/N]  ')).upper()
#         if cont in 'S':
#             continue
#         else:
#             print(sorted(valores))
#             break
#     else:
#         print('Valor adicionado com sucesso!')
#         valores.append(num)
#         cont = str(input('Deseja continuar? [S/N]  ')).upper()
#         if cont in 'S':
#             continue
#         else:
#             print(sorted(valores))
#             break

lista = []

while True:
    num = int(input("digite ou numero ou 0 para sair"))
    if num == 0:
        print(sorted(lista))
        break
    if num not in lista:
        lista.append(num)
    else:
        print("duplicado")


