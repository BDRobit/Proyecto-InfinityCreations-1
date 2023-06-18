import time
import os
from beautifultable import BeautifulTable
from pantalla import usuario
from pantalla import listRaza, listPoder, listHabilidad 
from pantalla import listEquipo

# opcion conectarse como jugador activa 
# Menu personajes botones, Crear Personaje y Salir funcionando
#Crear personaje, pide nombre de personaje
#Menu 2 revisando aun

#Error al ingresar
def incorrecto():
    os.system('cls')
    print('Opcion incorrecta, vuelva a intentar...')
    time.sleep(2)

def salir():
    os.system('cls')
    print('Adios...')
    time.sleep(2)









while True:

    if usuario.gm == False:
        # Si el usuario es GM
        print("El usuario es GM.")
        # Mandar a edicion de personaje guardado


    else:
        # Si el usuario no es GM
        print("Te conectaste como jugador")
        time.sleep(2)
        os.system('cls')
        # colocar en codigo de creacion de personaje

        # Para mostrar personaje
        def mostrarPersonajes():
            pass




        def crearPersonaje():
            os.system('cls')

            while True:            
                menu = BeautifulTable()
                menu.columns.header = ['=======Quieres Crear este personaje=======']
                menu.rows.append([input("Nombre del personaje: ")])
                menu.rows.append(['1. Selecciona Raza'])
                menu.rows.append(['2. Selecciona Equipamiento'])
                menu.rows.append(['3. Guardar'])
                menu.rows.append(['8. Salir'])
                menu.columns.alignment = BeautifulTable.ALIGN_LEFT

                print (menu)
                opcion = input('Opción: ')

                if opcion == '1':
                    print('=====Veras la lista de razas disponibles=====')
                    print('==========cada una tiene distintos===========')
                    print('===========poderes y habilidades=============')
                    listRaza(raza)
                    print('==Selecciona por su ID y mostrare sus habilidades==')
                    input("ID de raza escogida: ")
                    listHabilidad(raza)
                    print('======Puedes seleccionar 2 ID de habilidades=======')
                    input("ID de Habilidad 1: ")
                    input("ID de Habilidad 2: ")
                    listPoder(raza)
                    print('======Solo puedes seleccionar 1 poders=============')
                    input("ID de poder: ")
                    print('====Volveras al menu si deseas cambias la raza o sigues con el Equipamiento====')

                    time.sleep(2)
                    os.system('cls')
                    
                    print('cargando menu...')
                    time.sleep(1)
                    
                

                elif opcion == '2':
                    print('====Puedes escojer el equipamiento que quieras====')                  
                    listEquipo(equipo)
                    print('======Solo puedes seleccionar 1 equipo=============')
                    input("ID de equipo: ")
                    print('===============Volveras al menu ===================')

                    time.sleep(2)
                    os.system('cls')
                    
                    print('cargando menu...')
                    time.sleep(1)

                elif opcion == '3':
        # falta que verifique datos ingresados correctamente
                    print('====Guardando Personaje====')
                    time.sleep(2)
                    os.system('cls')
                    print('====podras verlo en mostrar personaje====') 
                    time.sleep(2)
                    os.system('cls')
                    print(menu1)
                        
                elif opcion == '8':            
                    os.system('cls')
                    salir()
                
                else:
                    incorrecto()


        # Primer menu Personaje
        menu1 = BeautifulTable()
        menu1.columns.header = ['=======Personajes=======']
        menu1.rows.append(['1. Mostrar personajes'])
        menu1.rows.append(['2. Crear Personaje'])
        menu1.rows.append(['3. Salir'])
        menu1.columns.alignment = BeautifulTable.ALIGN_LEFT

        while True:
            os.system('cls')
            print(menu1)
            opcion = input('Opcion: ')
            if opcion == '1':
                usuario = mostrarPersonaje()


            elif opcion == '2':
                crearPersonaje()



        #revisado
            elif opcion == '3':
                    salir()
                    break
            else:
                incorrecto()
                

