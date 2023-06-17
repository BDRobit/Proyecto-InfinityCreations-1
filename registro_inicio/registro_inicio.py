import time
import os
from models.usuario import Usuario

def iniciarSesion(usuarios_collection):
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

def registrarUsuario(usuarios_collection):
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