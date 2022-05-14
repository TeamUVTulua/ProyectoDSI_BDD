# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ****** #

from Usuario import *
from gestionUsuario import *

class registroUsuario:

    def __init__(self, rootRegistroUsuario):
        self.rootRegistroUsuario = rootRegistroUsuario
        self.rootRegistroUsuario.title("Registro Usuario")
        self.rootRegistroUsuario.geometry("1360x768+560+312")
        self.rootRegistroUsuario.resizable(1, 1)

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootRegistroUsuario, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        # ****** Frame Crear Usuario ****** #

        frameCrearUsuario = Frame(self.rootRegistroUsuario,bg="#18344A")
        frameCrearUsuario.place(x=160, y=0, width=650, height=600)

        Label(frameCrearUsuario, text="REGISTRAR USUARIO", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=50, y=20)

        # ****** Label ID Crear Usuario ****** #

        Label(frameCrearUsuario, text="Identificador: ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=70)
        self.ident = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.ident.place(x=50, y=110)

        # ****** Label Nombre Crear Usuario ****** #

        Label(frameCrearUsuario, text="Nombre: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=70)
        self.nombre = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.nombre.place(x=350, y=110)

        # ****** Label Apellido Crear Usuario ****** #

        Label(frameCrearUsuario, text="Apellido: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=150)
        self.apell = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.apell.place(x=50, y=190)

        # ****** Label Telefono Crear Usuario ****** #

        Label(frameCrearUsuario, text="Telefono: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=150)
        self.tel = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.tel.place(x=350, y=190)

        # ****** Label Direccion Crear Usuario ****** #

        Label(frameCrearUsuario, text="Direccion ", font=("comic sans MS", 16, "bold"), bg="#18344A",fg="white").place(x=50, y=230)
        self.dir = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.dir.place(x=50, y=270)

        # ****** Label Cargo Crear Usuario ****** #

        Label(frameCrearUsuario, text="Cargo ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=350, y=230)
        self.rolPass = ttk.Combobox(frameCrearUsuario, font=("comic sans MS",13), state="readonly", justify=CENTER)
        self.rolPass["values"] = ["vendedor","bodega","contador", "administrador"]
        self.rolPass.place(x=350,y=270)

        self.carg = self.rolPass

        # ****** Label Sueldo Crear Usuario ****** #

        Label(frameCrearUsuario, text="Sueldo ", font=("comic sans MS", 16, "bold"), bg="#18344A",fg="white").place(x=50, y=310)
        self.sueld = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.sueld.place(x=50, y=350)

        self.contraseña = self.ident

        # ****** Boton Guardar Crear Usuario ****** #

        BotonGuardar = Button(frameCrearUsuario, text="Registrar", command=self.registrar, font=("comic sans MS", 15), bd=0,cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

        # ****** Label Volver Crear Usuario ****** #

        BotonLogin = Button(frameCrearUsuario, text="Volver", command=self.volver, font=("comic sans MS", 15),bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def validacion(self):
        return (len(self.ident.get()) == 0 or len(self.carg.get()) == 0)

    def registrar(self):
        if self.validacion():
            messagebox.showinfo("error!", "Los datos son obligatorios")
        else:
            self.gestionUsuario = gestionUsuario()
            self.gestionUsuario.registrar_usuario(self.ident.get(), self.nombre.get(), self.sueld.get(),self.tel.get(),self.dir.get(), self.contraseña.get(),self.carg.get(),self.apell.get())
            self.volver()

        # ****** Para volver al login desde Crear Usuario ****** #
        def volver(self):
            self.rootRegistroUsuario.destroy()
            import GUIGestionEmpleado as ges
            ges.iniciar()

            # ****** Metodo para iniciar la interfaz desde otra ****** #

        def iniciar():
            rootRegistroUsuario = Tk()
            obj = registroUsuario(rootRegistroUsuario)
            rootRegistroUsuario.mainloop()

rootRegistroUsuario = Tk()
obj = registroUsuario(rootRegistroUsuario)
rootRegistroUsuario.mainloop()