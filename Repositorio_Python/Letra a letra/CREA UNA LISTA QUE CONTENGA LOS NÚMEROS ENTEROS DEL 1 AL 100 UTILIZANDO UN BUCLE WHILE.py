""" CREA UNA LISTA QUE CONTENGA LOS NÚMEROS ENTEROS
DEL 1 AL 100 UTILIZANDO UN BUCLE WHILE, Y PARTIENDO
DE UNA LISTA VACÍA
"""
lista = []
n = 1
entrando = True

while entrando:
    if len(lista) ==  100:
        entrando = False
    else:
        lista += [n] 
    n+=1

else:
    print (lista)