"""
PROGRAMA QUE PIDA UN NÚMERO ENTERO QUE ESTÉ EN EL
INTERVALO DEL 18 AL 25, Y QUE SIGA PIDIENDO NÚMEROS
MIENTRAS TE MANTENGAS EN EL INTERVALO

UTILIZA EL TIPO RANGE
"""
#No voy a declarar variable con el rango, para más facil.

num =int(input("Dame un número: "))

while num in range(18,26):
    print("El número está en el rango")
    num =int(input("Dame un número: "))
        
else:
    print ("Te has salido del rango")

#Al principio había utilizado "bandera", pero
#no siempre la "bandera" lo hace más sencillo