#coding: utf8

import os
os.system("clear")
from math import pi

print """
       Selecciona una forma:
           a) Triangulo
           b) Circulo
"""

forma=raw_input ("Indica una forma: ")

if (forma != "a") and (forma != "b"):
	print "Error: esa opcion no existe"

if (forma == "a"):
	base = input ("Indica la base: ")
	altura = input ("Indica la altura: ")
	print "Un triangulo de base", base, "y de altura", altura, "tiene un area de", ((base*altura)/2)
else:
	radio = input ("Indica el radio: ")
	print "Un circulo de radio", radio, "tiene un area de", round(pi*radio*2,2)
