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
7. Resolver el sistema de ecuaciones.
8. Fin.
