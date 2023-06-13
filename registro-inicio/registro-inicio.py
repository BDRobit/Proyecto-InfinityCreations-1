import requests
from beautifultable import BeautifulTable
from models.usuario import Usuario
import time
import os
import re

try:
    os.system('cls')
    menu = BeautifulTable()
    menu.columns.header = ['=======TheUnlimitedGame=======']
    menu.rows.append(['1. Iniciar Sesión'])
    menu.rows.append(['2. Registrar Usuario'])
    menu.rows.append(['3. Salir'])
    menu.columns.alignment = BeautifulTable.ALIGN_LEFT

    def iniciarSesion():
        os.system('cls')
        print("=== Inicio de Sesión ===")

        correo = input("Correo Electrónico: ")
        contraseña = input("Contraseña: ")

        usuario = Usuario(None, None, None, None, correo, contraseña, None)

        print("Inicio de sesión exitoso!")
        input("Presione Enter para continuar...")

    """     def registrarUsuario():
        os.system('cls')
        print("=== Registro de Usuario ===")

        nombreUsuario = input("Nombre Usuario: ")
        nombreRealNombre = input("Nombre Real: ")
        nombreRealApellido = input("Apellido Real: ")
        correo = input("Correo Electrónico: ")

        while correoDataBase(correo):
            print("El correo ya está registrado.")
            correo = input("Ingrese otro correo electrónico: ")
            
        while True:
            contraseña = input("Contraseña: ")
            if len(contraseña) < 8 or not re.match("^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]+$", contraseña):
                print("La contraseña debe tener al menos 8 caracteres y ser alfanumérica.")
            else:
                break

        usuario = Usuario(None, nombreUsuario, nombreRealNombre, nombreRealApellido, correo, contraseña, None)
        print("¡Usuario registrado exitosamente!")
        input("Presione Enter para continuar...") """

    def salir():
        os.system('cls')
        print('Adios...')
        time.sleep(2)

    def incorrecto():
        os.system('cls')
        print('Opcion incorrecta, vuelva a intentar...')
        time.sleep(2)

    while True:
        os.system('cls')
        print(menu)
        opcion = input('Opcion: ')
        if opcion == '1':
            iniciarSesion()
        elif opcion == '2':
            registrarUsuario()
        elif opcion == '3':
            salir()
            break
        else:
            incorrecto()

except (requests.ConnectionError, requests.Timeout):
    print("Sin conexion :(")