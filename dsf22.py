print('hello word!')
print('ola, seja bem vindo(a)!')
nome=input('digite seu nome completo: ').strip()
print('processando seu nome ...')

print(f'seu nome em maiusculas: {nome.upper()}')
print(f'seu nome em minusculas: {nome.lower()}')
'''print(f' seu nome possui: {len(nome.replace(" ",""))} caracteres')'''
print(f'seu primeiro nome possui: {len(nome.split()[0])} caracteres')
print(f'seu nome possui: {len(nome) - nome.count(" ")} caracteres' )