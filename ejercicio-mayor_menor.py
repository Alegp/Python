#coding: utf8

variableA = input ("Escribe un numero: ")
variableB = input ("Escribe un numero diferente: ")
variableC = input ("Escribe un numero diferente: ")

if (variableA == variableB) or (variableA == variableC) or (variableB == variableC):
	print "Error: numero repetido"
else:
    if (variableA > variableB) and (variableA > variableC):
		if (variableB > variableC):
			print "Mayor variableA ,Menor variableC"
		else:
		    print "Mayor variableA ,Menor variableB"
    else:
	    if (variableB > variableA) and (variableB > variableC):
		    if (variableA > variableC):
			    print "Mayor variableB ,Menor variableC"
		    else:
		        print "Mayor variableB ,Menor variableA"
	    else:
	        if (variableC > variableA) and (variableC > variableB):
		        if (variableA > variableB):
			       print "Mayor variableC ,Menor variableB"
		        else:
		            print "Mayor variableC ,Menor variableA"
	        else:
	            pass
