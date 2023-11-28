#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#Veamos quiero crear un minijuego de piedra, papel y tijeras que tenga las siguientes especificaciones: 
#1. Este minijuego sera multijugador, es decir, dos personas podran jugar al mismo tiempo. La consola solicitara que cada jugador seleccione una opcion (piedra, papel o tijeras) y luego de que ambos hayan seleccionado, la consola mostrara el resultado de la partida.
#2. El programa debe validar que la opcion seleccionada por el jugador sea una opcion valida (piedra, papel o tijeras). Si el jugador ingresa una opcion invalida, el programa debe solicitar que ingrese una opcion valida.
#3. El jugador puede elegir volver a jugar o salir.
#4. En cada ronda, el jugador debe entrar en una de las opciones de la lista y ser informado de si ganó, perdió o empató con el oponente.
#5. El minijuego debe controlar las entradas del usuario, colocarlas en minúsculas e informar al usuario si la opción no es válida.
#6. Al final de cada ronda, el jugador debe responder si quiere jugar de nuevo o no.
#7. Las reglas son las siguientes:
#   - Piedra aplasta tijeras
#   - Tijeras cortan papel
#   - Papel envuelve piedra
#   - Si ambos jugadores eligen la misma opción, es un empate.
# Escribe tu codigo aqui abajo sin comentarios para poder probarlo.
#-----------------------------------------------------------------------------------------
# Path: app.py
#-----------------------------------------------------------------------------------------
# Escribe tu codigo aqui abajo sin comentarios para poder probarlo.
#-----------------------------------------------------------------------------------------
#Escribe la linea de codigo sin comentarios para preguntar si desean volver a jugar(si desean que la aplicacion vuelva a preguntar por las opciones de los jugadores) o si no que termine la ejecucion de la aplicacion.
#-----------------------------------------------------------------------------------------
# Path: app.py
#-----------------------------------------------------------------------------------------
# Escribe la linea de codigo sin comentarios para preguntar si desean volver a jugar(si desean que la aplicacion vuelva a preguntar por las opciones de los jugadores) o si no que termine la ejecucion de la aplicacion.
#-----------------------------------------------------------------------------------------

import random

print("Bienvenido al juego de piedra, papel o tijeras")
print("Selecciona una de las siguientes opciones: 1. piedra, 2. papel o 3. tijeras")
print("Si quieres salir, escribe salir")
opcion = "si"

def Jugadas():
        jugador1 = input("Jugador 1, ingresa tu opción: ")
        jugador2 = input("Jugador 2, ingresa tu opción: ")

        if jugador1 == 1 and jugador2 == 2:
            print("Jugador 2 gana!")
        elif jugador1 == 1 and jugador2 == 3:
            print("Jugador 1 gana!")
        elif jugador1 == 2 and jugador2 == 1:
            print("Jugador 1 gana!")
        elif jugador1 == 2 and jugador2 == 3:
            print("Jugador 2 gana!")
        elif jugador1 == 3 and jugador2 == 2:
            print("Jugador 1 gana!")
        elif jugador1 == 3 and jugador2 == 1:
            print("Jugador 2 gana!")
        elif jugador1 == jugador2:
            print("Empate")
        elif (jugador1 != 1 or jugador1 != 2 or jugador1 != 3) or (jugador2 != 1 or jugador2 != 2 or jugador2 != 3):
            print("La opción ingresada no es válida, intente de nuevo")

while opcion == "si":
    Jugadas()
    opcion = input("Desea volver a jugar? (si/no): ")



