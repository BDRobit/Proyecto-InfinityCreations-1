import time
import os

# Ejemplo de envío de datos
# simulando clases y datos



#print(usuario)
  
class UserLogger:
    def __init__(self, id_usuario, nombre_real, nombre_usuario, gm):
        self.id_usuario = id_usuario
        self.nombre_real = nombre_real
        self.nombre_usuario = nombre_usuario
        self.gm = gm



    def __str__(self):
        return f"ID de Usuario: {self.id_usuario}\n" \
               f"Nombre Real: {self.nombre_real}\n" \
               f"Nombre de Usuario: {self.nombre_usuario}\n" \
               f"GM: {self.gm}"

usuario = UserLogger(1, "Jonas", "johndoe", True)  
    
##Simulando cosas

def listRazas():
    razas = [
        Raza(1, "Raza 1"),
        Raza(2, "Raza 2"),
        Raza(3, "Raza 3")
    ]

    for raza in razas:
        print(f"ID: {raza.ID_raza}, Nombre: {raza.nombreRaza}")


class listEquipo:
    def __init__(self, ID_equipo, nombreEquipo):
        self.ID_equipo = ID_equipo
        self.nombreEquipo = nombreEquipo

class Raza:
    def __init__(self, ID_raza, nombreRaza):
        self.ID_raza = ID_raza
        self.nombreRaza = nombreRaza

class listPoder:
    def __init__(self, ID_equipo, nombreEquipo):
        self.ID_equipo = ID_equipo
        self.nombreEquipo = nombreEquipo

class listHabilidad:
    def __init__(self, ID_equipo, nombreEquipo):
        self.ID_equipo = ID_equipo
        self.nombreEquipo = nombreEquipo                           



"""












# Ejemplo de lectura de datos (solo GM)
print(usuario.gm)

# Lógica condicional basada en el atributo gm
if usuario.gm:
    # Si el usuario es GM
    print("El usuario es GM. Redirigiendo a la sección de administración...")
    # Coloca aquí el código correspondiente a la sección de administración
else:
    # Si el usuario no es GM
    print("El usuario no es GM. Redirigiendo a la sección de usuarios regulares...")
    # Coloca aquí el código correspondiente a la sección de usuarios regulares


"""