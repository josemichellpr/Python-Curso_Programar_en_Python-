print("En este programa se te pedirá tu edad y la de un amigo ")
print("y el mismo programa, te dira cuál de los dos tiene más edad")

tu_edad = int(input("¿Cuál es TU edad? "))
edad_amigo = int(input("¿Cuál es la edad de tu amigo? "))

if tu_edad > edad_amigo:
    print ("Tu tienes más edad que tu amigo")
else:#Si no ocurre el condicional de arriba entonces deberá ocurrir uno de los 2
     #que está dentro del else.
    if tu_edad == edad_amigo:
        print ("Tu amigo y tú tienen la misma edad")
    else:
        print("Tu amigo es mayor que tú")
print ("")#Un espacio para que no se amontone mucho.
print ("FIN DEL PROGRAMA")