""" Programa que transforma un tiempo dado en segundos, en horas, minutos y segundos
correspondientes.

Introducir el dato 174452 segundos y nos tiene que dar 48 horas, 27 minutos
y 32 segundos """

# Lo importante es hacer el análisis, resolviendo varias veces el problema con diferentes cantidades
#para darte cuenta de la ruta crítica a seguir. Una vez detectada una o más rutas, establecer el camino óptimo.
print ("Me das el tiempo en segundos y yo te lo devuelvo desglosado en horas")
print ("minutos y segundos, respectivamente.")
print (" ")
tiempo_entrada = int(input("Dame el tiempo en segundos: "))
#HORAS
horas = tiempo_entrada//3600

residuo_segundos = tiempo_entrada % 3600 #Es el residuo de la división de arriba ("horas)

#MINUTOS
minutos = residuo_segundos // 60

#SEGUNDOS
segundos = residuo_segundos % 60
print (" ")
print ("horas: ", horas)
print ("minutos: ", minutos)
print ("segundos: ", segundos)