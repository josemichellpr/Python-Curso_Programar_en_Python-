print ("En este programa se te pedirán 2 números que sumados deben resultar 10")
print ("¿Estás listo?")

numero_1 = float(input("Dame el primer número: "))
numero_2 = float(input("Dame el segundo número: "))

suma = numero_1 + numero_2

if suma > 10:
    print("Has fallado, la suma es igual a ", suma, ", que es mayor que 10.")

if suma < 10:
    print("Has fallado, la suma es igual a ", suma, ", que es menor que 10.")

if suma == 10:
    print ("EXITO")

print ("FIN DEL PROGRAMA. ADIOS")