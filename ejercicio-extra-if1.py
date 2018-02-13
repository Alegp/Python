#coding: utf8

dividendo = input ("Escriba el dividendo: ")
divisor   = input ("Escriba el divisor: ")

cociente = dividendo // divisorç
resto    = dividendo % divisor

if divisor == 0:
    print "No se puede dividir por 0"

if dividendo % divisor == 0:
    print ("La division es exacta. Cociente: ", cociente)
else:
    print ("La division no es exacta. Cociente: ", cociente, ". Resto: ", resto)
