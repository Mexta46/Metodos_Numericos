# Cuadratura de Gauss con Python
## Definicion
La cuadratura de Gauss aproxima el integral de una función en un intervalo [a,b] centrado en cero mediante un cálculo numérico con menos operaciones y evaluaciones de la función. 


## Algoritmo

El algoritmo se desarrolla en un tramo en el intervalo [a,b] junto a la gráfica para mostrar el concepto. 

Se representa como una suma ponderada:

![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/1af68233-4ecb-4052-a565-cfba89dbfec3)

![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/18673eab-ce26-4360-a2fa-1b880337b241)


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

Instrucciones usando la cuadratura de Gauss como una función

1.- Para el ejemplo el integral buscado es:

![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/e7e60bc9-ee4f-4667-af94-1c0d4f6df56f)

que usando cuadratura de Gauss con un solo intervalo[a,b] tiene como resultado:

![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/1d5a68e8-83cb-4a10-a765-c571b2d7a935)

>Integral:  2.03821975687

---------------------

2.- El resultado se puede mejorar aumentando el número de tramos en el intervalo [a,b]. Por ejemplo, el resultado usando 4 tramos el resultado es semejante al usar el método del trapecio con 128 tramos, lo que muestra el ahorro en calculos entre los métodos

----------------------

>Integral:  2.05357719003

![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/3c656246-45b8-408b-9c74-d3d0ec721241)

----------------------

3.- intervalo de integración

a = 4 

b = 9

tramos = 4


![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/c0840c15-10ba-4d93-a25b-2a33d8f19421)

----------------------

4.- intervalo de integración.

a = 2

b = 4

tramos = 4

![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/a57269fb-eacd-4b58-94d6-2346e8c115c4)

----------------------

5.- intervalo de integración

a = 1.3

b = 1.8

tramos = 4

![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/78ad83aa-f01c-439b-8dc4-014431a27aed)

---------------------------
