# Cuadratura de Gauss con Python
## Definicion
La cuadratura de Gauss aproxima el integral de una función en un intervalo [a,b] centrado en cero mediante un cálculo numérico con menos operaciones y evaluaciones de la función. 


## Algoritmo

El algoritmo se desarrolla en un tramo en el intervalo [a,b] junto a la gráfica para mostrar el concepto. 

1.- Elección de los nodos y pesos: Elige los nodos X𝑖 y sus correspondientes pesos W𝑖​. Estos nodos y pesos están predefinidos para diferentes grados de precisión y se pueden encontrar en tablas.

2.- Transformación del intervalo de integración: Si la integral está definida en un intervalo [a,b]. diferente de [−1,1], es necesario transformarla al intervalo
[−1,1]. Esto se hace mediante una transformación lineal: ![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/7ef3e576-5664-4405-9e82-80bf49f6384b)

3.- Evaluación de la integral aproximada: Utiliza la fórmula de cuadratura de Gauss para calcular la aproximación de la integral: ![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/8145aed4-2e4a-45d9-a5d2-e20dc9f3f3f8) es la función que se está integrando.

4.- Transformación del resultado (opcional): Si has transformado el intervalo de integración en el paso 2, es posible que necesites transformar el resultado de vuelta al intervalo original. Esto se hace aplicando la transformación inversa.

5.- Calcular el error (opcional): Si conoces la fórmula del error para la cuadratura de Gauss, puedes calcular el error de aproximación. Por lo general, el error disminuye exponencialmente con el número de nodos.

6.- Iteración (opcional): Si la precisión deseada no se alcanza con el número de nodos elegidos inicialmente, puedes aumentar el número de nodos y repetir el proceso.

Es importante tener en cuenta que la elección adecuada de los nodos y pesos depende de la función que estés integrando y del grado de precisión que necesites.

![image](https://github.com/Mexta46/Metodos_Numericos_Tema4/assets/160789479/18673eab-ce26-4360-a2fa-1b880337b241)


## Metodologia
```python

                    # Integración: Cuadratura de Gauss de dos puntos
                    # modelo con varios tramos entre [a,b]
import numpy as np    #bibliotecas a importar 
import matplotlib.pyplot as plt

                    # cuadratura de Gauss de dos puntos
def integraCuadGauss2p(funcionx,a,b):
    x0 = -1/np.sqrt(3)
    x1 = -x0
    xa = (b+a)/2 + (b-a)/2*(x0)
    xb = (b+a)/2 + (b-a)/2*(x1)
    area = ((b-a)/2)*(funcionx(xa) + funcionx(xb))
    return(area)        #retorna area

                    # INGRESO
fx = lambda x: np.sqrt(x)*np.sin(x)

                    # intervalo de integración
a = 1                    #intervalo a
b = 3                    #intervalo b
tramos = 4                # numero de tramos

                    # PROCEDIMIENTO
muestras = tramos+1                #tramos 
xi = np.linspace(a,b,muestras)    
area = 0
for i in range(0,muestras-1,1):        # se declara un ciclo for
    deltaA = integraCuadGauss2p(fx,xi[i],xi[i+1])    # se calcula delta
    area = area + deltaA    #se suma el area y delta A
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
