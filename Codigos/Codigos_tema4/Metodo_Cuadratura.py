
                    # Integración: Cuadratura de Gauss de dos puntos
                    # modelo con varios tramos entre [a,b]
import numpy as np    #bibliotecas a importar 
import matplotlib.pyplot as plt

                    # cuadratura de Gauss de dos puntos
def integraCuadGauss2p(funcionx,a,b):
    x0 = -1/np.sqrt(3)
    x1 = -x0
    xa = (b+a)/2 + (b-a)/2*(x0)
    xb = (b+a)/2 + (b-a)/2*(x1)
    area = ((b-a)/2)*(funcionx(xa) + funcionx(xb)) #se calcula el area
    return(area)        #retorna area

                    # INGRESO
fx = lambda x: np.sqrt(x)*np.sin(x)  

                    # intervalo de integración
a = 1                    #intervalo a
b = 3                    #intervalo b
tramos = 4                # numero de tramos

                    # PROCEDIMIENTO
muestras = tramos+1                #tramos 
xi = np.linspace(a,b,muestras)    
area = 0
for i in range(0,muestras-1,1):        # se declara un ciclo for
    deltaA = integraCuadGauss2p(fx,xi[i],xi[i+1])    # se calcula delta
    area = area + deltaA    #se suma el area y delta A
                    # SALIDA
print('Integral: ', area)