print("Programa que te dice si:")
print ("Eres niño, joven, adulto o anciano")
#Declaramos la variable
#Y al mismo tiempo la requerimos
#Punto a favor Python vs C ++
edad = int(input("Dame tu edad: "))
#Lo que acabamos de hacer arriba es
#anidar las funciones, como en
#Mathematica
#Creo que desde este tipo de codigos
#ya necesitas diagramas de flujo
if edad < 14:
    print ("Eres un NIÑO")
elif 14 <= edad < 25:
    print ("Eres un JOVEN")
elif 25 <= edad < 70:
    print ("Eres un ADULTO")
elif 70 <= edad < 125 :
    print ("Eres ANCIANO")
else:
    print ("No me chingues, nadie a vivido tanto tiempo XD")
    print ("Y tampoco se puede tener edad cero o negativa")