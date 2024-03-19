# Metodo 4: Gauss-seidel
### Definicion
El método de Gauss-seidel es muy semejante al método de Jacobi. Mientras que en el de Jacobi se utiliza el valor de las incógnitas para determinar una nueva aproximación, en el de Gauss-Seidel se va utilizando los valores de las incógnitas recien calculados en la misma iteración, y no en la siguiente.
Lo que hace este método es reemplazar las variables que fueron calculadas en la iteración anterior por las de la iteración actual al instante. De esta manera, se reduce el número de iteraciones.
### Algoritmo
1. Ordenar el sistema de ecuaciones para convertirla en matriz, asegurandose que la matriz:
 - No tenga elementos nulos.
 - La matriz tiene que ser dominante. Esto quiere decir que los elementos en la diagonal, deben de contener el mayor coeficiente de la ecuación.
 - El sistema de ecuaciones debe de ser cuadrado, es decir, el número de ecuaciones es igual al número de incógnitas.
2. Despejar las respectivas variables de cada columna en la diagonal de los elementos.
3. Inicializar a cada variable como 0.
4. Calcular la siguiente iteración usando las ecuaciones anteriores y los valores de las iteraciones más actuales.
5. Calcular el porcentaje de error.
6. Repetir el paso 4 hasta que el error igual al esperado.
### Metodologia
8x+y+4z=1

2x+10y+6z=4

4x+3y+9z=6
![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-19%20004013.png)
### Ejemplos

------------

3x+y=6

x+2y=2

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-19%20004654.png)

------------

8x-2y=9

x+13y=20

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-19%20005149.png)

------------

2x+y=9

x-5y=4

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-19%20005402.png)
