# como documentar los metodos en python
# Crear matriz
# Generar numero aleatorio

#------------------------- Getters and setters ----------------------#


def get_tamano_tablero():
    global tamano_tablero
    return tamano_tablero


def set_tamano_tablero(tamano):
    global tamano_tablero
    tamano_tablero = tamano


#------------------------- end Getters and setters ----------------------#

# Esta funcion genera numeros aleatorios entero
# @numero_maximo es el limite opciones posibles de numeros aleatorios
# return: un numero aleatorio entre 0 y (numero_maximo - 1)
def get_numero_aleatorio(numero_maximo):
    return 1


# Esta funcion se encarga de pedirle al usuario el tamano del tablero y crear un tablero cuadrado con numeros aleatorios
# return: Un tablero de tamano NxN lleno de valores aleatorios
def crear_Tablero():
    global tablero
    tamano = input("Elija el tamano del tablero: ")
    set_tamano_tablero(tamano)

    fila_nueva = []
    for fila in range(0, tamano):
        for columna in range(0, tamano):
            fila_nueva[columna] = fila

        tablero[fila] = fila_nueva

    print("Creando tablero...")


print("     *   * ***** ***** **   ** ***** *****    ")
print("     *   * *       *   * * * *   *   *        ")
print("     *   * *****   *   *  *  *   *   *****    ")
print("     *   *     *   *   *     *   *   *        ")
print("     ***** ***** ***** *     *   *   *****    ")
print("**********************************************")
print("*     Bienvenido al juego de azulejos        *")
print("**********************************************")

# constantes para los modos de juego
OPCION_MODO_INDIVIDUAL = 1
OPCION_MODO_AUTOMATICO = 2
OPCION_SALIR = 3

# Aquí se guardará la opción elegida por el usuario
opcion_elegida_por_usuario = 4

# variables del juego
tamano_tablero = 0
tablero = []

# Se muestra el menu mientras el usuario no elija una opcion valida
while (opcion_elegida_por_usuario > opcion_salir or opcion_elegida_por_usuario <= 0):
    print("Seleccione una opcion:")
    print("1. Jugar")
    print("2. Modo automatico")
    print("3. Salir")
    opcion_elegida_por_usuario = input("Opcion: ")

if (opcion_elegida_por_usuario == opcion_modo_individual):
    crear_Tablero()
elif (opcion_elegida_por_usuario == opcion_modo_automatico):
    print("Método no disponible")
elif (opcion_elegida_por_usuario == opcion_salir):
    print("Gracias por jugar")
else:
    print("La opción no es válida")
