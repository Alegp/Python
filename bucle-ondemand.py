#coding: utf8

# Inicializaciones
salir = "N"
numero = 1
peticion = input("Escriba el numero limite: ")

if peticion <= 0:
	print "Error: No se puede 0 o negativos"
else:
	while ( salir=="N" ):
		# Hago cosas
		print numero

		# Incremento
		numero = numero + 1
		# Activo indicador de salida si toca
		if ( numero > peticion ): # Condición de salida
				salir = "S"
