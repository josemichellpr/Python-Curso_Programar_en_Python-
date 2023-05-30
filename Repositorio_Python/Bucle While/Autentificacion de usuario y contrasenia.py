"""
Programa que te pide tu usuario y contraseña (AMBAS)
si estas no son correctas, te las pedirá de nuevo """

usuario = input ("Ingresa tu usuario")
usuario_conf = input ("Confirma tu usuario")
password = input ("Ingresa tu contraseña")
password_conf = input ("Confirma tu contraseña ")

while usuario != usuario_conf or password != password_conf:
    print ("La contraseña y/o usuario NO coinciden, inténtentalo de nuevo")
    usuario = input ("Ingresa tu usuario")
    usuario_conf = input ("Confirma tu usuario")
    password = input ("Ingresa tu contraseña")
    password_conf = input ("Confirma tu contraseña ")

print ("CONTRASEÑAS REGISTRADAS")