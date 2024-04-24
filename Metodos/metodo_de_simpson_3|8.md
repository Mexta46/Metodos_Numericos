# Metodo de Simpson

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/SIMPSON%206.png)

## Definicion

El método de Simpson 3/8 es un método numérico para aproximar la integral definida de una función en un intervalo dado. Este método es una extensión del método de Simpson 1/3, pero utiliza una fórmula más precisa para mejorar la aproximación.

La fórmula del método de Simpson 3/8 es la siguiente:

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/SIMPSON%207.png)

## Algoritmo

1. Empezar

2. Definir la función f(x)

3. Lea el límite inferior de integración, el límite superior de
   integración y número de subintervalo

4. Cálculos: tamaño del paso = (límite superior - límite inferior)/número de subintervalo

5. Establecer: valor de integración = f(límite inferior) + f(límite superior)

6. Establecer: i = 1

7. Si i > número de subintervalo, entonces vaya a

8. Calcular: k = límite inferior + i * h

9. Si mod 3 = 0 entonces
     Valor de integración = Valor de integración + 2* f(k)
   De lo contrario
     Valor de integración = Valor de integración + 3 * f(k)
   Terminara si

10. Incremente i en 1, es decir, i = i+1 y vaya al paso 7

11. Calcule: Valor de integración = Valor de integración * tamaño de paso*3/8

12. Mostrar el valor de integración como respuesta requerida

13. Detener

## Metodologia

```python
# Simpson's 3/8 Rule

# Define function to integrate
def f(x):
    return 1/(1 + x**2)

# Implementing Simpson's 3/8
def simpson38(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%3 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 3 * f(k)
    
    # Finding final integration value
    integration = integration * 3 * h / 8
    
    return integration
    
# Input section
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

# Call trapezoidal() method and get result
result = simpson38(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 3/8 method is: %0.6f" % (result) )
```

#EJEMPLOS

##Ejemplo 1

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/SIMPSON%208.png)

##Ejemplo 2

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/SIMPSON%209.png)

##Ejemplo 3

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/SIMPSON%2010.png)

##Ejemplo 4

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/SIMPSON%2011.png)

##Ejemplo 5

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/SIMPSON%2012.png)

