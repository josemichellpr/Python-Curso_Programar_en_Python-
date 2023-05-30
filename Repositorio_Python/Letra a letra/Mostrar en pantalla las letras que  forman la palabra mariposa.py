"""
Mostrar en pantalla las letras que 
forman la palabra "mariposa".
"""

n = 0
entrando = True
hola = "mariposa"
numero = len (hola)
while entrando:
    if n == numero + 1:
        entrando = False
    elif n < numero:
        print("mariposa"[n])
        n += 1
