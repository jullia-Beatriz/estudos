print('ola seja bem vindo!')
nome = input('digite seu nome completo: ')
nome = nome.title() 
print('seu nome possui Silva? ')
if 'Silva' in nome:
    print(True)

elif '' in nome:
    print(False)