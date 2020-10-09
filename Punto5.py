"""
5) Diseñar un algoritmo que pida por teclado tres números; si el primero es negativo,
debe imprimir el producto de los tres y si no lo es, imprimirá la suma.

"""

A = float(input("Por favor Digite un número: "))
B = float(input("Por favor digite un segundo número: "))
C = float(input("Por favor digite un tercer número: "))

print("Le confirmo que escribió el número "+str(A)+", posteriormente "+str(B)+ " y por último el "+ str(C))

if A < 0:
    producto = A * B * C
    print("El producto es: " + str(producto))
else:
    suma = A+B+C
    print("La suma  es: " + str(suma))