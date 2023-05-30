""" Programa que obtiene el mayor de 3 números
"""

print ("Este programa te ayudará a obtener el mayor de 3 números")
print (" ")
#Creo que esto de obtener el mayor o menor de un conjunto de números
#en programación es como en un campeonato del deporte que tu quieras
#se enfrentan en pares y poco a poco se van eliminando entre ellos
#se van "midiendo" para ver cual es el mejor...
num_1 = float(input("Dame el 1er número: "))
num_2 = float(input("Dame el 2do número: "))
num_3 = float(input("Dame el 3er número: "))

if num_1 == num_2 == num_3:
    print ("Los números son iguales, no hay máximo, ni mínimo")
    
elif num_1 == num_2:
    if num_2 > num_3:
        print(num_2,"Es el número mayor del conjunto")
    else:
        print(num_3,"Es el número mayor del conjunto")
        
elif num_1 == num_3:
    if num_3 > num_2:
        print(num_3,"Es el número mayor del conjunto")
    else:
        print(num_2,"Es el número mayor del conjunto")

elif num_1 > num_3:
    if num_1 > num_2:
        print (num_1,"Es el número mayor del conjunto")
    else:
        print(num_2,"Es el número mayor del conjunto")

elif num_1 < num_3:
    if num_3 > num_2:
        print(num_3,"Es el número mayor del conjunto")
    else:
        print(num_2,"Es el número mayor del conjunto")
    