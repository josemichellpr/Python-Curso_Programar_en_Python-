"""Programa que suma números pares, hasta cierto límite, definido por el usuario."""

print ("Este es un programa chido que te obtiene")
print ("la sumatoria de un número PAR")
print ("p/e : si me pides la sumatoria hasta el 6")
print ("Yo te entregaría 2 + 4 + 6 = 12")
limite = float(input ("Dime el límite de la sumatoria: "))

#Lo que recomienda el profe es que en vez de declarar
#con numeros, mejor con caracter, por si el usuario
#se equivoca, no se interrumpa abruptamente el programa.
if limite%2 == 0:
    contador = 0
    suma = 0
    while contador < limite + 2:
        suma =  suma + contador
        contador = contador + 2
    else:
        print ("La sumatoria es: ", suma)
else:
    print ("Te dije que solo números pares bro")
    limite = float(input ("Dime el límite de la sumatoria: "))
    while (limite % 2) != 0:
        limite = float(input ("Dime el límite de la sumatoria: "))
        
    contador = 0
    suma = 0   
    while contador < limite + 2:
                suma =  suma + contador
                contador = contador + 2
    else:    
                print ("La sumatoria es: ", suma)