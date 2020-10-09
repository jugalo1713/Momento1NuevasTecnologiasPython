"""
10) Modificar el algoritmo anterior, de forma que si se teclea un cero, se vuelva a pedir
el número por teclado (así hasta que se teclee un número mayor que cero) (recuerda
la estructura mientras).
"""



a = int(input("Por favor ingresar un número: "))

while a == 0:
    a = int(input("Por favor ingresar un número que no sea 0: "))

if a %2 ==0:
    print("El número es par")
elif a%2 != 0:
    print("El número es impar")
else:
    print("escriba un número correcto")