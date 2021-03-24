#fatiamento
frase=('curso em video python')
print(frase[9])
print(frase[9:14])
print(frase[15:21])

#ANALISE
frase=('Curso Em Video Python')
print(len(frase)) #quantos caracteres a frase tem
print(frase.count('o',0 ,14))
print(frase.find('deo')) #encontre
print(frase.find('android'))
print ('Curso' in frase)

#TRANSFORMACAO
frase='curso em video python'
print(frase.replace('python', 'android')) #substitui python por android
print(frase.upper()) #maiusculas
print(frase.lower()) #minusculas
print(frase.capitalize()) #comeco da palavra masiculas
print(frase.title()) #comeco de todas as palavrsa maiusculas

frase='    aprenda python    '
print(frase.strip()) #elimina os espacos desnecessarios
print(frase.rstrip()) #comeca eliminar os espacos desnecessarios pela direita
print(frase.lstrip()) #comeca a remover pela esquerda

#DIVISAO
frase=('Curso Em Video Python')
print(frase.split()) #divide onde tem espacos e cria indices de palavras, virando uma lista

#JUNCAO
frase=('Curso Em Video Python')
print('-'.join(frase))