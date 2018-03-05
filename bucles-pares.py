#coding: utf8

# Inicializaciones
salir = "N"
numero = 2
peticion = input("Escriba el numero limite: ")

if peticion <= 1:
	print "Error: No se puede 1 o negativos"
else:
	while ( salir=="N" ):
		# Hago cosas
	    print numero

		# Incremento
	    numero = numero + 2
		# Activo indicador de salida si toca
	    if ( numero > peticion ): # Condición de salida
            salir = "S"
