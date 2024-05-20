def lagrange_interpolation(x_points, y_points, x_value):
    n = len(x_points)
    result = 0

    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term *= (x_value - x_points[j]) / (x_points[i] - x_points[j])
        result += term

    return result

def main():
    try:
        # Solicitar al usuario que ingrese los puntos
        num_points = int(input("Ingrese el número de puntos: "))
        if num_points <= 0:
            raise ValueError("El número de puntos debe ser mayor que cero.")

        x_points = []
        y_points = []

        for i in range(num_points):
            x = float(input(f"Ingrese x{i}: "))
            y = float(input(f"Ingrese y{i}: "))
            x_points.append(x)
            y_points.append(y)

        # Solicitar al usuario que ingrese el valor de x para evaluar el polinomio
        x_value = float(input("Ingrese el valor de x para evaluar el polinomio: "))
        result = lagrange_interpolation(x_points, y_points, x_value)
        print(f"El valor del polinomio en x = {x_value} es: {result}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
