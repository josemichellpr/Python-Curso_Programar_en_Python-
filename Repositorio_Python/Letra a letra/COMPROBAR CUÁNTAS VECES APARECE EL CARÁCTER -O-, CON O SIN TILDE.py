"""
COMPROBAR CUÁNTAS VECES APARECE EL CARÁCTER "O",
CON O SIN TILDE, EN LA SIGUIENTE CADENA DE CARACTERES
"""

n = 0
entrando = True
op = 0
hola = """Muchos años después, frente al pelotón de
fusilamiento, el coronel Aureliano Buendía había de
recordar aquella tarde remota en que su padre lo llevó
a reconocer el hielo"""
numero = len (hola)
while entrando:
    if n== numero + 1:
        entrando = False
    elif n < numero:
        if hola [n] == 'o' or hola [n] == 'ó':
            op += 1
    n+=1            
else:
    print ("Las veces que aparece o y ó en el texto es: ",op)