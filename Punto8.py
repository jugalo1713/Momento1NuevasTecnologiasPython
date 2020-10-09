"""
8) Una tienda ofrece un descuento del 15% sobre el total de la compra durante el mes
de octubre. Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar
al cliente.

"""

print("Por favor a continuación ingresar mes de venta, si no va ingresar más ventas poner el mes en 0 para terminar")
0
mes = int(input("Escriba el mes de la compra en números: "))
sumatoria = float(0)
sumatoriaDesc = float(0)

while mes != 0:
    
    valor = float(input("Indique el valor de la compra: "))
    if mes == 10:
        sumatoriaDesc = valor + sumatoriaDesc
        
    else:
        sumatoria = valor + sumatoria
        
    mes = int(input("Escriba el mes de la compra en números: "))

totDesc = sumatoriaDesc*0.85
total = sumatoria + totDesc


print("El total que incluye descuento "+ str(totDesc))
print("El total que no incluye descuento es: "+str(sumatoria))
print("El total comprado es: " + str(total) )



