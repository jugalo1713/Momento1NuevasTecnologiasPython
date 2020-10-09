"""
11) Algoritmo que nos diga si una persona puede acceder a cursar un ciclo formativo
de grado superior o no. Para acceder a un grado superior, si se tiene un titulo de
bachiller, en caso de no tenerlo, se puede acceder si hemos superado una prueba de
acceso.
"""

diploma = input("Confirme si o no en caso de que tenga un grado de bachiller: ")

if diploma.lower() == "si":
    print("Como tiene titulo bachiller Ud puede acceder a un ciclo formativo de grado superior")
elif diploma.lower() == "no":
    prueba = input("Confirme si ha hecho la prueba de acceso: ")
    if prueba.lower() == "si":
        print("Como no tiene grado bachiller pero si hizo la prueba de acceso Ud puede acceder a un ciclo formativo de grado superior")
    else:
        print("Como no tiene grado bachiller ni hizo la prueba de acceso Ud NO puede acceder a un ciclo formativo de grado superior")
else:
    print("Poner una respuesta valida")
