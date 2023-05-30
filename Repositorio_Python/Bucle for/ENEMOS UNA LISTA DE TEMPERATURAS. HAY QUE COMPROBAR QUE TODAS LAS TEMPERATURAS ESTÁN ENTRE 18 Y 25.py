"""
TENEMOS UNA LISTA DE TEMPERATURAS. HAY QUE COMPROBAR QUE
TODAS LAS TEMPERATURAS ESTÁN ENTRE 18 Y 25 INCLUIDOS.
SI ALGUNA NO CUMPLE LA CONDICIÓN SE PARA EL PROGRAMA Y
LO INDICA, SINO VA MOSTRANDO QUE LA TEMPERATURA VERIFICADA
ES CORRECTA.
"""

temperaturas = [19,22,21,24,23,27,21,20,19,18,21,20]

for n in temperaturas:
    if 18 <= n <= 25:
        print(n)
    else:
        print("Se ha detenido el programa, ya que",n,)
        print("no cumple los requisitos de temperatura.")
        break