# Metodo 3: Jacobi
### Definicion
El método de Jacobi es un método iterativo para resolver sistemas de ecuaciones lineales más simple y se aplica sólo a sistemas cuadrados, es decir, a sistemas con tantas incógnitas como ecuaciones.
Para cada iteración, el método utiliza los valores previamente estimados de las variables. En caso de ser la iteración inicial, las variables tienen valores default, o bien, el usuario define dichos valores.
### Algoritmo
1. Ordenar el sistema de ecuaciones para convertirla en matriz, asegurandose que la matriz:
 - No tenga elementos nulos.
 - La matriz tiene que ser dominante. Esto quiere decir que los elementos en la diagonal, deben de contener el mayor coeficiente de la ecuación.
 - El sistema de ecuaciones debe de ser cuadrado, es decir, el número de ecuaciones es igual al número de incógnitas.
2. Despejar las respectivas variables de cada columna en la diagonal de los elementos.
3. Inicializar a cada variable como 0.
4. Calcular la siguiente iteración usando las ecuaciones anteriores y los valores de las iteraciones anteriores.
5. Calcular el porcentaje de error.
6. Repetir el paso 4 hasta que el error igual al esperado.
### Metodologia

9x+2y-z=-2 

7x+8y+5z=3 

3x+4y-10z=6

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-18%20234208.png)
### Ejemplos

------------

7x+3y=3

2x+4y=10

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-19%20000244.png)

------------

5x-3y=7

3x+7y=4

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-19%20001213.png)

------------

8x+y=1

2x-5y=4

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/imagen_2024-03-19_001958333.png)


------------

7x+4y+4z=50

3x+8y+5z=20

2x+1y+10z=15

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/imagen_2024-03-22_214524697.png)

------------

10x-2y+9z=15

x+5y-4z=2

5x-y+25z=15

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/imagen_2024-03-22_215713983.png)
