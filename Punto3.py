"""
3) Algoritmo que lea dos números y nos diga cual de ellos es mayor o bien si son
iguales (recuerda usar la estructura condicional SI)

"""

A = float(input("Por favor Digite un número: "))
B = float(input("Por favor digite un segundo número: "))


if A > B:
    print("El número más alto es " + str(A))
elif B > A:
    print("El número más alto es " + str(B))
elif B == A:
    print("Los dos números son iguales ")
else:
    print("Ingrese un número valido")