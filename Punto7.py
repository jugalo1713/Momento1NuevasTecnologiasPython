"""
7) Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el
curso actual. Diseñar un algoritmo para este propósito (recuerda que para calcular el
porcentaje puedes hacer una regla de 3).
"""

a = float(input("Por favor confirmar cuantos niños hay en la escuela "))
b = float(input("Por favor confirmar cuantos niñas hay en la escuela "))

total = a+b
porcNinos = a * 100  / total
porcNinas = b * 100  / total

print("El total de alumnos es "+ str(total))
print("El porcentaje de niños es: " + str(porcNinos)+"%")
print("El porcentaje de niños es: " + str(porcNinas)+"%")