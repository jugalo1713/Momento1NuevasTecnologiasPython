"""
9) Realizar un algoritmo que dado un número entero, visualice en pantalla si es par o
impar. En el caso de ser 0, debe visualizar “el número no es par ni impar” (para que un
numero sea par, se debe dividir entre dos y que su resto sea 0)

"""

a = int(input("Por favor ingresar un número: "))

if a == 0:
    print("El número no es ni par ni impar ")
elif a %2 ==0:
    print("El número es par")
elif a%2 != 0:
    print("El número es impar")
else:
    print("escriba un número correcto")