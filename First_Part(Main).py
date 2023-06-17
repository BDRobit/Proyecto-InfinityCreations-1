from pymongo import MongoClient
from beautifultable import BeautifulTable
import os
from registro_inicio.registro_inicio import iniciarSesion, registrarUsuario, salir, incorrecto

# Establecer la conexión con MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["infinityCreations"]
usuarios_collection = db["usuarios"]

menu = BeautifulTable()
menu.columns.header = ['=======TheUnlimitedGame=======']
menu.rows.append(['1. Iniciar Sesión'])
menu.rows.append(['2. Registrar Usuario'])
menu.rows.append(['3. Salir'])
menu.columns.alignment = BeautifulTable.ALIGN_LEFT

while True:
    os.system('cls')
    print(menu)
    opcion = input('Opcion: ')
    if opcion == '1':
        iniciarSesion(usuarios_collection)
    elif opcion == '2':
        registrarUsuario(usuarios_collection)
    elif opcion == '3':
        salir()
        break
    else:
        incorrecto()

# Cerrar la conexión con MongoDB
client.close()