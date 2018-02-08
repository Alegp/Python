#coding: utf8

numero = input ("Indica un numero: ")

if ((numero % 2 == 0) or ((numero >= -10) and (numero <= 40)) or (numero < 0)):
	print "Numero valido"
else:
	print "Numero invalido"
