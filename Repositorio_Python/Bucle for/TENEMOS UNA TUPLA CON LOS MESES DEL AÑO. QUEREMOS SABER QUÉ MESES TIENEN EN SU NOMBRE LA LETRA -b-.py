"""
TENEMOS UNA TUPLA CON LOS MESES DEL AÑO. QUEREMOS SABER
QUÉ MESES TIENEN EN SU NOMBRE LA LETRA "b".
"""

meses = ("Enero", "Febrero", "Marzo","Abril","Mayo","Junio",
         "Julio","Agosto","Septiembre","Octubre","Noviembre",
         "Diciembre")

for n in range (0,12):
    if "b" in meses[n]:
        print(meses[n])