from math import radians, cos, sin, tan


angulo = float(input('Valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'Seno: {seno:.2f}, Cosseno: {cosseno:.2f}, Tangente: {tangente:.2f}')
