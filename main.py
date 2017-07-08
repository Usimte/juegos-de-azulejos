# como documentar los metodos en python
# Crear matriz
# Generar numero aleatorio

from random import randrange, random
from os import system, name as opsystem
from time import sleep

# ------------------------- Getters and setters ----------------------#


def get_tamano_tablero():
    global tamano_tablero
    return tamano_tablero


def set_tamano_tablero(tamano):
    global tamano_tablero
    tamano_tablero = tamano


# ------------------------- end Getters and setters ----------------------#

# constantes para los modos de juego
OPCION_MODO_INDIVIDUAL = 1
OPCION_MODO_AUTOMATICO = 2
OPCION_SALIR = 3

# Aquí se guardará la opción elegida por el usuario
opcion_elegida_por_usuario = 4

# variables del juego
tamano_tablero = 0
tablero = []


# Esta funcion genera numeros aleatorios entero
# @numero_maximo es el limite opciones posibles de numeros aleatorios
# return: un numero aleatorio entre 0 y (numero_maximo - 1)
def get_numero_aleatorio(numero_maximo):
    return randrange(0, stop=numero_maximo)


# Esta funcion se encarga de pedirle al usuario el tamano del tablero y crear
# un tablero cuadrado con numeros aleatorios return: Un tablero de tamano NxN
# lleno de valores aleatorios
def crear_Tablero(tam=tamano_tablero):
    global tablero
    set_tamano_tablero(tam)
    print("Creando tablero...")
    fila_nueva = []
    for fila in range(0, get_tamano_tablero()):
        for columna in range(0, tam):
            fila_nueva.append(get_numero_aleatorio(get_tamano_tablero()))
        tablero.append(fila_nueva)
        fila_nueva = []

# Esta función inicia un flujo de juego automático, el tablero se crea según un tamaño máximo posible indicado por el usuario
def modo_Automatico():
    tamano = 0
    seleccion_usuario = 0
    while(seleccion_usuario <= 0):
        encabezado(1)
        seleccion_usuario = int(input("Ingrese el tamaño máximo posible: "))
        if(seleccion_usuario <= 0):
            print('Intenta crear un tablero más grande')
            sleep(1)
    while (tamano == 0):
        tamano = get_numero_aleatorio(seleccion_usuario + 1)
    crear_Tablero(tamano)


# Esta función inicia un flujo manual de juego, el tablero es creado según
# las indicaciones del usuario
def creador_Manual():
    tamano = 0
    while(tamano <= 0):
        encabezado(1)
        tamano = int(input("Elija el tamano del tablero: "))
        if(tamano <= 0):
            print('Intenta crear un tablero más grande')
            sleep(1)
    crear_Tablero(tamano)

    if(opsystem == 'posix'):
        system('clear')
    else:
        system('cls')
    print("     *   * ***** ***** **   ** ***** *****    ")
    print("     *   * *       *   * * * *   *   *        ")
    print("     *   * *****   *   *  *  *   *   *****    ")
    print("     *   *     *   *   *     *   *   *        ")
    print("     ***** ***** ***** *     *   *   *****    ")
    print("**********************************************")
    if(modo == 0):
        print("*     Bienvenido al juego de azulejos        *")
    elif(modo == 1):
        print("*           Que empiece el juego             *")
    print("**********************************************")


# Se muestra el menu mientras el usuario no elija una opcion válida
while (opcion_elegida_por_usuario > OPCION_SALIR or
        opcion_elegida_por_usuario <= 0):
    encabezado()
    print("Seleccione una opcion:")
    print("1. Jugar")
    print("2. Modo automatico")
    print("3. Salir")
    opcion_elegida_por_usuario = int(input("Opcion: "))
    if (opcion_elegida_por_usuario == OPCION_MODO_INDIVIDUAL):
        modo_Manual()
    elif (opcion_elegida_por_usuario == OPCION_MODO_AUTOMATICO):
        modo_Automatico()
    elif (opcion_elegida_por_usuario == OPCION_SALIR):
        print("Gracias por jugar")
    else:
        print("La opción no es válida")
        sleep(1)
