# coding: utf8

# Inicializaciones
salir  = "N"
suma   = 1
maximo = input ("Indique un numero:") 
sumaTotal  = 0

if maximo <= 0 :
	print "Error 404"

while ( salir=="N" ):
	# Hago cosas
	print suma

	# Incremento
	sumaTotal = suma + sumaTotal
	suma  = suma + 1
	# Activo indicador de salida si toca
	if ( suma > maximo): # Condición de salida
		print sumaTotal
		salir = "S"
