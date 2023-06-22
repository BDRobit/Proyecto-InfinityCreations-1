import os
import time
from beautifultable import BeautifulTable



from pantalla import usuario
from pantalla import listRazas, listPoder, listHabilidad 
from pantalla import listEquipo

# ordenando menu personaje para quitar errores


def incorrecto():
    os.system('cls')
    print('Opción incorrecta, vuelva a intentar...')
    time.sleep(2)

def salir():
    os.system('cls')
    print('Adiós...')
    time.sleep(2)

def mostrarPersonaje():
    pass

def crearPersonaje():
    os.system('cls')

# Primer menú Personaje
menu1 = BeautifulTable()
menu1.columns.header = ['=======Personajes=======']
menu1.rows.append(['1. Mostrar personajes'])
menu1.rows.append(['2. Crear Personaje'])
menu1.rows.append(['3. Salir'])
menu1.columns.alignment = BeautifulTable.ALIGN_LEFT

while True:
    os.system('cls')
    print(menu1)
    opcion = input('Opción: ')

    if opcion == '1':
        mostrarPersonaje()

    elif opcion == '2':
        crearPersonaje()

    elif opcion == '3':
        salir()
        break

    else:
        incorrecto()


    while True:
        menu = BeautifulTable()
        menu.columns.header = ['=======¿Quieres crear este personaje?=======']
        menu.rows.append([input("Nombre del personaje: ")])
        menu.rows.append(['1. Selecciona Raza'])
        menu.rows.append(['2. Selecciona Equipamiento'])
        menu.rows.append(['3. Guardar'])
        menu.rows.append(['8. Salir'])
        menu.columns.alignment = BeautifulTable.ALIGN_LEFT

        print(menu)
        opcion = input('Opción: ')

        if opcion == '1':
            print('=======Verás la lista de razas disponibles=======')
            print('===Cada una tiene distintos poderes y habilidades===')
            listRazas()
            print('=====Selecciona por su ID y mostraré sus habilidades=====')
            input("ID de raza escogida: ")
            listHabilidad()
            print('=====Puedes seleccionar 2 ID de habilidades======')
            input("ID de Habilidad 1: ")
            input("ID de Habilidad 2: ")
            listPoder()
            print('=======Solo puedes seleccionar 1 poder=======')
            input("ID de poder: ")
            print('====Volverás al menú si deseas cambiar la raza o seguir con el equipamiento====')

            time.sleep(2)
            os.system('cls')

            print('Cargando menú...')
            time.sleep(1)

        elif opcion == '2':
            print('=====Puedes elegir el equipamiento que desees=====')
            listEquipo()
            print('=======Solo puedes seleccionar 1 equipo=======')
            input("ID de equipo: ")
            print('=======Volverás al menú=======')

            time.sleep(2)
            os.system('cls')

            print('Cargando menú...')
            time.sleep(1)

        elif opcion == '3':
            # Falta verificar que los datos se ingresen correctamente
            print('=======Guardando Personaje=======')
            time.sleep(2)
            os.system('cls')
            print('=======Podrás verlo en "Mostrar personaje"=======')
            time.sleep(2)
            os.system('cls')
            print(menu1)

        elif opcion == '8':
            os.system('cls')
            salir()
            break

        else:
            incorrecto()

