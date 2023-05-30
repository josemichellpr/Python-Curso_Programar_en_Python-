"""
PROGRAMA QUE MUESTRA SI LOS NÚMEROS DE UNA LISTA
SON POSITIVOS O NEGATIVOS, A EXCEPCIÓN DEL CERO
QUE SE LO SALTA.
"""

numeros = [1,4,-3,5,0,7,-2,6]

for n in numeros:
    if n == 0:
        #Pues que el cero no es + ni -.
        continue
    else:
        if n < 0:
            print(n, "es NEGATIVO")
        else:
            if n > 0:
                print(n,"es POSITIVO")
                
 # Es congruente este código con el mi diagrama de flujo,
 #aunque tambien se podía con elif.