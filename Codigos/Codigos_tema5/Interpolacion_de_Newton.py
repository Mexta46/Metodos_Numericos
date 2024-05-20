def newton_interpolation(x, y, x_eval):
    n = len(x)
    divided_diffs = [[0 for j in range(n+1)] for i in range(n+1)]
    
    # Inicializar primera columna con los valores y
    for i in range(n):
        divided_diffs[i][0] = y[i]
    
    # Calcular las diferencias divididas
    for j in range(1, n+1):
        for i in range(n-j, -1, -1):
            if j == 1:
                divided_diffs[i][j] = (divided_diffs[i+1][j-1] - divided_diffs[i][j-1]) / (x[i+j] - x[i])
            else:
                divided_diffs[i][j] = (divided_diffs[i+1][j-1] - divided_diffs[i][j-1]) / (x[i+j] - x[i])
    
    # Evaluar el polinomio interpolante
    p = divided_diffs[0][0]
    for j in range(1, n+1):
        term = divided_diffs[0][j]
        for i in range(j):
            term *= (x_eval - x[i])
        p += term
    
    return p

# Ejemplo de uso
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
x_eval = 2.5

result = newton_interpolation(x, y, x_eval)
print(f"El valor interpolado en x={x_eval} es: {result}")