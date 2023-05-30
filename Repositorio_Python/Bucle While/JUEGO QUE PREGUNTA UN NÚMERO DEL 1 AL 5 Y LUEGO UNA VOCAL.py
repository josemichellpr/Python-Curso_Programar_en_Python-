"""JUEGO QUE PREGUNTA UN NÚMERO DEL 1 AL 5 Y LUEGO UNA VOCAL. TIENES 100 PUNTOS
"""
#SIN "BANDERA"
print ("Juego que pregunta un número del 1 al 5 y luego una vocal. Tienes 100 puntos,")
print (" si aciertas uno de ellos te quita 2 puntos, si no aciertas ninguno te quita ")
print ("5 puntos. El programa no se acaba hasta que aciertas los dos. Cuando se acaba")
print ("el programa te dice los puntos que te quedan")

num = input("Dame un número del 1 al 5: ")
vocal = input ("Dame una vocal: ")
x = input ("Confirma el número que capturaste: ")
y =  input ("Confirma la vocal que capturaste: ")
puntaje = 100
jugar = input ("Jugamos (si/no): ")
if jugar == "si":  
    while (not (num == x and vocal == y)):
        print ("Sin coincidencias")
        
        if num != x and vocal != y:
            puntaje = puntaje - 5
            
        else:
           puntaje = puntaje - 2

        x = input ("¿Cuál fue el número que capturaste?: ")
        y =  input ("Cuál fue la vocal que capturaste:")

    else:
        print ("Tu puntaje es: ",puntaje)


else:
    print ("BYE")


#CON BANDERA

print ("Juego que pregunta un número del 1 al 5 y luego una vocal. Tienes 100 puntos,")
print (" si aciertas uno de ellos te quita 2 puntos, si no aciertas ninguno te quita ")
print ("5 puntos. El programa no se acaba hasta que aciertas los dos. Cuando se acaba")
print ("el programa te dice los puntos que te quedan")

num = input("Dame un número del 1 al 5: ")
vocal = input ("Dame una vocal: ")
puntaje = 100
entrando = True

while entrando : #Aquí ya entramos por defecto, podemos solicitar entrada. Eso creo
    x = input ("¿Cuál fue el número que capturaste?: ")
    y =  input ("Cuál fue la vocal que capturaste:")
    if num == x and vocal == y:
        entrando = False
    elif num != x and vocal != y:
        puntaje = puntaje - 5
    else:
        puntaje = puntaje - 2
else :
    print ("Tu puntaje es: ",puntaje )