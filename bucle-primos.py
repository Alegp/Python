#coding: utf8
#Alejandro García Ponce
# Inicializaciones


salir = "N"
numero = 7
modulo = numero
aciertos = 0

while ( salir=="N" ):
    # Hago cosas
    if (numero%modulo==0):
		aciertos = aciertos + 1
    # Incremento
    modulo = modulo -1
    # Activo indicador de salida si toca
    if (modulo < 1): # Condición de salida
		salir = "S"

if (aciertos == 2):
	print ("Es primo. Aciertos: "), aciertos
else:
	print ("No es primo. Aciertos: "), aciertos
