# Interpolacion de Lagrange
## Definición
La interpolación de Lagrange es un método numérico utilizado para encontrar el polinomio único de grado n que pasa por un conjunto de n+1 puntos dados (x0, y0), (x1, y1), ..., (xn, yn). Este polinomio interpolante, denotado como P(x), se expresa como una combinación lineal de polinomios base llamados polinomios de Lagrange:
P(x) = y0L0(x) + y1L1(x) + ... + ynLn(x)
donde los polinomios de Lagrange Li(x) se definen como:
Li(x) = ((x - x0) / (xi - x0)) * ((x - x1) / (xi - x1)) * ... * ((x - xi-1) / (xi - xi-1)) * ((x - xi+1) / (xi - xi+1)) * ... * ((x - xn) / (xi - xn))
Estos polinomios de Lagrange tienen la propiedad de que Li(xj) = 0 para todo j ≠ i, y Li(xi) = 1.
## Algoritmo
1. Obtener los puntos (x0, y0), (x1, y1), ..., (xn, yn).
2. Para cada punto (xi, yi): a. Inicializar el polinomio de Lagrange Li(x) = 1. b. Para cada j desde 0 hasta n, j ≠ i: Li(x) = Li(x) * ((x - xj) / (xi - xj))
3. Construir el polinomio interpolante P(x) como la suma ponderada de los polinomios de Lagrange: P(x) = y0L0(x) + y1L1(x) + ... + ynLn(x)
4. Evaluar el polinomio interpolante P(x) en el punto deseado x_eval.