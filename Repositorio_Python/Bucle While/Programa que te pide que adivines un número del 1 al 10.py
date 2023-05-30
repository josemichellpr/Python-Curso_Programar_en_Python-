"""
Programa que te pide que adivines un número del 1 al 10
y te pida números constantemente hasta que lo adivines.
Añade un contador que te diga los intentos que has necesitado.

Conviene que crees tres variables, y utiliza un "else" 
"""

print ("Te pediré que adivines el número que tengo guardado en mi memoria")
incognita = 9
veces = 0
numero = int(input("Dame el número: "))

while numero != incognita:
    veces = veces + 1
    print ("No has acertado. Intento número ", veces)
    numero = int(input("Dame el número: "))

if numero == incognita and veces == 0:
    print ("Lo has resuelto al primer intento")

if numero == incognita:
    veces = veces + 1
    print ("Felicidades, lo has logrado al intento # ", veces)
