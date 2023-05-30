"""
PROGRAMA QUE SUMA LOS MÚLTIPLOS DE 3 EN UN RANGO DADO.
"""

print ("Este es un programa que te pedirá dos números y hara ")
print ("la sumatoria de todos aquellos que sean múltiplos de 3")
print (" ")
inf = int(input("Dame el primer número (extremo inferior del rango: "))
sup = int(input("Dame el segundo número (extremo superior del rango: "))
suma = inf

while suma < sup:
    if suma % 3 == 0:
        sumatri = suma
        contador = sumatri + 3
        while contador < sup  or contador == (sup + 3):
            sumatri = sumatri + contador
            contador = contador + 3
        else:
            suma = sumatri
            print (suma)
            
    else:
        suma = suma + 1

else:
    print("La sumatoria es igual ", suma)
