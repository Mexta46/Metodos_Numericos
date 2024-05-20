def lagrange_interpolation(x, y, x_eval):
    n = len(x)
    p = 0
    
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_eval - x[j]) / (x[i] - x[j])
        p += term
    
    return p

# Ejemplo de uso
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
x_eval = 2.5

result = lagrange_interpolation(x, y, x_eval)
print(f"El valor interpolado en x={x_eval} es: {result}")