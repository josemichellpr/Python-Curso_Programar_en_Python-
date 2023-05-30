"""
Programa que te pide que te inventes una contraseña y que
luego la repitas dos veces más.
Después comprueba que lo has hecho correctamente
"""
#El profe nos da a entender que la contraseña debe ser cualquier caracter. Ok

print ("Este es un programa que te pedirá que inventes una contraseña")
print ("Despues te pedirá que la confirmes dos veces")
print (" ")

password = input("Escribe una contraseña de puros caracteres: ")
password_1 = input (" Confirma la contraseña: ")
password_2 = input ("Confirma la contraseña una vez más:  ")

if password == password_1 == password_2:
    print ("Las contraseñas coinciden")
else:
    print ("Vuelve a intentarlo")