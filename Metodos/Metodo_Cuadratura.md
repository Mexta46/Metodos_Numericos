# Cuadratura de Gauss con Python
### Definicion
La cuadratura de Gauss aproxima el integral de una función en un intervalo [a,b] centrado en cero mediante un cálculo numérico con menos operaciones y evaluaciones de la función. Se representa como una suma ponderada:
![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/1af68233-4ecb-4052-a565-cfba89dbfec3)

## Algoritmo


## Metodologia
```python

# Integración: Cuadratura de Gauss de dos puntos
# modelo con varios tramos entre [a,b]
import numpy as np
import matplotlib.pyplot as plt

# cuadratura de Gauss de dos puntos
def integraCuadGauss2p(funcionx,a,b):
    x0 = -1/np.sqrt(3)
    x1 = -x0
    xa = (b+a)/2 + (b-a)/2*(x0)
    xb = (b+a)/2 + (b-a)/2*(x1)
    area = ((b-a)/2)*(funcionx(xa) + funcionx(xb))
    return(area)

# INGRESO
fx = lambda x: np.sqrt(x)*np.sin(x)

# intervalo de integración
a = 1
b = 3
tramos = 4

# PROCEDIMIENTO
muestras = tramos+1
xi = np.linspace(a,b,muestras)
area = 0
for i in range(0,muestras-1,1):
    deltaA = integraCuadGauss2p(fx,xi[i],xi[i+1])
    area = area + deltaA
# SALIDA
print('Integral: ', area)


```

## Ejemplos

----------------------

1.-


--------------------------

2.-


----------------------
