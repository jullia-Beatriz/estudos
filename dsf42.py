r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:  '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3 and r3 == r1:
        print('Os segmentos acima formam um triangulo EQUILATERO!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Os segmentos acima formam um triangulo ISOSCELES!')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('Os segmentos acima formam um triangulo ESCALENO!')
else:
    print('Os segmentos acima NAO PODEM FORMAR UM TRIANGULO!')