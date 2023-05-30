"""
PROGRAMA QUE PIDE UN NÚMERO AL USUARIO. SI ESE NÚMERO
MÁS ALGÚN NÚMERO DE UNA LISTA DADA ES IGUAL A 100,
EL PROGRAMA DICE QUE EL NÚMERO CUMPLE LA CONDICIÓN
"""

lista = [28,36,43,52,61,75,84,97]
numero = int (input("Dame un número: "))
enter = False

for i in lista:
    if numero + i == 100:
        enter = True

if enter == True:
    print ("El número SI cumple con las condiciones")
else:
    print ("El número NO cumple con las condiciones")
