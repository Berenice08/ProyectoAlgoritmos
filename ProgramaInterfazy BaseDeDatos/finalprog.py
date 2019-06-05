from tkinter import *
import tkinter.messagebox
import mysql.connector
from datetime import date, datetime, timedelta
mydb = mysql.connector.connect(user="root",password="perrito",host="localhost",db="hospital_prueba1")
c= mydb.cursor(buffered=True)


#PRIMERA PANTALLA, LOG IN :
ventana = Tk()
ventana.title ("------- Login Base de Datos--------")
ventana.geometry ("350x150+500+250")
Label(ventana, text = "Usuario:").pack()
caja1 = Entry(ventana)
caja1.pack() 
Label(ventana, text = "Contraseña:").pack()
caja2 = Entry(ventana, show = "*")
caja2.pack()

def login():
    usuario = caja1.get()
    contr = caja2.get()
    b=("SELECT Permisos FROM Usuarios WHERE User=" )
    d=("AND Password=")
    y=b+'"'+usuario+'"'+d+'"'+contr+'"'
    c.execute(y)
    if c.fetchall():
        return True
    else:
        return False
    c.close()
    
def Permisos(us):
    b=("SELECT Permisos FROM Usuarios WHERE User=")
    y=b+'"'+us+'"'
    c.execute(y)
    bien=c.fetchall()
    for i in bien:
        global GLOB
        GLOB= i

def entrar():             
    #import tkinter.messagebox
    usuario = caja1.get()
    validar = login()
    Permi=Permisos(usuario)
    if validar ==True :
        tkinter.messagebox.showinfo("BIENVENIDO", "Usuario y contraseña correctos")
        ventana.destroy()
    else:
        tkinter.messagebox.showinfo("Mensaje","Login incorrecto, usuario no identificado")
Button (text = "Login", command = entrar).pack()
ventana.mainloop()



#PERMISOS:  O = Secretaria, 1 = Doctor, 2 = Admin, 3 = Paciente
#SEGUNDA VENTANA (SI ES ADMIN)

if GLOB==(2,):  
    ids = []
    class Application:
        def __init__(self, master):
            self.master = master    #marcos
            self.left = Frame(master, width=800, height=720, bg='#006')
            self.left.pack(side=LEFT)
            self.right = Frame(master, width=400, height=720, bg='#006')
            self.right.pack(side=RIGHT)
            self.right = Frame(master, width=400, height=720, bg='#006')
            self.right.pack(side=RIGHT)
            self.right = Frame(master, width=400, height=720, bg='#006')
            self.right.pack(side=RIGHT)

            self.heading = Label(self.left, text="Agregar Usuario", fg='#FFF', bg='#006') #etiquetas para ventana
            self.heading.place(x=10, y=10)
            self.apellidos = Label(self.left, text="Nombre de usuario", fg='#FFF', bg='#006')
            self.apellidos.place(x=70, y=140)
            self.nombre = Label(self.left, text="Contraseña nueva", fg='#FFF', bg='#006')
            self.nombre.place(x=70, y=190)
            self.genero = Label(self.left, text="Puesto(secretaria,doctor,admin,paciente)", fg='#FFF', bg='#006')
            self.genero.place(x=70, y=240)

            self.user_ent = Entry(self.left, width=30)  #entradas
            self.user_ent.place(x=350, y=140)
            self.psw_ent = Entry(self.left, width=30)
            self.psw_ent.place(x=350, y=190)
            self.puesto_ent = Entry(self.left, width=30)
            self.puesto_ent.place(x=350, y=250)

            self.submit = Button(self.left,text="Añadir usuario",width=20,height=2,fg='#FFF',bg='#00a',command=self.añadir_usuario) #boton
            self.submit.place(x=210,y=370)
                
        def añadir_usuario(self): #Función a llamar cuando se le da click a añadir 
            self.val1 = self.user_ent.get()  #inputs  
            self.val2 = self.psw_ent.get()
            if self.puesto_ent.get()== "secretaria" :
                self.val3= 0
            elif self.puesto_ent.get()== "doctor" :
                self.val3= 1
            elif self.puesto_ent.get()== "admin" :
                self.val3= 2
            elif self.puesto_ent.get()== "paciente" :
                self.val3= 3
            else:
                tkinter.messagebox.showinfo("Cuidado","puesto no valido")
           
            if self.val1 == '' :  #Checar si el formato está completo
                tkinter.messagebox.showinfo("Cuidado","Por favor llena todo el formato")
            else:
                add_user =("INSERT INTO Usuarios"
                               "(User,Password,Permisos)" 
                               "VALUES (%s, %s, %s)")
                data_users =(self.val1,self.val2,self.val3)                 
                c.execute(add_user, data_users)
                mydb.commit()        
                tkinter.messagebox.showinfo("Excelente","El usuario  " +  " ha sido creado")
    root = Tk()
    b = Application(root)
    root.geometry("1200x720+0+0") # Resolución de la ventana 
    root.resizable(False, False)# Reajuste de tamaño de pantalla   
    root.mainloop() 


#VENTANA 2 PARA SECRETARIA    
elif GLOB==(0,): 
    from tkinter import ttk
    from tkinter.ttk import Style
    from tkinter import messagebox
    import mysql.connector
    from pr1 import *
    
    def cargarC():
        cita = Hospital()
        arreglo = cita.cargar(arregloIDM[comboM.current()])
        for c in arreglo:
            NombreM.set(c[1])
            EdadM.set(c[2])
            GeneroM.set(c[3])
            DireccionM.set(c[4])
            TelefonoM.set(c[5]) 
            Hora_citaM.set(c[6])


    def insertar():
        cita = Hospital()
        cita.insertar(Nombre.get(),Edad.get(),Genero.get(),Direccion.get(),Telefono.get(),Hora_cita.get())
        Nombre.set("")
        Edad.set("")
        Genero.set("")
        Direccion.set("")
        Telefono.set("")
        Hora_cita.set("")
        messagebox.showinfo("Excelente","Cita agendada")
        consultar()
        llenarCombo()

    def modificar():
        cita = Hospital()
        cita.modificar(NombreM.get(),EdadM.get(),GeneroM.get(),DireccionM.get(),TelefonoM.get(),Hora_citaM.get(),arregloIDM[comboM.current()])
        NombreM.set("")
        EdadM.set("")
        GeneroM.set("")
        DireccionM.set("")
        TelefonoM.set("")
        Hora_citaM.set("")
        messagebox.showinfo("Excelente","Contacto modificado")
        consultar()
        llenarCombo()

    def consultar():
        r.config(state=NORMAL)
        r.delete("1.0",END)
        r.insert(INSERT,"Nombre\t\tEdad\t\tGenero\t\tDireccion\t\tTelefono\t\tHora_cita\t\n")
        cita = Hospital()
        arreglo = cita.consultar()
        for c in arreglo:
            r.insert(INSERT,c[1]+"\t\t"+str(c[2])+"\t\t"+c[3]+"\t\t"+c[4]+"\t\t"+str(c[5])+"\t\t"+(c[6])+"\n")
        r.place(x=20,y=60)
        r.config(state=DISABLED)

    def buscar(key):
        if(cajaB.get()==""):
            consultar()
        else:
            r.config(state=NORMAL)
            r.delete("1.0",END)
            r.insert(INSERT,"Nombre\t\tEdad\t\tGenero\t\tDireccion\t\tTelefono\t\tHora_cita\t\n")
            cita = Hospital()
            arreglo = cita.buscar(cajaB.get())
            for c in arreglo:
                r.insert(INSERT,c[1]+"\t\t"+str(c[2])+"\t\t"+c[3]+"\t\t"+c[4]+"\t\t"+str(c[5])+"\t\t"+(c[6])+"\n")
            r.place(x=20,y=60)
            r.config(state=DISABLED)

    def eliminar():
        print(combo.current())
        cita = Hospital()
        cita.eliminar(arregloID[combo.current()])
        messagebox.showinfo("Mensaje","Cita eliminada")
        consultar()
        llenarCombo()

    def pestInsertar():
        s.configure('My.TFrame',bg=colorFondo,fg=colorLetra)
        pes0 = ttk.Frame(notebook,style='My.TFrame')
        notebook.add(pes0,text="Añadir cita")
        Label(pes0,text="Nombre del paciente", fg=colorLetra, bg=colorFondo).place(x=20,y=50)
        Label(pes0,text="Edad", fg=colorLetra, bg=colorFondo).place(x=20,y=100)
        Label(pes0,text="Género", fg=colorLetra, bg=colorFondo).place(x=20,y=150)
        Label(pes0,text="Dirección", fg=colorLetra, bg=colorFondo).place(x=20,y=200)
        Label(pes0,text="Teléfono", fg=colorLetra, bg=colorFondo).place(x=20,y=250)
        Label(pes0,text="Hora de la cita", fg=colorLetra, bg=colorFondo).place(x=20,y=300)
        Entry(pes0,textvariable=Nombre).place(x=120,y=50)
        Entry(pes0,textvariable=Edad).place(x=120,y=100)
        Entry(pes0,textvariable=Genero).place(x=120,y=150)
        Entry(pes0,textvariable=Direccion).place(x=120,y=200)
        Entry(pes0,textvariable=Telefono).place(x=120,y=250)
        Entry(pes0,textvariable=Hora_cita).place(x=120,y=300)
        Button(pes0,text="Guardar",bg="#00a",fg="white",command=insertar).place(x=120,y=350)

    def pestModificar():
        pes3 = ttk.Frame(notebook,style='My.TFrame')
        notebook.add(pes3,text="Modificar")
        Label(pes3,text="Seleccionar :",fg=colorLetra,bg=colorFondo).place(x=20,y=50)
        global comboM
        comboM = ttk.Combobox(pes3)
        comboM.place(x=80,y=50)
        Button(pes3,text="Cargar",bg="#00a",fg="white",command=cargarC).place(x=120,y=90)
        Label(pes3,text="Nombre del paciente", fg=colorLetra, bg=colorFondo).place(x=20,y=120)
        Label(pes3,text="Edad", fg=colorLetra, bg=colorFondo).place(x=20,y=150)
        Label(pes3,text="Género", fg=colorLetra, bg=colorFondo).place(x=20,y=180)
        Label(pes3,text="Dirección", fg=colorLetra, bg=colorFondo).place(x=20,y=210)
        Label(pes3,text="Teléfono", fg=colorLetra, bg=colorFondo).place(x=20,y=240)
        Label(pes3,text="Hora de la cita", fg=colorLetra, bg=colorFondo).place(x=20,y=270)
        Entry(pes3,textvariable=NombreM).place(x=120,y=120)
        Entry(pes3,textvariable=EdadM).place(x=120,y=150)
        Entry(pes3,textvariable=GeneroM).place(x=120,y=180)
        Entry(pes3,textvariable=DireccionM).place(x=120,y=210)
        Entry(pes3,textvariable=TelefonoM).place(x=120,y=240)
        Entry(pes3,textvariable=Hora_citaM).place(x=120,y=270)
        Button(pes3,text="Guardar",bg="#00a",fg="white",command=modificar).place(x=120,y=350)

    def pestEliminar():
        pes2 = ttk.Frame(notebook,style='My.TFrame')
        notebook.add(pes2,text="Eliminar")
        Label(pes2,text="Seleccionar :",fg=colorLetra,bg=colorFondo).place(x=20,y=100)
        global combo
        combo = ttk.Combobox(pes2)
        combo.place(x=80,y=100)
        llenarCombo()
        Button(pes2,text="Eliminar",bg="#00a",fg="white",command=eliminar).place(x=120,y=200)

    def llenarCombo():
        citas = Hospital()
        arreglo = citas.consultar()
        arregloCitas = []
        global arregloID
        arregloID = []
        for c in arreglo:
            arregloCitas.append(c[1])
            arregloID.append(c[0])
        combo['values']=arregloCitas
        combo.current(0)

        citas = Hospital()
        arreglo = citas.consultar()
        arregloCitas = []
        global arregloIDM
        arregloIDM = []
        for c in arreglo:
            arregloCitas.append(c[1])
            arregloIDM.append(c[0])
        comboM['values']=arregloCitas
        comboM.current(0)

    ventana= Tk()
    colorFondo = "#006"
    colorLetra = "#FFF"
    s = Style()
    s.configure('My.TFrame',background=colorFondo,foreground=colorLetra)
    Nombre = StringVar()
    Edad = StringVar()
    Genero = StringVar()
    Direccion = StringVar()
    Telefono = StringVar()
    Hora_cita = StringVar()
    NombreM = StringVar()
    EdadM = StringVar()
    GeneroM = StringVar()
    DireccionM = StringVar()
    TelefonoM = StringVar()
    Hora_citaM = StringVar()
    cajaB = StringVar()
    notebook = ttk.Notebook(ventana)
    notebook.pack(fill='both',expand='yes')
    pestInsertar()
    pes1 = ttk.Frame(notebook,style='My.TFrame')
    notebook.add(pes1,text="Consultar")
    r = Text(pes1,width=100,height=100)
    consultar()
    Label(pes1,text="Buscar: ",fg=colorLetra,bg=colorFondo).place(x=20,y=30)
    entry = Entry(pes1,textvariable=cajaB)
    entry.place(x=80,y=30)
    entry.bind("<KeyRelease>",buscar)
    pestModificar()
    pestEliminar()
    ventana.geometry("600x800")
    ventana.mainloop()
   
#VENTANA2 PARA DOCTOR    
elif GLOB== (1,):
    ids = []
    class Application:
        def __init__(self, master):
            self.master = master
            self.left = Frame(master, width=800, height=720, bg='#006') #marcos
            self.left.pack(side=LEFT)
            self.right = Frame(master, width=400, height=720, bg='#006')
            self.right.pack(side=RIGHT)
            self.right = Frame(master, width=400, height=720, bg='#006')
            self.right.pack(side=RIGHT)
            self.right = Frame(master, width=400, height=720, bg='#006')
            self.right.pack(side=RIGHT)
            self.heading = Label(self.left, text="Agregar Paciente", fg='#FFF', bg='#006') # etiq. para ventana
            self.heading.place(x=0, y=0)
            self.apellidos = Label(self.left, text="Apellidos", fg='#FFF', bg='#006')
            self.apellidos.place(x=70, y=140)
            self.nombre = Label(self.left, text="Nombre", fg='#FFF', bg='#006')
            self.nombre.place(x=70, y=190)
            self.genero = Label(self.left, text="Genero", fg='#FFF', bg='#006')
            self.genero.place(x=70, y=240)
            self.dia = Label(self.left, text="Fecha de nacimiento", fg='#FFF', bg='#006')
            self.dia.place(x=70, y=290)
            self.dia = Label(self.left, text="Dia", fg='#FFF', bg='#006')
            self.dia.place(x=70, y=340)
            self.mes = Label(self.left, text="Mes", fg='#FFF', bg='#006')
            self.mes.place(x=70, y=390)
            self.año = Label(self.left, text="Año",fg='#FFF', bg='#006')
            self.año.place(x=70, y=440)

            self.apellidos_ent = Entry(self.left, width=30) #entradas
            self.apellidos_ent.place(x=250, y=140)
            self.nombre_ent = Entry(self.left, width=30)
            self.nombre_ent.place(x=250, y=190)
            self.genero_ent = Entry(self.left, width=30)
            self.genero_ent.place(x=250, y=240)
            self.dia_ent = Entry(self.left, width=30)
            self.dia_ent.place(x=250, y=340)
            self.mes_ent = Entry(self.left, width=30)
            self.mes_ent.place(x=250, y=390)
            self.año_ent = Entry(self.left, width=30)
            self.año_ent.place(x=250, y=440)

            self.submit = Button(self.left,text="Añadir paciente",width=20,height=2,bg='#00a',fg='#FFF',command=self.añadir_pac)#boton
            self.submit.place(x=210,y=470)

       
        def añadir_pac(self):
            self.val1 = int(self.dia_ent.get())   #inputs
            self.val11=int(self.mes_ent.get())
            self.val12=int(self.año_ent.get())
            self.val2 = self.apellidos_ent.get()
            self.val3 = self.nombre_ent.get()
            self.val4 = self.genero_ent.get()

            if self.val1 == '' or self.val2 == '' or self.val3 == ''or self.val11 == '' :
                tkinter.messagebox.showinfo("Cuidado","Por favor llena todo el formato")
            else:
                add_paciente =("INSERT INTO Pacientes"
                               "(Fecha_de_nacimiento,Apellidos,Nombres,Genero)" 
                               "VALUES (%s, %s, %s, %s)")
                data_pacientes =(date(self.val12,self.val11,self.val1),self.val2,self.val3,self.val4)                 
                c.execute(add_paciente, data_pacientes)
                mydb.commit()        
                sql = "SELECT * FROM Pacientes WHERE Apellidos ='%s' and Nombres = '%s'"%(self.val2,self.val3)
                c.execute(sql)
                myresult = c.fetchall()
                for x in myresult:   
                     t=x[0]
                tkinter.messagebox.showinfo("Excelente","El paciente  " +  " ha sido añadido")
                tkinter.messagebox.showinfo("El numero de paciente es ",t )
    root = Tk()
    b = Application(root)
    root.geometry("1200x720+0+0")
    root.resizable(False, False)
    root.mainloop()
#VENTANA 2 PARA PACIENTE
elif GLOB==(3,):
    ids = []
    class Application:
        def __init__(self, master):
            self.master = master
            self.left = Frame(master, width=800, height=720, bg='#006') #marcos
            self.left.pack(side=LEFT)
            self.heading = Label(self.left, text="Consultar datos ", fg='#FFF', bg='#006') #etiquetas
            self.heading.place(x=0, y=0)
            self.numero = Label(self.left, text="Número de paciente", fg='#FFF', bg='#006')
            self.numero.place(x=50, y=180)
            self.numero_ent = Entry(self.left, width=30) #entrads
            self.numero_ent.place(x=350, y=190)
            self.submitt = Button(self.left,text="Consultar Nombre",width=20,height=2,bg='#00a',fg='#FFF',command=self.name) #boton
            self.submitt.place(x=240,y=290)
            self.submitt = Button(self.left,text="Consultar Apellidos",width=20,height=2,bg='#00a',fg='#FFF',command=self.last)
            self.submitt.place(x=240,y=340)
            self.submitt = Button(self.left,text="Consultar Género",width=20,height=2,bg='#00a',fg='#FFF',command=self.gender)
            self.submitt.place(x=240,y=390)
            self.submitt = Button(self.left,text="Consultar Fecha de Nacimiento",width=25,height=2,bg='#00a',fg='#FFF',command=self.date)
            self.submitt.place(x=225,y=440)
        def name(self):
            self.val1 = int(self.numero_ent.get())
            if self.val1 == '' :
                tkinter.messagebox.showinfo("Cuidado","Por favor llena todo el formato")
            else:
                selec=("""SELECT * FROM Pacientes  WHERE Numero_de_paciente=%s"""%self.val1)
                c.execute(selec)
                result_set = c.fetchall()
                for row in result_set:
                    r=row
                tkinter.messagebox.showinfo("Nombre",row[3])
        def last(self):
            self.val1 = int(self.numero_ent.get())
            if self.val1 == '' :
                tkinter.messagebox.showinfo("Cuidado","Por favor llena todo el formato")
            else:
                selec=("""SELECT * FROM Pacientes  WHERE Numero_de_paciente=%s"""%self.val1)
                c.execute(selec)
                result_set = c.fetchall()
                for row in result_set:
                    r=row
                tkinter.messagebox.showinfo("Apellidos",row[2])

        def gender(self):
            self.val1 = int(self.numero_ent.get())
            if self.val1 == '' :
                tkinter.messagebox.showinfo("Cuidado","Por favor llena todo el formato")
            else:
                selec=("""SELECT * FROM Pacientes  WHERE Numero_de_paciente=%s"""%self.val1)
                c.execute(selec)
                result_set = c.fetchall()
                for row in result_set:
                    r=row
                tkinter.messagebox.showinfo("Genero",row[4])

        def date(self):
            self.val1 = int(self.numero_ent.get())
            if self.val1 == '' :
                tkinter.messagebox.showinfo("Cuidado","Por favor llena todo el formato")
            else:
                selec=("""SELECT * FROM Pacientes  WHERE Numero_de_paciente=%s"""%self.val1)
                c.execute(selec)
                result_set = c.fetchall()
                for row in result_set:
                    r=row
                tkinter.messagebox.showinfo("Fecha_de_nacimiento",row[1])
                
 

    root = Tk()
    b = Application(root)
    root.geometry("1200x720+0+0")
    root.resizable(False, False)
    root.mainloop()
    
else:
    var_lbl = tk.StringVar()
    var_lbl.set(f"Error")