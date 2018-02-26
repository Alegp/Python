#coding: utf8

valor1 = input ("Escriba un numero: ")
valor2 = input ("Escriba un numero: ")

if (valor1 == 0) or (valor2 == 0):
	print "Error: hay uno o mas ceros"
else:
	if (valor1 > valor2):
		mayor = valor1
		menor = valor2
	else:
		if (valor2 >= valor1):
			mayor = valor2
			menor = valor1
	if (mayor % menor == 0):
		print mayor, "es multiplo de", menor
	else:
		print mayor, "no es multiplo de", menor
