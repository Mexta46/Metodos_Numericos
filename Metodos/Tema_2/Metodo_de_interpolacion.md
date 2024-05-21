# Interpolación
## Definición
La interpolación es un método numérico utilizado para estimar valores desconocidos de una función a partir de un conjunto de puntos conocidos. Los métodos de interpolación crean una función continua que pasa a través de todos los puntos dados y se utiliza para estimar valores entre estos puntos.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema2/interpolacion.jpg)

## Algoritmo
1. Definir el conjunto de puntos \((x_i, y_i)\) donde \( y_i = f(x_i) \).
2. Elegir el método de interpolación adecuado (e.g., interpolación lineal, interpolación polinómica).
3. Construir la función de interpolación que pase a través de todos los puntos dados.
4. Utilizar la función de interpolación para estimar valores en puntos desconocidos.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema2/interpolacionf.png)

## Metodología

### Código en Python para Interpolación Lineal
A continuación, se presenta un ejemplo de código en Python para aplicar la interpolación lineal para estimar valores de una función desconocida a partir de un conjunto de puntos conocidos.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Definir los puntos conocidos (x, y)
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# Crear la función de interpolación lineal
f_interpolada = interp1d(x, y, kind='linear')

# Definir los puntos donde se desea estimar los valores
x_nuevo = np.linspace(0, 5, 50)
y_nuevo = f_interpolada(x_nuevo)

# Graficar los puntos conocidos y la función de interpolación
plt.plot(x, y, 'o', label='Puntos conocidos')
plt.plot(x_nuevo, y_nuevo, '-', label='Interpolación lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación Lineal')
plt.show()
```

### Código en Python para Interpolación Polinómica
También se puede utilizar la interpolación polinómica para ajustar un polinomio que pase por todos los puntos conocidos.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Definir los puntos conocidos (x, y)
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# Crear el polinomio de interpolación
polinomio = lagrange(x, y)

# Definir los puntos donde se desea estimar los valores
x_nuevo = np.linspace(0, 5, 50)
y_nuevo = polinomio(x_nuevo)

# Graficar los puntos conocidos y el polinomio de interpolación
plt.plot(x, y, 'o', label='Puntos conocidos')
plt.plot(x_nuevo, y_nuevo, '-', label='Interpolación polinómica')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación Polinómica')
plt.show()
```

### Resultados y Análisis
Los códigos anteriores aplican la interpolación lineal y polinómica a un conjunto de puntos conocidos. Los resultados se muestran en gráficos que ilustran cómo la función de interpolación pasa a través de todos los puntos conocidos y estima valores en puntos intermedios.
