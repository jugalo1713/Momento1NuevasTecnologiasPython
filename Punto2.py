
"""
2) Algoritmo que lea dos números, calculando y escribiendo el valor de su suma, resta,
producto y división.
"""

A = float(input("Cual es el valor de A: "))
B = float(input("Cual es el valor de B: "))
suma = A + B
resta = A-B
multip = A * B


print("Le confirmo que escribió el número "+str(A)+" y posteriormente "+str(B))
print("La suma es = "+str(suma))
print("La resta es = "+str(resta))
print("La multiplicación es = "+str(multip))

if B == 0:
    print("El segundo número no puede ser 0 (Cero), escriba otro")
else:
    div = A / B
    print("La división es = "+str(div))