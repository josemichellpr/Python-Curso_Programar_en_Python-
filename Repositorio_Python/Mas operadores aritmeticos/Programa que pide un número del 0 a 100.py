""" Programa que pide un número del 0 a 100 y
comprueba si introduces un número correcto.
"""
print ("Este es un programa en el que introduces un número del 0 al 100")
print (" y si el número introducido NO está en ese rango, te lo digo")
print (" ")

numero = float(input("Dame el número: "))
if 0 <= numero <= 100:
    print ("Muy bien")
else:
    print ("Vuelve a intentarlo")