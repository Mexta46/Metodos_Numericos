# Metodo de simpsom
## Definición
![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/simpson1.png)
El método de Simpson es una técnica de integración numérica que utiliza polinomios de segundo grado para aproximar el área bajo una curva. Se basa en dividir el área en segmentos y calcular una suma ponderada de los valores de la función en los extremos y en el punto medio de cada segmento.
## Algoritmo

1. f(x) que se desea integrar.
2. Especificar el intervalo de integración,[a,b].
3. Dividir el intervalo [a,b] en n subintervalos de igual tamaño, donde n es un número par.
4. Calcular el ancho de cada subintervalo, h=(b−a)/2.
5. Calcular los valores de la función f(x) en los extremos de los subintervalos: f(a),f(a+h),f(a+2h),…,f(b).
6. Calcular los valores de la función f(x) en los puntos medios de los subintervalos: f(a+((h)/2)), f(a+((3h)/2)), ... , f(b+((h)/2)).
7. Aplicar la fórmula de Simpson para calcular la aproximación de la integral:
![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/simpson2.png)
8. Devolver el valor calculado como la aproximación de la integral.


##Metodología 
```
<?php

// Definir la función a integrar
function f($x) {
    return /* Definir la función aquí */;
}

// Método de Simpson para aproximar la integral
function simpson($a, $b, $n) {
    // Calcular el ancho de cada subintervalo
    $h = ($b - $a) / $n;
    // Sumar el valor de la función en los extremos
    $sum = f($a) + f($b);
    
    // Calcular la suma de los valores de la función en los puntos medios
    for ($i = 1; $i < $n; $i++) {
        // Calcular el valor de x en el punto medio del subintervalo
        $x = $a + $i * $h;
        // Aplicar la regla de Simpson (ponderar por 2 o 4 según el índice)
        if ($i % 2 == 0) {
            $sum += 2 * f($x);
        } else {
            $sum += 4 * f($x);
        }
    }
    
    // Devolver el resultado de la aproximación de la integral
    return $h * $sum / 3;
}

// Intervalo de integración y número de subintervalos
$a = /* valor de 'a' */;
$b = /* valor de 'b' */;
$n = /* número de subintervalos (debe ser par) */;

// Calcular la aproximación de la integral
$result = simpson($a, $b, $n);

// Mostrar el resultado de la aproximación de la integral
echo "Aproximación de la integral: " . $result;

?>
```

##Ejemplos
