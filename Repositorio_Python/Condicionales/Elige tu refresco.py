print ("***REFRESCOS***")
print ("Elige tu refresco. Solo tengo cuatro tipos.5")
print("Coke (1), Pepsi (2), Manzana (3), TopoChico (4)")
eleccion = int(input(" Tu elección: "))

if eleccion == 1:
    print ("Toma tu Coke. Que lo disfrutes")
elif eleccion == 2:
    print ("Toma tu Pepsi. Que lo disfrutes")
elif eleccion == 3:
    print ("Toma tu Manzana. Que lo disfrutes")
    #Hay que recordar que con ELSE ya no hay necesidad de hacer igualaciones
    #Ahora utilizo ELSE cuando ya las demás posibilidades se agotaron. 
else:
    print ("Toma tu Topochico. Que lo disfrutes")
