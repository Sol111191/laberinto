# -*- coding: utf-8 -*-
'laberinto con jugador'
'Nombre: Soledad Colque Iquise '

import random

def crearMapaLaberinto(numeroFilas, numeroColumnas, numeroParedes, numeroEspacios, numeroJugador):
    #crear mapa lleno de paredes
    mapaLaberinto = []
    numeroParedesGeneradas = 0
    for fila in range(0, numeroFilas):
        filaMapaLaberinto = []
        for columna in range(0, numeroColumnas):
#             if (random.randrange(2) == 1 and numeroParedesGeneradas < numeroParedes):
#                 filaMapaLaberinto.append('#')
#                 numeroParedesGeneradas += 1
#             else:
#                 filaMapaLaberinto.append('')
            filaMapaLaberinto.append('#')
        mapaLaberinto.append(filaMapaLaberinto)
#Se ubica un punto de inicio aleartorio y a partir del punto se generan espacios
    numeroEspaciosGenerados = 0
    filaPosicionActual = random.randrange(numeroFilas)
    columnaPosicionActual = random.randrange(numeroColumnas)
    mapaLaberinto[filaPosicionActual][columnaPosicionActual] = ' '
    numeroEspaciosGenerados += 1
#Se ubica al jugador en un punto aleatorio
    jugadorPosicionFila = random.randrange(numeroFilas)
    jugadorPosicionColumna = random.randrange(numeroColumnas)
    mapaLaberinto[jugadorPosicionFila][jugadorPosicionColumna] = 'W'
    
    print(jugadorPosicionFila, jugadorPosicionColumna)

    while numeroEspaciosGenerados < numeroEspacios:
        direccion = random.randrange(4)
        if direccion == 0 and filaPosicionActual > 0:
            filaPosicionActual -=1
        elif direccion == 1 and filaPosicionActual < numeroFilas -1:
            filaPosicionActual += 1
        elif direccion == 2 and columnaPosicionActual > 0:
            columnaPosicionActual -= 1
        else:
            if columnaPosicionActual <numeroColumnas -1:
                columnaPosicionActual += 1
                
        if mapaLaberinto[filaPosicionActual][columnaPosicionActual] == '#':
            mapaLaberinto[filaPosicionActual][columnaPosicionActual] = ' '
            numeroEspaciosGenerados += 1
            
    return mapaLaberinto

def MoverJugador(laberinto, num_filas, num_columnas):
  for i in range(0, num_filas):
    for j in range(0, num_columnas):
      if laberinto[i][j] == "W":
        posJugador_Y = i
        posJugador_X = j
  print("Movimiento Jugador")
  print(posJugador_Y, posJugador_X)
  mover = True

  while mover:
    direccion = random.randrange(3)
    #Movimiento Arriba
    if direccion == 0 and laberinto[posJugador_Y - 1][posJugador_X] == " " and (posJugador_Y >= 0 and posJugador_Y < num_filas and posJugador_X >= 0 and posJugador_X <= num_columnas):
      laberinto[posJugador_Y - 1][posJugador_X] = "W"
      laberinto[posJugador_Y][posJugador_X] = " "
      mover = False
    #Movimiento Abajo
    elif direccion == 1 and laberinto[posJugador_Y + 1][posJugador_X] == " "  and (posJugador_Y >= 0 and posJugador_Y < num_filas and posJugador_X >= 0 and posJugador_X <= num_columnas):
      laberinto[posJugador_Y + 1][posJugador_X] = "W"
      laberinto[posJugador_Y][posJugador_X] = " "
      mover = False
    #Mover Izquierda
    if direccion == 2 and laberinto[posJugador_Y][posJugador_X - 1] == " " and (posJugador_Y >= 0 and posJugador_Y < num_filas and posJugador_X >= 0 and posJugador_X <= num_columnas):
      laberinto[posJugador_Y][posJugador_X - 1] = "W"
      laberinto[posJugador_Y][posJugador_X] = " "
      mover = False
    else:
      if laberinto[posJugador_Y][posJugador_X + 1] == " "  and (posJugador_Y >= 0 and posJugador_Y < num_filas and posJugador_X >= 0 and posJugador_X <= num_columnas):
        laberinto[posJugador_Y - 1][posJugador_X] = "W"
        laberinto[posJugador_Y][posJugador_X] = " "
        mover = False

    if laberinto[posJugador_Y-1][posJugador_X] == "#" and laberinto[posJugador_Y+1][posJugador_X] == "#" and laberinto[posJugador_Y][posJugador_X-1] == "#" and laberinto[posJugador_Y][posJugador_X+1] == "#":
      print("No tengo salida")
      mover = False

numeroFilas = int(input('Introduzca el número de filas del laberinto: '))
numeroColumnas = int(input('Introduzca el número de columnas del laberinto: '))
numeroParedes = int(input('Introduzca el número de paredes del laberinto: '))
numeroEspacios = numeroFilas * numeroColumnas - numeroParedes
#numeroJugador= int(input('Introduzca el numero de jugadores: '))

laberinto = crearMapaLaberinto(numeroFilas, numeroColumnas, numeroParedes, numeroEspacios, numeroJugador)

for filaMapaLaberinto in laberinto:
    print(filaMapaLaberinto)

for i in range(1,5):
  MoverJugador(laberinto, numeroFilas, numeroColumnas)