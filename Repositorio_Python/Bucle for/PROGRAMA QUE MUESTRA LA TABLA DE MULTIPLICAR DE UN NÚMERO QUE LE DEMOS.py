"""
PROGRAMA QUE MUESTRA LA TABLA DE MULTIPLICAR
DE UN NÚMERO QUE LE DEMOS.
"""
num = int(input("Dame un número: "))
for n in range(1,11):
    print(num,"*",n,"= ",num * n)