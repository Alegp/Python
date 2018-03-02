#coding: utf8

# Inicializaciones
salir = "N"
numero = 1

while ( salir=="N" ):
    # Hago cosas
    print numero

    # Incremento
    numero = numero + 1
    # Activo indicador de salida si toca
    if ( numero > 50 ): # Condición de salida
            salir = "S"
