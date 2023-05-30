"""
PROGRAMA QUE TE DICE LAS VOCALES Y LAS CONSONANTES
QUE TIENE UNA PALABRA QUE INTRODUZCA EL USUARIO"""

n = 0
ov = 0
oc = 0
entrando = True
vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
palabra = input ("Dame una palabra: ")
longitud = len (palabra)

while entrando:
    if n == longitud:
        entrando = False
    elif palabra[n] in vocales:
        ov +=1
    elif palabra[n] not in vocales:
        oc+=1

    n+=1

else:
    print ("El número de vocales es: ", ov)
    print ("El número de consonantes es: ", oc)