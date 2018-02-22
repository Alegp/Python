#coding: utf8
import os

os.system ("clear")

print """
********************************************************************************
		  <Menu de gasolinas> 
			1. Super/Normal 
			2. Super/Turbo 
			3. Sin plomo/Normal 
			4. Sin plomo/Con aditivos 
			5. Diesel/Normal 
			6. Diesel/Fast and Furius 
********************************************************************************"""

gasolina = input ("Seleccione su tipo de gasolina: ")

if (gasolina != 1) and (gasolina != 2) and (gasolina != 3) and (gasolina != 4) and (gasolina != 5) and (gasolina != 6):
	print "Error: seleccion no valida"
	exit

litros = input ("Seleccione la cantidad de litros: ")

if (litros == 0):
	print "Error: No se puede rellenar 0 litros"
	exit

if (gasolina == 1):
	print "Ha seleccionado Super/Normal. El importe total es", (litros * 1.5)
elif (gasolina == 2):
	print "Ha seleccionado Super/Turbo. El importe total es", (litros * 1.55)
elif (gasolina == 3):
	print "Ha seleccionado Sin plomo/Normal. El importe total es", (litros * 1.6)
elif (gasolina == 4):
	print "Ha seleccionado Sin plomo/Con aditivos. El importe total es", (litros * 1.65)
elif (gasolina == 5):
	print "Ha seleccionado Diesel/Normal. El importe total es", (litros * 1.7)
elif (gasolina == 6):
	print "Ha seleccionado Diesel/Fast and Furius. El importe total es", (litros * 1.75)
