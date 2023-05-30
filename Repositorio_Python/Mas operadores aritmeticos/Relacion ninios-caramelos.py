"""
Programa que dado un número de caramelos
y un número de niños, diga a cuántos caramelos
toca cada niño y cuantos caramelos hay """

infantes = int(input("¿Cuántos infantes hay? " ))
caramelos = int(input("¿Cuántos caramelos comprarás? " ))

print("A cada niño le corresponden ", caramelos//infantes)
print("Sobrarían ", caramelos%infantes)