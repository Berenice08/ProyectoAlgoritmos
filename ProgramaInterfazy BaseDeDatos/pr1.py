from conexion import * 

class Hospital(Conexion):
    
    def insertar(self,n,e,g,d,t,h):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO Citas VALUES (null,'"+n+"','"+e+"','"+g+"','"+d+"','"+t+"','"+h+"')")
        cnx.commit() #Realizar inserción
        self.cerrarConexion(cnx)

    def cargar(self,ID):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Citas WHERE ID="+str(ID))
        arreglo = []
        for (Citas) in cursor:
            arreglo.append(Citas)
        self.cerrarConexion(cnx)
        return arreglo

    def modificar(self,n,e,g,d,t,h,ID):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("UPDATE Citas SET Nombre='"+n+"',Edad='"+str(e)+"',Genero='"+g+"',Direccion='"+d+"',Telefono='"+str(t)+"',Hora_cita='"+h+"' WHERE ID='"+str(ID)+"'") 
        cnx.commit()
        self.cerrarConexion(cnx) 

    def buscar(self,cadena):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Citas WHERE Nombre LIKE '%"+str(cadena)+"%'")
        arreglo = []
        for (Citas) in cursor:
            arreglo.append(Citas)
        self.cerrarConexion(cnx)
        return arreglo  


    def consultar(self):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Citas")
        arreglo = []
        for (Citas) in cursor:
            arreglo.append(Citas)
        self.cerrarConexion(cnx)
        return arreglo
   
    


    def eliminar(self,ID):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM Citas WHERE ID="+str(ID))
        cnx.commit()
        self.cerrarConexion(cnx)

class Usuario(Conexion):

    def consultar(self,us,pas):
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE User='"+us+"' AND Password='"+pas+"'")
        for (usuario) in cursor:
            if usuario [1]==us and usuario[2]==pas:
                self.cerrarConexion(cnx)
                return True
        self.cerrarConexion(cnx)
        return False
        
 
    
    def Permisoss(us):
        mydb = mysql.connector.connect(user="root",password="12345",host="localhost",db="HOSPITAL_PRUEBA1")
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("""SELECT Permisos FROM Usuarios WHERE User='"+us+"' """)
        bien=mycursor.fetchall()
        for i in bien:
            if i ==(0,):
        
             print (True)
        else:
            print (False)