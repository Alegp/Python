#coding: utf8

# Inicializaciones
salir = "N"
anyo = 2001

while ( salir=="N" ):
		# Hago cosas
		print anyo

		# Incremento
		anyo = anyo + 1
		# Activo indicador de salida si toca
		if ( anyo >=2017 ): # Condición de salida
			salir = "S"
