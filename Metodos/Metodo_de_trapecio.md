# Regla del trapecio
## Definición
La regla del trapecio es un método de aproximación numérica utilizado para estimar el valor de una integral definida. Consiste en aproximar el área bajo una curva mediante el área de trapecios formados por segmentos rectos. La regla del trapecio se basa en dividir el intervalo de integración en pequeños segmentos y aproximar el área bajo la curva en cada segmento con un trapecio cuya base superior coincide con el valor de la función en un extremo del segmento y cuya base inferior coincide con el valor de la función en el otro extremo. La suma de las áreas de estos trapecios proporciona una aproximación al valor de la integral.
## Algoritmo
1. Definir el intervalo de integración [a, b] y el número de subintervalos n en los que se dividirá el intervalo.
2. Calcular el ancho de cada subintervalo: h = (b - a) / n
3. Evaluar la función en los puntos extremos del intervalo (a y b) y en los puntos intermedios (xi = a + i*h, donde i = 1, 2, ..., n-1).
4. Calcular la aproximación de la integral definida utilizando la fórmula del trapecio: Integral aproximada = (h/2) * (f(a) + 2*[f(x1) + f(x2) + ... + f(xn-1)] + f(b)) Donde f(a), f(b) y f(xi) son los valores de la función evaluada en los puntos correspondientes.
5. Cuantos más subintervalos se tomen (es decir, mayor sea n), más precisa será la aproximación de la integral.
## Metodología
```python
fun = ""
def f(x):
    try:
        # Evalúa la expresión algebraica y devuelve el resultado
        expresion = fun.replace("x", f"{x}")
        expresion2 = expresion.replace("^", "**")
        expresion3 = expresion2.replace("e", "2.71828")
        resultado = eval(expresion3)
        return resultado
    except Exception as e:
        print("La expresion esta mal, tienes que usar la variable x dentro de la expresion y cada vez que tienes que mutiplicar un numero con una variable tienes que usar *, por ejemplo 3*x^2")
        return None
def trapecio(a, b, n):
    h = (b - a) / n
    if f(a) == None:
        return None
    suma = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        suma += 2 * f(x)
    integral = (h / 2) * suma
    return round(integral, 2)
fun = input("Ingresa la expresion algebraica con la variable x y usando el signo de multiplicacion para cada variable x que se multiplica con un numero:")
try:
    a = float(input("Ingresa el limite inferior:"))
    b = float(input("Ingresa el limite superior:"))
    n = int(input("Ingresa la cantidad de iteraciones a usar:"))
    resultado = trapecio(a, b, n)
    if(resultado!=None):
        print(f"La aproximación de la integral definida en el intervalo [{a}, {b}] con {n} subintervalos es: {resultado}")
    else:
        print("Los datos que ingresaste son incorrectos")
except Exception as e:
    print("Los datos que ingresaste son incorrectos")
```

## Ejemplos
1. integral de 3x con los limites [1,2]
