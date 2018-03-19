# coding: utf8
#Alejandro García Ponce
# Inicializaciones
salir  = "N"
suma   = 1
maximo = 5
sumaTotal  = 0

if maximo <= 0 :
	print ("Error 404")

while ( salir=="N" ):
	# Hago cosas
	if (suma <= maximo-1):
		print (suma ,"+" ,)
	else:
		print (suma ,)
	# Incremento
	sumaTotal = suma + sumaTotal
	suma  = suma + 1
	# Activo indicador de salida si toca
	if ( suma > maximo): # Condición de salida
		print ("=", sumaTotal)
                    salir = "S"
