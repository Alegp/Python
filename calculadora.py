#coding: utf8

num1 = input ("EScribe un numero:")
operacion = raw_input ("Escribe un operador: ")
num2 = input ("Escribe un numero: ")

if not( (operacion == "+") or (operacion == "-") or (operacion == "*") or (operacion == "/") ):
	print "Error: no has indicado un operador valido"
	exit

if (operacion == "+"):
	print "El resultado es", (num1+num2)
else:
    if (operacion == "-"):
        print "El resultado es", (num1-num2)
    else:
        if (operacion == "*"):
            print "El resultado es", (num1*num2)
        else:
			if (operacion == "/"):
				print "El resultado es" (num1/num2)
