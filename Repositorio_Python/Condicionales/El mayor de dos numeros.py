print("En este programa se te pedirán dos números cualesquiera diferentes entre sí y ")
print ("el mismo programa te dirá cual de los dos números es mayor")
print ("")#Aquí dejo este print, para que NO este encimado.
numero_1 = float(input("Dame el primer número: "))
numero_2 = float(input("Dame el segundo número: "))

if numero_1 > numero_2:
    print (numero_1, "  MAYOR que ", numero_2, ".")
else:
    print (numero_2, "  MAYOR que ", numero_1, ".")
