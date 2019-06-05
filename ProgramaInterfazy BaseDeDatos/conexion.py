import mysql.connector
from mysql.connector import errorcode

class Conexion:

    def conectar(self):
        try:
            conexion = mysql.connector.connect(user='root',
                password='perrito',
                host='localhost',
                database='hospital_prueba1')
            print("Conectado correctamente")
            return conexion
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de usuario o contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de datos no existe")
            else:
                print("err")
            return None

    def cerrarConexion(self,conexion):
        print("Cerrando conexión...")
        conexion.close()
        print("Conexión cerrada")