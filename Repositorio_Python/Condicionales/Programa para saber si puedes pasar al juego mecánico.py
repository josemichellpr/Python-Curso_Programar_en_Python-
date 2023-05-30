print ("Insertarás tu altura y peso")
print ("Pero si no mides mas de 1.3 m")
print ("O pesas más de 40.5 kg, NO PODRAS INGRESAR ")
altura = float (input("Dame tu altura: "))
peso = float (input("Dame tu peso: "))

if  altura > 1.3 or peso > 40.5:
    print ("Pásale")
else :
    print ("Suerte a la próxima")