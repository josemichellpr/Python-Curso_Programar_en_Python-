"""
RULETA DE LOS COLORES
(utilizar lista y "bandera" lógica)
"""

print ("*** RULETA DE LOS COLORES ***")
print ("Si atinas a uno de mis colores,guardados en mi memoria ")
print ("te doy un punto, de lo contrario se termina el juego.")

clrs_mem = ['rojo', 'amarillo', 'verde', 'azul', 'morado']
puntaje = 0
n = 0
entrando = True
color = input("Dame un color: ")

while entrando:
    if color in clrs_mem[0:len(clrs_mem)]:
        puntaje +=1
        print ("Bien hecho.Tu puntaje es: ", puntaje)
        print("")
        color = input("Dame un color: ")

    else:
        entrando = False
        
   

else:
    print ("Ese color no está en mi memoria. Se terminó")
    print ("Tu puntaje es: ", puntaje)