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


        # ****** Frame inicio Productos Side Der ****** #

        frameIzquierdoCrearUsu = Frame(self.rootRegistroUsuario,bg="#18344A")
        frameIzquierdoCrearUsu.place(x=160, y=0, width=650, height=600)

        Label(frameIzquierdoCrearUsu, text="REGISTRAR USUARIO", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=50, y=20)

        # ------Row 1---

        Label(frameIzquierdoCrearUsu, text="Identificador: ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=70)
        self.ident = Entry(frameIzquierdoCrearUsu, font=("comic sans MS", 16))
        self.ident.place(x=50, y=110)

        Label(frameIzquierdoCrearUsu, text="Nombre: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=70)
        self.nombre = Entry(frameIzquierdoCrearUsu, font=("comic sans MS", 16))
        self.nombre.place(x=350, y=110)

        # ------Row 2---

        Label(frameIzquierdoCrearUsu, text="Apellido: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=150)
        self.apell = Entry(frameIzquierdoCrearUsu, font=("comic sans MS", 16))
        self.apell.place(x=50, y=190)

        Label(frameIzquierdoCrearUsu, text="Telefono: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=150)
        self.tel = Entry(frameIzquierdoCrearUsu, font=("comic sans MS", 16))
        self.tel.place(x=350, y=190)

        # ------Row 3---

        Label(frameIzquierdoCrearUsu, text="Direccion ", font=("comic sans MS", 16, "bold"), bg="#18344A",fg="white").place(x=50, y=230)
        self.dir = Entry(frameIzquierdoCrearUsu, font=("comic sans MS", 16))
        self.dir.place(x=50, y=270)

        Label(frameIzquierdoCrearUsu, text="Cargo ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=350, y=230)
        self.rolPass = ttk.Combobox(frameIzquierdoCrearUsu, font=("comic sans MS",13), state="readonly", justify=CENTER)
        self.rolPass["values"] = ["vendedor","bodega","contador", "administrador"]
        self.rolPass.place(x=350,y=270)

        self.carg = self.rolPass
        #self.carg = Entry(frameIzquierdoCrearUsu, font=("comic sans MS", 16))
        #self.carg.place(x=350, y=270)

        # ------Row 4---

        Label(frameIzquierdoCrearUsu, text="Sueldo ", font=("comic sans MS", 16, "bold"), bg="#18344A",fg="white").place(x=50, y=310)
        self.sueld = Entry(frameIzquierdoCrearUsu, font=("comic sans MS", 16))
        self.sueld.place(x=50, y=350)

        self.contraseña = self.ident

        # ------Row 5---



        # ------Row 6---
        BotonGuardar = Button(frameIzquierdoCrearUsu, text="Registrar", command=self.registrar, font=("comic sans MS", 15), bd=0,
                              cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)
        BotonLogin = Button(frameIzquierdoCrearUsu, text="Volver", command=self.volver, font=("comic sans MS", 15),
                            bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def validacion(self):
        return (len(self.ident.get()) == 0 or len(self.carg.get()) == 0) #<--

    def registrar(self):

        if self.validacion():
            messagebox.showinfo("error!", "Los datos son obligatorios")
        else:
            self.gestionUsuario = gestionUsuario()
            self.gestionUsuario.registrar_usuario(self.ident.get(), self.nombre.get(), self.sueld.get(),self.tel.get(),
                                                  self.dir.get(), self.contraseña.get(),self.carg.get(),
                                                  self.apell.get())
            self.volver()

    # Para ir al Login
    def volver(self):
        self.rootRegistroUsuario.destroy()
        import GUIGestionEmpleado as ges
        ges.iniciar()


def iniciar():
    rootRegistroUsuario = Tk()
    obj = registroUsuario(rootRegistroUsuario)
    rootRegistroUsuario.mainloop()

rootRegistroUsuario = Tk()
obj = registroUsuario(rootRegistroUsuario)
rootRegistroUsuario.mainloop()