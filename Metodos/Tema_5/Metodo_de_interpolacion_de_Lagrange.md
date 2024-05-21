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

## Metodologia
``` Python
def lagrange_interpolation(xP, y_points, x_value): #evalua la interpolacion y previene que este tenga que dividir entre cero
    n = len(xP) #crea una lista con los valores de x
    for i in range(n): #recorre los valores para rectificar que estos no sean los mismo para dividir entre cero
        for j in range(i + 1, n):
            if x[i] == x[j]:
                raise ValueError(f"Los puntos x{i} y x{j} son idénticos, lo que causa una división por cero.") 
    result = 0 
    for i in range(n):
        termino = y_points[i]
        for j in range(n):
            if j != i:
                termino *= (x_value - xP[j]) / (xP[i] - xP[j])
        result += termino

    return round(result,2) #retorna el resultado a dos cifras significativas

try:
    num_points = int(input("Ingrese el número de puntos: ")) #se ingresa la cantidad de puntos a tratar
    if num_points <= 0: #verifica que el numero de puntos a tratar no sea menor a cero
        raise ValueError("El número de puntos debe ser mayor que cero.")

    xVal = [] #define una matriz de valores x
    yVal = [] #define una matriz de valores x

    for i in range(num_points):
        xi = float(input(f"Ingrese x{i}: ")) #se ingresan los valores de x
        yi = float(input(f"Ingrese y{i}: ")) #se ingresan los valores de y
        xVal.append(xi) #agrega los valores de x en la matriz de valores de x
        yVal.append(yi) #agrega los valores de y en la matriz de valores de y

    x = float(input("Ingrese el valor de x para evaluar el polinomio: ")) #pide el valor de x para calcular y
    result = lagrange_interpolation(xVal, yVal, x) 
    print(f"El valor del polinomio en x = {x} es: {result}") #muestra el resultado

except ValueError as e:
    print(f"Error: {e}")

```

## Ejemplos

------

Ejercicio 1 resuelto: se usaran los parametros
- numero de puntos: 4
- x0: 4
- y0: 6
- x1: 19
- y1: 20
- x2: 34
- y2: 32
- x3: 42
- y3: 47
- valor de x: 60

**Resultado**

![](https://github.com/Mexta46/Metodos_Numericos/blob/9e22efabf9c8dad6b9be0ecdd8d9af81d3d70575/Imagenes/Imagenes_tema5/LN1.png)

------

Ejercicio 2 resuelto: usando los parametros
- numero de puntos: 2
- x0: 34
- y0: 40
- x1: 50
- y1: 60
- valor de x: 77

**Resultado**

![](https://github.com/Mexta46/Metodos_Numericos/blob/9e22efabf9c8dad6b9be0ecdd8d9af81d3d70575/Imagenes/Imagenes_tema5/LN2.png)

-------

Ejercicio 3 resuelto: usando los valores
- numero de puntos: 5
- x0: 1
- y0: 6
- x1: 12
- y1: 17
- x2: 25
- y2: 30
- x3: 32
- y3: 38
- x4: 40
- y4: 47
- valor de x: 50

**Resultado**

![](https://github.com/Mexta46/Metodos_Numericos/blob/9e22efabf9c8dad6b9be0ecdd8d9af81d3d70575/Imagenes/Imagenes_tema5/LN3.png)

--------

Ejercicio 4 resuelto: usando los parametros
- numero de puntos: 2
- x0: 12
- y0: 24
- x1: 15
- y1: 30
- valor de x: 20

**Resultado**

![](https://github.com/Mexta46/Metodos_Numericos/blob/9e22efabf9c8dad6b9be0ecdd8d9af81d3d70575/Imagenes/Imagenes_tema5/LN4.png)

--------

Ejercicio 5 resuelto: usando los parametros
- numero de puntos: 3
- x0: 11
- y0: 22
- x1: 25
- y1: 30
- x2: 33
- y2: 45
- valor de x: 50

**Resultado**

![](https://github.com/Mexta46/Metodos_Numericos/blob/9e22efabf9c8dad6b9be0ecdd8d9af81d3d70575/Imagenes/Imagenes_tema5/LN5.png)