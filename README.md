# RandomPi

Software para calcular o valor de pi baseado exclusivamente na geração aleatória de números entre 0 e 1.

### Instalando as dependências

Clone esse repositório e:
```
pip3 install argparse
```

### O problema

Você tem uma função chamada *random()* que gera um número de 0 a 1 de modo aleatório e uniformamente distribuído.
Calcule o valor de pi.

### A Resolução

A ideia básica é gerar dois números aleatórios com a função *random()* de modo a criar as coordenadas cartesianas de um ponto dentro de um plano. Depois disso, gera-se *n* coordenadas do mesmo modo:

imagem1

Podemos agora considerar a área com os pontos acima como um quarto de um quadrado 2x2. Se desenharmos um círculo de raio 1 inteiramente dentro desse quadrado teremos:

imagem2

O objetivo agora é contar o número de pontos dentro do círculo e todos os que estão dentro do quadrado.
A proporção entre esses dois números será aproximada da proporção entre a área do círculo e a área do quadrado.

imagem3 - equacao das proporções

Para saber se um ponto está ou não dentro do círculo, utiliza-se do Teorema de Pitágoras, assim, se a distância da coordenada de um ponto é menor que o tamanho do raio da circunferência, ele está dentro do círculo:

imagem4 - teorema de pitágoras

Sabe-se que a área de um círculo é:

imagem5 - fórmula pi*r^2

E que a fórmula da área desse quadrado é:

imagem6 - fórmula (2*r)^2

Assim encontramos a equação:

imagem7 - (pi*r^2)/((2*r)^2) = (num pts dentro do círculo)/(num pts total)

Dela podemos deduzir a fórmula:

imagem8 - pi = 4 * (num pts dentro do círculo) / (num pts total)

E assim, encontramos o valor de pi utilizando apenas a função *random()*.


**[Problema baseado neste vídeo do canal 'Joma Tech'](https://www.youtube.com/watch?v=pvimAM_SLic&feature=youtu.be)**