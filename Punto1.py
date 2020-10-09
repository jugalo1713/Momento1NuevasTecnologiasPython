

"""1) Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un
algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al
final las dos variables (recuerda la asignación). """


A = input("Cual es el valor de A: ")
B = input("Cual es el valor de B: ")
print("El valor de A es "+str(A)+ " y el valor de B es: "+ str(B))

C = A
A = B
B = C

print("Si intercambiamos los valores A quedaría: " + str(A)+ " y B quedaría: "+ str(B))
