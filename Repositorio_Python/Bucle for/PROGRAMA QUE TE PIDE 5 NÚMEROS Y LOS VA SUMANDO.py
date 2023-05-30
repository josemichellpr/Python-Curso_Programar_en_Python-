"""
PROGRAMA QUE TE PIDE 5 NÚMEROS Y LOS VA SUMANDO.
AL FINAL TE MUESTRA EL RESULTADO
"""

suma = 0
for i in range (1,6):
    numero = int(input ("Dame un número: "))
    suma = suma + numero
print (suma)