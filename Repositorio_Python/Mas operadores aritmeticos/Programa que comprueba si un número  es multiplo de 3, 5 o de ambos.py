""" Programa que comprueba si un número  es multiplo de 3, 5 o de ambos
"""

print ("Este programa te ayudará a determinar si un número")
print ("es multiplo de 3, 5 o de ambos")
print ("")
# Para saber si un número es multiplo de 3, si al dividirlo por 3
#su residuo es cero, es multiplo de 3.
#Si al dividirlo por 5, su residuo es cero. Es multiplo de 5
#Desde mi entendimiento, si es divisible por ambos es porque
#al dividirlo por 15, su residuo es cero. 

numero = float (input("Dame el número: "))
if numero == 0:
    print ("No jodas")
elif numero%15 == 0:
    print (numero, "Es un multiplo tanto de 3 como de 5.")
elif numero%5 == 0:
    print (numero, "Es un multiplo de 5.")
elif numero%3 == 0:
    print (numero, "Es un multiplo de 3.")
else:
    print (numero, "NO es multiplo de 3, 5 o ambos. BYE")