"""
PROGRAMA QUE COMPRUEBA SI UN ELEMENTO ESTÁ EN UNA LISTA
Y NOS DICE EN QUÉ POSICIÓN (indice)se encuentra.
"""

lista = [2,5,90,23,45,87,54,11,38]
num = int(input("Dame un número: "))
if num not in lista:
    print ("El número",num,"no está en la lista")
else:
    for n in range (0,len(lista)):
        if num == lista[n]:
            print("El número",num,"se encuentra en la posición",n+1,"de esta lista")
