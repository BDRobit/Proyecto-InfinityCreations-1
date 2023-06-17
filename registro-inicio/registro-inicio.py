from pymongo import MongoClient
from beautifultable import BeautifulTable
from models.usuario import Usuario
import time
import os

# Establecer la conexión con MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["infinityCreations"]
usuarios_collection = db["usuarios"]

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

        usuario = usuarios_collection.find_one({"correo": correo, "contraseña": contraseña})

        if usuario:
            print("Inicio de sesión exitoso!")
        else:
            print("Inicio de sesión fallido. Verifica tus credenciales.")

        input("Presione Enter para continuar...")

    def registrarUsuario():
        os.system('cls')
        print("=== Registro de Usuario ===")

        nombreUsuario = input("Nombre Usuario: ")
        nombreRealNombre = input("Nombre Real: ")
        nombreRealApellido = input("Apellido Real: ")
        correo = input("Correo Electrónico: ")

        while usuarios_collection.find_one({"correo": correo}):
            print("El correo ya está registrado.")
            correo = input("Ingrese otro correo electrónico: ")
            
        while True:
            contraseña = input("Contraseña: ")
            if len(contraseña) < 8:
                print("La contraseña debe tener al menos 8 caracteres.")
            else:
                break

        usuario = Usuario(None, nombreUsuario, nombreRealNombre, nombreRealApellido, correo, contraseña, None)
        usuarios_collection.insert_one(usuario.__dict__)
        print("¡Usuario registrado exitosamente!")
        input("Presione Enter para continuar...")

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

except:
    print("Error durante la ejecución del programa.")

# Cerrar la conexión con MongoDB
client.close()