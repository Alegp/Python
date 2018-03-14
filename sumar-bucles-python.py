# coding: utf8

# Inicializaciones
salir  = "N"
suma   = 1
maximo = 5
sumaTotal  = 0

while ( salir=="N" ):
    # Hago cosas
    if (suma%2==0):
        print (suma , )
        if (suma <= maximo -1):
            print ("+", )
        # Incremento
        sumaTotal = suma + 1
    # Activo indicador de salida si toca
    if ( suma > maximo): # Condición de salida
        print ("=", sumaTotal)
        salir = "S"
