"""
4) Algoritmo que lea tres números distintos y nos diga cual de ellos es el mayor
(recuerda usar la estructura condicional Si y los operadores lógicos).
"""

A = float(input("Por favor Digite un número: "))
B = float(input("Por favor digite un segundo número: "))
C = float(input("Por favor digite un tercer número: "))

print("Le confirmo que escribió el número "+str(A)+", posteriormente "+str(B)+ " y por último el "+ str(C))

if A == B or A == C or B == C:
    print("Esta escribiendo números repetidos")
elif A > B and A > C:
    print("El número más alto fue el primero que es: "+ str(A))
elif B > A and B > C:
    print("El número más alto fue el Segundo que es: "+ str(B))
elif C > A and C > B:
    print("El número más alto fue el Tercero que es: "+ str(C))

else:
    print("Escriba un número valido")