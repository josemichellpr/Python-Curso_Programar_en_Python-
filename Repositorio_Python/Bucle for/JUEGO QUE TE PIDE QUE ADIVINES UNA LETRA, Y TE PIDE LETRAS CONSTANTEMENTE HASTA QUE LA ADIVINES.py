"""
JUEGO QUE TE PIDE QUE ADIVINES UNA LETRA, Y TE PIDE LETRAS
CONSTANTEMENTE HASTA QUE LA ADIVINES, Y ENTONCES SE PARA.
SE PUEDE PROBAR CON TODAS, MENOS CON LA "w", EN CUYO CASO
MUESTRA QUE ESA LETRA NO ESTÁ PERMITIDA Y SE PARA EL PROGRAMA.
"""

letra_adiv = "z"
letra = input ("Dame una letra: ")
#Este programa no deja avanzar si la letra es la prohibida (w)
while letra == "w" or letra == "W":
    print("La letra w no está permitida en este programa")
    letra = input ("Dame una letra: ")
    print("")
#Si la letra NO es w, pero tampoco z, entra al bucle y pide otra letra.
while letra != letra_adiv:
    print("Buen intento")
    letra = input ("Dame una letra: ")
    print("")
#Si la letra es z, sale del bucle y se termina el programa.
else:
    print("Has acertado.BYE")