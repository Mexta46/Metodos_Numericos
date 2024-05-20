def Verificador(x, y):
    n = len(x)
    coeficiente = [0] * n
    for i in range(n):
        coeficiente[i] = y[i]
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            if x[i] == x[i-j]:
                raise ValueError(f"Los puntos x{i} y x{i-j} son idénticos, lo que causa una división por cero.")
            coeficiente[i] = (coeficiente[i] - coeficiente[i-1]) / (x[i] - x[i-j])
    return coeficiente

def newton_polynomial(x_val, x, coeficiente):
    n = len(x)
    result = coeficiente[0]
    for i in range(1, n):
        termino = coeficiente[i]
        for j in range(i):
            termino *= (x_val - x[j])
        result += termino
    return result


try:
    numP = int(input("Ingrese el número de puntos: "))
    if numP <= 0:
        raise ValueError("El número de puntos debe ser mayor que cero.")

    xP = []
    yP = []

    for i in range(numP):
        x = float(input(f"Ingrese x{i}: "))
        y = float(input(f"Ingrese y{i}: "))
        xP.append(x)
        yP.append(y)

    coeficiente = Verificador(xP, yP)
    print("Coeficientes del polinomio interpolante de Newton:", coeficiente)

    x_value = float(input("Ingrese el valor de x para evaluar el polinomio: "))
    result = newton_polynomial(x_value, xP, coeficiente)
    print(f"El valor del polinomio en x = {x_value} es: {result}")

except ValueError as e:
    print(f"Error: {e}")