"""
PROGRAMA QUE COMPRUEBA CUÁNTAS VECES ESTÁ
UN NÚMERO EN UNA LISTA DADA
"""

lista = [28,36,43,52,61,43,75,84,43,97]
numero = int(input("Dame un número: "))
suma = 0
for i in lista:
    if numero == i:
        suma +=1
print("El número", numero, "está en mi memoria", suma, "veces")
