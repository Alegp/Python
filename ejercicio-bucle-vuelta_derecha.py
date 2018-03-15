# coding: utf8
#Alejandro García Ponce

# Inicializaciones
salir  = "N"
suma   = 1

while ( salir=="N" ):
        # Hago cosas
        if (suma%8==1) or (suma%8==2):
           print suma , "-> Arriba"
        if (suma%8==3) or (suma%8==4):
           print suma , "-> Derecha" 
        if (suma%8==5) or (suma%8==6):
           print suma , "-> Abajo" 
        if (suma%8==7) or (suma%8==0):
           print suma , "-> Izquierda" 
        # Incremento
        suma  = suma + 1
        # Activo indicador de salida si toca
        if ( suma > 8): # Condición de salida
            salir = "S"
