"""
PROGRAMA QUE TE PIDE CONTRASEÑAS Y SI NO COINCIDEN
TE REGRESA HASTA QUE SE LAS DES BIEN.
"""

password = input("Dame tu contraseña: ")
password_2 = input("Confirma tu contraseña: ")

while password != password_2:
    password_2 = input("Confirma tu contraseña: ")

input("Contraseñas guardadas")