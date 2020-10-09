"""
6) Realizar un algoritmo que lea un número por teclado. En caso de que ese número
sea 0 o menor que 0, se saldrá del programa imprimiendo antes un mensaje de error.
Si es mayor que 0, se deberá calcular su cuadrado y la raiz cuadrada del mismo,
visualizando el numero que ha tecleado el usuario y su resultado (“Del numero X, su
potencia es X y su raiz X” ). Para calcular la raiz cuadrada se puede usar la función
interna RAIZ(X) o con una potencia de 0,5.
"""
from math import sqrt
A = float(input("Por favor Digite un número: "))

if A <= 0:
    print("************************ERROR****************************")
else:
    raiz = sqrt(A)
    potencia = A**2
    
    print("El número escogido fue el: "+ str(A))
    print("La raíz es:  "+ str(raiz))
    print("El cuadrado del número es: "+ str(potencia))