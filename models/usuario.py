class Usuario:

    def __init__(self, id_usuario, nombreUsuario, nombreRealNombre, nombreRealApellido, correo, contraseña, gameMaster):
        self._id_usuario = id_usuario
        self._nombreUsuario = nombreUsuario
        self._nombreRealNombre = nombreRealNombre
        self._nombreRealApellido = nombreRealApellido
        self._correo = correo
        self._contraseña = contraseña
        self._gameMaster = gameMaster

    def getId_usuario(self):
        return self.__id_usuario
    
    def getNombreUsuario(self):
        return self.__nombreUsuario
    
    def getNombreRealNombre(self):
        return self.__nombreRealNombre
    
    def getNombreRealApellido(self):
        return self.__nombreRealApellido
    
    def getCorreo(self):
        return self.__correo
    
    def getContraseña(self):
        return self.__contraseña
    
    def getGm(self):
        return self.__gameMaster
    
    def setId_usuario(self, id_usuario):
        self.__id_usuario = id_usuario
    
    def setNombreUsuario(self, nombreUsuario):
        self.__nombreUsuario = nombreUsuario
    
    def setNombreRealNombre(self, nombreRealNombre):
        self.__nombreRealNombre = nombreRealNombre
    
    def setNombreRealApellido(self, nombreRealApellido):
        self.__nombreRealApellido = nombreRealApellido
    
    def setCorreo(self, correo):
        self.__correo = correo
    
    def setContraseña(self, contraseña):
        self.__contraseña = contraseña
    
    def setGm(self, gameMaster):
        self.__gameMaster = gameMaster