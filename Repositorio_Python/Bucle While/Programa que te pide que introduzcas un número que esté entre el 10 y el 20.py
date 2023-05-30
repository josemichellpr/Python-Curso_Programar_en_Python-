"""
Programa que te pide que introduzcas un número que esté
entre el 10 y el 20. Si es correcto te diga que estás
en el rango, y te pida otro. Hasta que le des un número
fuera del rango y se acabe el programa.
"""
print ("Dame un número y siempre y cuando esté entre el 10 y 20")
print ("te pediré otro, de lo contrario se termina el programa")
print (" ")

numero = 10
while 10 <= numero <= 20:
    numero = float(input("Dame un número: "))
    print ("Bien. Una vez más")
print ("Se terminó. El número dado está fuera del rango")
