# Interpolación lineal

## Definicion 

La fórmula de interpolación lineal es el método más simple que se utiliza para estimar el valor de una función entre dos valores conocidos. Además, la fórmula de interpolación lineal es un método útil para ajustar curvas utilizando polinomios lineales. Básicamente, el método de interpolación se utiliza para encontrar nuevos valores para cualquier función utilizando el conjunto de valores. Los valores desconocidos en la tabla se encuentran usando la fórmula de interpolación lineal.

La fórmula de interpolación lineal es el método más simple que se utiliza para estimar el valor de una función entre dos valores conocidos. Además, la fórmula de interpolación lineal es un método útil para ajustar curvas utilizando polinomios lineales. Básicamente, el método de interpolación se utiliza para encontrar nuevos valores para cualquier función utilizando el conjunto de valores. Los valores desconocidos en la tabla se encuentran usando la fórmula de interpolación lineal.

## Fórmula
![Formula](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcdgJkeZFq65sgSuHEB_7nEooMkJ1sWJTqF3uidUKv&s)

## Algoritmo
**Paso 1:** Empezar.

**Paso 2:** Leer los puntos de datos (x 0 , y 0 ) y (x 1 , y 1 ).

**Paso 3:** Leer el valor de las variables independientes, digamos xp cuyo valor correspondiente de dependiente digamos yp debe ser determinado.

**Paso 4:** Calcula yp = y 0 + ((y 1 - y 0 )/(x 1 - x 0 )) * (x - x 0 ).

**Paso 5:** Muestra el valor de yp como valor interpolado.

## Metodologia 
def interpolacion_lineal(x0, y0, x1, y1, x):
    m = (y1 - y0) / (x1 - x0)
    y = (m * (x - x0)) + y0
    return y

def main():
    x0 = 1.0
    y0 = 75.0
    x1 = 3.0
    y1 = 100.0
    
    x = 6
    
    y = interpolacion_lineal(x0, y0, x1, y1, x)
    
    print(f"El valor de y para x = {x} es: {y}")

if __name__ == "__main__":
    main()
    
## Ejemplos 


