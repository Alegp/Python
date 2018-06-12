#Alejandro Garcia
#Los importes
import time
import sense_hat
from random import randint

#Colores de los pixeles
azul=(0,0,255)
red = (255,0,0)
nothing = (0,0,0)

#Asignaciones de sense
sense = sense_hat.SenseHat()
sense.clear()

#Mensaje de Hola inicial
sense.show_message("Hola")
sense.clear()
time.sleep(1)

# Valores del rey de la izquierda
fila_rey_1 = 2 #randint(0,7)
columna_rey_1 = 2 #randint(0,3)
#Valores del rey de la derecha
fila_rey_2 = 5 #randint (0,7)
columna_rey_2 = 5 #randint (4,7)
#Contador de publicidad
contador = 0

sense.set_pixel(columna_rey_1,fila_rey_1,azul)
sense.set_pixel(columna_rey_2,fila_rey_2,red)

time.sleep(1)

while True:
  #Decide el movimiento siguiente del rey de la izquierda
  movimiento_rey_1 = randint (1,8)
  #Decide el movimiento siguiente del rey de la derecha
  movimiento_rey_2 = randint (1,8)
  
  #Los movimientos posibles del rey de la izquierda
  #Movimiento 1 es hacia arriba
  if (movimiento_rey_1 == 1):
    if (fila_rey_1 == 0):
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
    else:
      sense.set_pixel(columna_rey_1,fila_rey_1,nothing)
      fila_rey_1 = fila_rey_1 - 1
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
  #Movimiento 2 es hacia abajo
  if (movimiento_rey_1 == 2):
    if (fila_rey_1 == 7):
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
    else:
      sense.set_pixel(columna_rey_1,fila_rey_1,nothing)
      fila_rey_1 = fila_rey_1 + 1
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
  #Movimiento 3 es hacia la izquierda
  if (movimiento_rey_1 == 3):
    if (columna_rey_1 == 0):
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
    else:
      sense.set_pixel(columna_rey_1,fila_rey_1,nothing)
      columna_rey_1 = columna_rey_1 - 1
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
  #Movimiento 4 es hacia la derecha
  if (movimiento_rey_1 == 4):
    if (columna_rey_1 == 3):
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
    else:
      sense.set_pixel(columna_rey_1,fila_rey_1,nothing)
      columna_rey_1 = columna_rey_1 + 1
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
  #Movimiento 5 es hacia arriba a la izquierda
  if (movimiento_rey_1 == 5):
    if (columna_rey_1 == 0) or (fila_rey_1 == 0):
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
    else:
      sense.set_pixel(columna_rey_1,fila_rey_1,nothing)
      columna_rey_1 = columna_rey_1 - 1
      fila_rey_1 = fila_rey_1 - 1
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
  #Movimiento 6 es hacia arriba a la derecha
  if (movimiento_rey_1 == 6):
    if (columna_rey_1 == 3) or (fila_rey_1 == 0):
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
    else:
      sense.set_pixel(columna_rey_1,fila_rey_1,nothing)
      columna_rey_1 = columna_rey_1 + 1
      fila_rey_1 = fila_rey_1 - 1
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
  #Movimiento 7 es hacia abajo a la izquierda 
  if (movimiento_rey_1 == 7):
    if (columna_rey_1 == 0) or (fila_rey_1 == 7):
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
    else:
      sense.set_pixel(columna_rey_1,fila_rey_1,nothing)
      columna_rey_1 = columna_rey_1 - 1
      fila_rey_1 = fila_rey_1 + 1
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
  #Movimiento 8 es hacia abajo a la derecha
  if (movimiento_rey_1 == 8):
    if (columna_rey_1 == 3) or (fila_rey_1 == 7):
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
    else:
      sense.set_pixel(columna_rey_1,fila_rey_1,nothing)
      columna_rey_1 = columna_rey_1 + 1
      fila_rey_1 = fila_rey_1 + 1
      sense.set_pixel(columna_rey_1,fila_rey_1,azul)
  
  
  #Los movimientos posibles del rey de la derecha
  #Movimiento 1 es hacia arriba
  if (movimiento_rey_2 == 1):
    if (fila_rey_2 == 0):
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
    else:
      sense.set_pixel(columna_rey_2,fila_rey_2,nothing)
      fila_rey_2 = fila_rey_2 - 1
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
  #Movimiento 2 es hacia abajo
  if (movimiento_rey_2 == 2):
    if (fila_rey_2 == 7):
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
    else:
      sense.set_pixel(columna_rey_2,fila_rey_2,nothing)
      fila_rey_2 = fila_rey_2 + 1
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
  #Movimiento 3 es hacia la izquierda
  if (movimiento_rey_2 == 3):
    if (columna_rey_2 == 4):
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
    else:
      sense.set_pixel(columna_rey_2,fila_rey_2,nothing)
      columna_rey_2 = columna_rey_2 - 1
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
  #Movimiento 4 es hacia la derecha
  if (movimiento_rey_2 == 4):
    if (columna_rey_2 == 7):
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
    else:
      sense.set_pixel(columna_rey_2,fila_rey_2,nothing)
      columna_rey_2 = columna_rey_2 + 1
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
  #Movimiento 5 es hacia arriba a la izquierda
  if (movimiento_rey_2 == 5):
    if (columna_rey_2 == 4) or (fila_rey_2 == 0):
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
    else:
      sense.set_pixel(columna_rey_2,fila_rey_2,nothing)
      columna_rey_2 = columna_rey_2 - 1
      fila_rey_2 = fila_rey_2 - 1
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
  #Movimiento 6 es hacia arriba a la derecha
  if (movimiento_rey_2 == 6):
    if (columna_rey_2 == 7) or (fila_rey_2 == 0):
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
    else:
      sense.set_pixel(columna_rey_2,fila_rey_2,nothing)
      columna_rey_2 = columna_rey_2 + 1
      fila_rey_2 = fila_rey_2 - 1
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
  #Movimiento 7 es hacia abajo a la izquierda 
  if (movimiento_rey_2 == 7):
    if (columna_rey_2 == 4) or (fila_rey_2 == 7):
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
    else:
      sense.set_pixel(columna_rey_2,fila_rey_2,nothing)
      columna_rey_2 = columna_rey_2 - 1
      fila_rey_2 = fila_rey_2 + 1
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
  #Movimiento 8 es hacia abajo a la derecha
  if (movimiento_rey_2 == 8):
    if (columna_rey_2 == 7) or (fila_rey_2 == 7):
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
    else:
      sense.set_pixel(columna_rey_2,fila_rey_2,nothing)
      columna_rey_2 = columna_rey_2 + 1
      fila_rey_2 = fila_rey_2 + 1
      sense.set_pixel(columna_rey_2,fila_rey_2,red)
  
  time.sleep(1)
  contador = contador + 1
  if (contador == 3):
    sense.show_message("...")
    contador = 0  sense.clear()
    time.sleep(1)
  
