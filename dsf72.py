extenso = ('zero','um','dois','tres', 'quatro', 'cinco' ,'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove' , 'vinte' )
num = int(input('digite um numero (entre 0 e 20) para ve-lo por extenso:  '))

if num <= len(extenso):
    print('voce digitou o numero', extenso[num])
else:
    print('number invalid!')