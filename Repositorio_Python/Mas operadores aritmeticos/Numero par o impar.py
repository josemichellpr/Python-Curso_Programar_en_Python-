""" Programa que comprueba si un número dado es par o impar
"""

print ("Este programa te ayudará a determinar si un número es par o impar")
print ("")
# Para saber si un número es par, es sencillo. Si al dividirlo por 2
#su residuo es cero. Es un número par, de lo contrario (tiene residuo), es impar.

numero = float (input("Dame el número: "))
if numero == 0:
    print ("No jodas")
elif numero%2 == 0:
    print ("Es un número par. De nada")
else:
    print ("Es un número impar")
