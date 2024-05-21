# Overflow
## Definición
El overflow (desbordamiento) ocurre cuando un cálculo produce un resultado que es mayor que el valor máximo que puede ser representado con el tipo de datos numérico utilizado en el sistema de cómputo. Esto puede llevar a resultados incorrectos o a la pérdida de información.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/overflow.png)

## Algoritmo
1. Definir la función f(x) cuyo cálculo puede llevar al overflow.
2. Especificar el intervalo de evaluación [a, b].
3. Dividir el intervalo [a, b] en n subintervalos de igual tamaño.
4. Calcular el valor de f(x) en puntos específicos del intervalo.
5. Detectar si ocurre overflow y manejarlo adecuadamente.
6. Analizar cómo y dónde ocurre el overflow a lo largo del intervalo.
7. Devolver los valores calculados y las instancias de overflow detectadas.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/overflowf.png)

## Metodología

### Código en Python para Evaluar el Overflow
A continuación, se presenta un ejemplo de código en Python para evaluar el problema de overflow en la función \( f(x) = e^x \) en el intervalo [0, 50].

```python
import numpy as np

def calcular_overflow(f, a, b, n):
    """
    Función para detectar overflow en la evaluación de una función f(x) en el intervalo [a, b].

    Parámetros:
    f (función): Función a evaluar.
    a (float): Límite inferior del intervalo.
    b (float): Límite superior del intervalo.
    n (int): Número de subintervalos.

    Devuelve:
    list: Lista de valores calculados y marcas de overflow en los puntos del intervalo.
    """
    h = (b - a) / n  # tamaño del subintervalo
    valores = []
    overflows = []

    for i in range(n + 1):
        x = a + i * h
        try:
            valor = f(x)
            valores.append(valor)
            overflows.append(False)
        except OverflowError:
            valores.append(float('inf'))  # Usar infinito para marcar overflow
            overflows.append(True)

    return valores, overflows

# Definición de la función a evaluar
def f(x):
    return np.exp(x)

# Parámetros del intervalo
a = 0
b = 50
n = 10  # número de subintervalos

# Calcular valores y detectar overflow
valores, overflows = calcular_overflow(f, a, b, n)

# Imprimir resultados
print("x\tValor\t\tOverflow")
for i in range(n + 1):
    x = a + i * h
    overflow = "Sí" if overflows[i] else "No"
    print(f"{x:.2f}\t{valores[i]:.5e}\t{overflow}")
```

### Resultados y Análisis
El código anterior genera una tabla que muestra el valor de la función y si ocurrió overflow en varios puntos del intervalo [0, 50]. Analizando estos resultados, se puede observar cómo y dónde ocurre el overflow, lo que ayuda a entender mejor las limitaciones de representación numérica y el comportamiento de la función en estos casos.
