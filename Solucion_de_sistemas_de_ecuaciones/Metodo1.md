# Metodo 1: Gauss
### Definicion
La eliminación gaussiana es un algoritmo que permite resolver un sistema de ecuaciones lineal. Consiste en una secuencia de operaciones realizadas sobre las matrices de los coeficientes de dichas ecuaciones.
Este algoritmo aparece por primera vez en el libro «Los nueve capítulos de el arte matemático«, un libro realizado por varias generaciones de estudiosos en China entre los siglos I y II AC.
Carl Friedrich Gauss desarrollo en 1810 una notación para la eliminación simétrica que fue adoptada en el siglo IX por las llamadas «computadoras humanas» para resolver los problemas de mínimos cuadrados  en ecuaciones normales. Finalmente el algoritmo comenzó a llamarse solamente por el nombre de Gauss.
### Algoritmo
1. Convertir el sistema de ecuaciones en matriz.
2. Hallar el pivote, se inicia desde el primer valor de la primera fila de la primera columna de la raiz.
3. Transformar el  valor del pivote en 1, multiplicando la inversa del valor del pivote (en caso que sea cero sumarle 1).
4. Convertir todos los valores inferiores de la misma fila del pivote en cero, sumandole su inverso aditivo por el valor superior de la columna del pivote.
5. Pasar a la siguiente fila y la siguiente columna del pivote seleccionado y repetir el paso 3 hasta que se llegue a la ultima columna de la matriz.
6. Convertir la matriz en un sistema de ecuaciones.
7. Resolver el sistema de ecuaciones de abajo asía arrriba.
8. Fin.
### Metodologia
Queremos resolver el siguiente sistema de ecuasiones:
x-y+z=2
x-2y+z=7
x-y=-2
![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%205.png)
### Ejemplos

------------

2x+3y=8
4x-2y=2
![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-18%20190843.png)

------------

x+y=1
-x+y=0

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-18%20190853.png)

------------

3x+2y=4
5x-4y=6
![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Captura%20de%20pantalla%202024-03-18%20190900.png)
