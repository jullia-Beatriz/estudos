frase = input('Digite uma frase: ')
frase = frase.upper()
frase = frase.replace(" ", "")
inv = frase[::-1]

if frase == inv:
    print(f'''O inverso de {frase} e {frase}
    temos um Palindromo!''')
else:
    print('''para formar um Palindromo a frase tem que ter  mesmo sentido sendo lida de tras para frente!
A frase nao formou um Palindromo!
    tente novamente!''')