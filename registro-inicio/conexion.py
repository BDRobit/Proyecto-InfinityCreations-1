import cx_Oracle

class Conexion:

    def __init__(self):
        #inicializar el wallet
        cx_Oracle.init_oracle_client(lib_dir = r"")
        self.__connection = cx_Oracle.connect(user="", password="", dsn="clases2022_high")
        self.__cursor = self.__connection.cursor()

    def getConexion(self):
        return self.__connection

    def getCursor(self):
        return self.__cursor