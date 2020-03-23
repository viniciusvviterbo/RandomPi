import argparse
import math
import random

# Configuracao do argumento
parser = argparse.ArgumentParser(description = 'Software para calcular o valor de pi baseado exclusivamente na geração aleatória de números entre 0 e 1.')
parser.add_argument('-n', action = 'store', dest = 'num_pnts', default = '', required = True, help = 'Número de pontos a serem gerados.')
arguments = parser.parse_args()
num_pnts = int(arguments.num_pnts)
# Declara a variável que conta o número de pontos dentro do círculo no plano cartesiano
num_pnts_circulo = 0
# Declara a variável que conta o número total de pontos dentro do quadrado no plano cartesiano
num_pnts_total = 0
# Realiza uma iteração para cada ponto
for numero_de_pontos in range(num_pnts):
    # Gera as coordenadas do ponto da iteração
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    # Calcula a distância entre o ponto da iteração e o ponto (0,0)
    dist = math.sqrt(x*x + y*y)
    # Testa se o ponto esteja dentro do círculo de raio = 1
    if dist <= 1:
        # Acrescenta o contador de pontos dentro do círculo em 1
        num_pnts_circulo += 1
    # Acrescenta o contador de pontos dentro do quadrado em 1
    num_pnts_total += 1
# Calcula o valor de pi a partir dessa equação deduzida
pi = 4 * num_pnts_circulo / num_pnts_total
# Exibe o valor encontrado (quanto maior o número de pontos, mais preciso é o valor retornado)
print(pi)