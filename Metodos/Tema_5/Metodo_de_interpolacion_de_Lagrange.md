# Interpolacion de Newton
## Definición
La interpolación de Newton es un método numérico utilizado para construir un polinomio de grado n que pase por un conjunto de n+1 puntos dados (x0, y0), (x1, y1), ..., (xn, yn). Este polinomio interpolante, denotado como P(x), se expresa en la forma de Newton:
P(x) = y0 + a1(x - x0) + a2(x - x0)(x - x1) + ... + an(x - x0)(x - x1)...(x - xn-1)
donde los coeficientes a1, a2, ..., an se conocen como diferencias divididas y se calculan a partir de los puntos dados.
Las diferencias divididas se definen recursivamente de la siguiente manera:

f[x0] = y0
f[x0, x1] = (y1 - y0) / (x1 - x0)
f[x0, x1, x2] = (f[x1, x2] - f[x0, x1]) / (x2 - x0)
...
f[x0, x1, ..., xn] = (f[x1, x2, ..., xn] - f[x0, x1, ..., xn-1]) / (xn - x0)

Así, las diferencias divididas representan las pendientes sucesivas de las secantes que unen los puntos dados.
## Algoritmo
1. Obtener los puntos (x0, y0), (x1, y1), ..., (xn, yn).
2. Construir una tabla de diferencias divididas de (n+1) filas y (n+1) columnas.
3. Inicializar la primera columna de la tabla con los valores y0, y1, ..., yn.
4. Calcular las diferencias divididas f[x0, x1], f[x0, x1, x2], ..., f[x0, x1, ..., xn] usando la definición recursiva y llenar la tabla de diferencias divididas.
3. Evaluar el polinomio interpolante P(x) en el punto deseado x utilizando la fórmula de Newton y las diferencias divididas calculadas.
