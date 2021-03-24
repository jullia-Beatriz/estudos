from math import cos, sin, tan, radians
an=float(input(' digite o valor do angulo:  '))
seno=sin(radians(an))
cos=cos(radians(an))
tang=tan(radians(an))

print(f' O angulo de {an}g tem: \n O seno de:     {seno:.2f}')
print(f' O cosseno de:  {cos:.2f}')
print(f' A tangente de: {tang:.2f}')