# Metodo 2: Gauss-Jordan
### Definicion
El método de Gauss-Jordan es una técnica de resolución de sistemas de ecuaciones lineales que utiliza la eliminación gaussiana, seguida de la eliminación de Gauss-Jordan para llevar la matriz aumentada a su forma escalonada reducida. Este método es una extensión del método de Gauss, y a menudo se le considera una mejora de este último.

La eliminación gaussiana, utilizada en la primera etapa del método de Gauss-Jordan, consiste en aplicar operaciones elementales de fila a la matriz aumentada para convertirla en una forma escalonada. Estas operaciones incluyen intercambiar filas, multiplicar filas por escalares y sumar o restar múltiplos de una fila a otra.

Una vez que la matriz aumentada está en forma escalonada, la segunda etapa del método de Gauss-Jordan, la eliminación de Gauss-Jordan, continúa aplicando operaciones elementales de fila para llevar la matriz a su forma escalonada reducida. Esto implica convertir todos los elementos debajo y encima de los pivotes en cero, lo que resulta en una matriz en la que la matriz de coeficientes se convierte en la matriz identidad y el vector de términos independientes se convierte en la solución del sistema de ecuaciones lineales.
### Algoritmo
1. Ir a la primera columna número cero de izquierda a derecha.
2. Si la primera fila tiene un cero en esta columna, intercambiarlo con otra que no lo tenga.
3. Luego, obtener ceros debajo de este elemento delantero, sumando múltiplos adecuados del renglón superior a los renglones debajo de él.
4. Cubrir el renglón superior y repetir el proceso anterior con la submatriz restante. Repetir con el resto de los renglones (en este punto la matriz se encuentra en forma escalonada).
5. Comenzando con el último renglón no cero, avanzar hacia arriba: para cada renglón obtener 1 delantero e introducir ceros arriba de este sumando múltiplos correspondientes a los renglones correspondientes.
### Metodologia
2x+y-z=8

-3x-y+2z=-11

-2x+y+2z=-3

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-18%20212756.png)
### Ejemplos

------------

2x+y=0

6x+5y=-2

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-18%20212811.png)

------------

2x+3y=7

3x-2y=4

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-18%20212821.png)

------------

2x+3y=20

-2x+y=4

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-18%20212832.png)
