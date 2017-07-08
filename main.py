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


# Esta función se encarga de imprimir el trablero de una forma legible para el
# usuario, mostrando sus indicadores de fila y columna para facilitar la
# interacción al seleccionar una casilla
def imprimir_tablero():
    partial_tab = '\t'
    for fila in range(0, get_tamano_tablero()):
        partial_tab += str(fila) + '\t'
    print(partial_tab)
    print(' ')
    partial_tab = ' '
    num_fila = 0
    for fila in tablero:
        partial_tab += str(num_fila) + '\t'
        num_fila += 1
        for columna in fila:
            partial_tab += str(columna) + '\t'
        print(partial_tab)
        partial_tab = ' '


# Esta función retorna verdadero si el tablero está vacío, en caso contrario
# retorna False
def tablero_limpio():
    for fila in tablero:
        for columna in fila:
            if str(columna) != ' ':
                return False
    return True


# Esta función inicia un flujo de juego automático, el tablero se crea
# según un tamaño máximo posible indicado por el usuario
def creador_Automatico():
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


# Esta función analiza y elimina los elementos correspondientes según
# la casilla escogida
def eliminar(coordenadaX, coordenadaY, item=None):
    seleccion = tablero[coordenadaY][coordenadaX]
    if item is None:
        tablero[coordenadaY][coordenadaX] = ' '
    elif item == ' ':
        return None
    elif item == seleccion:
        tablero[coordenadaY][coordenadaX] = ' '
    else:
        return None
    if coordenadaY > 0:
        eliminar(coordenadaX, coordenadaY - 1, seleccion)
    if coordenadaX < tamano_tablero - 1:
        eliminar(coordenadaX + 1, coordenadaY, seleccion)
    if coordenadaY < tamano_tablero - 1:
        eliminar(coordenadaX, coordenadaY + 1, seleccion)
    if coordenadaX > 0:
        eliminar(coordenadaX - 1, coordenadaY, seleccion)


# Esta función busca ordenar el tablero organizando los elementos de forma
# horizontal y vertical
def ordenar():
    tiene_espacios = True
    while tiene_espacios:
        tiene_espacios = False
        num_fila = 0
        for fila in tablero:
            num_columna = 0
            for columna in fila:
                if columna == ' ' and tablero[num_fila - 1][
                        num_columna] != ' ' and num_fila > 0:
                    mover_vertical(num_columna, num_fila)
                    tiene_espacios = True
                num_columna += 1
            num_fila += 1


# Esta función desplaza verticalmente un espacio, una casilla hacia arriba
def mover_vertical(coordenadaX, coordenadaY):
    if coordenadaY > 0:
        tablero[coordenadaY][coordenadaX] = tablero[
            coordenadaY - 1][coordenadaX]
        tablero[coordenadaY - 1][coordenadaX] = ' '


# Esta función define el modo de juego automatico
def modo_Automatico():
    creador_Automatico()
    while not tablero_limpio():
        sleep(1)
        encabezado(2)
        imprimir_tablero()
        print(' ')
        coordenadaX = get_numero_aleatorio(get_tamano_tablero())
        coordenadaY = get_numero_aleatorio(get_tamano_tablero())
        eliminar(coordenadaX, coordenadaY)
        ordenar()


# Esta función define el modo de juego manual
def modo_Manual():
    creador_Manual()
    while not tablero_limpio():
        encabezado(2)
        imprimir_tablero()
        print(' ')
        coordenadaX = int(input('Ingrese la coordenada X: '))
        coordenadaY = int(input('Ingrese la coordenada Y: '))
        eliminar(coordenadaX, coordenadaY)
        ordenar()


# Esta función se encarga de imprimir un encabezado que cambia según la etapa
# En la que se encuentre el juego
def encabezado(modo=0):
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
        print("*         Configuremos el tablero            *")
    elif(modo == 2):
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
