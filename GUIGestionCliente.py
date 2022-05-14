# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk

import self
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ******#

# ****** Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


# ****** Clase GUIGestCli ****** #

class GUIGestCli:
    def __init__(self, rootGestCli):
        self.rootGestCli = rootGestCli
        self.rootGestCli.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGestCli.geometry("1360x768+560+312")
        self.rootGestCli.resizable(1, 1)
        self.rootGestCli.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.rootGestCli.attributes('-fullscreen', True)

        # ****** Logo de Fondo ****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGestCli, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame Botones Opciones Side Izq ****** #

        frameIzquierdoCli = Frame(self.rootGestCli, bg="#18344A")
        frameIzquierdoCli.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoCli, text="Gestion Cliente", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=125, y=30)

        # ****** Boton Consultar Clientes ****** #

        BotonConsultarCliente = Button(frameIzquierdoCli, text="Consultar Clientes", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarCliente.place(x=120, y=120, width=240)

        # ****** Boton Crear Clientes ****** #

        BotonCrearCliente = Button(frameIzquierdoCli, text="Crear Cliente", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearCliente.place(x=120, y=180, width=240)

        # ****** Boton Modificar Clientes ****** #

        BotonListarEmpleados = Button(frameIzquierdoCli, text="Modificar Cliente",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonListarEmpleados.place(x=120, y=240, width=240)

        # ******Boton Listar Clientes ****** #

        BotonListarCliente = Button(frameIzquierdoCli, text="Listar Clientes",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonListarCliente.place(x=120, y=300, width=240)

        # ******Boton Eliminar Cliente ****** #

        BotonEliminarCliente = Button(frameIzquierdoCli, text="Eliminar Cliente", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarCliente.place(x=120, y=360, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameIzquierdoCli, text="Cerrar Sesión", command=self.rootGestCli.destroy, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

        # ****** Frame inicio Productos Side Der ****** #
        frameDerechoCli = Frame(self.rootGestCli, bg="#18344A")
        frameDerechoCli.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Cliente ****** #
        Label(frameDerechoCli, text="Clientes", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=280, y=20)

        # ****** Datos del perfil ****** #
        Label(frameDerechoCli, text="ID:", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80,y=70)
        Label(frameDerechoCli, text="Nombre:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=110)
        Label(frameDerechoCli, text="Apellido1:", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80, y=160)
        Label(frameDerechoCli, text="Apellido2:", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80, y=210)
        Label(frameDerechoCli, text="Correo: ", font=("comic sans MS", 20), bg="#18344A",fg="white").place(x=80, y=260)
        Label(frameDerechoCli, text="Telefono: ", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80, y=310)
        Label(frameDerechoCli, text="Direccion:", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80, y=360)

        # ****** Boton Modificar Datos ****** #

        BotonModificarDatos = Button(frameDerechoCli, text="Modificar datos", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=210, y=430, width=240)

def gestionProducto(self):
    self.rootGestCli.destroy()
    import GUIGestionProducto as GesProd
    GesProd.GesProdInicio()

def login_window(self):
    self.rootGUIAdministrador.destroy()
    import LoginUsuario

def iniciar():
    rootGestCli = Tk()
    obj = GUIGestCli(rootGestCli)
    rootGestCli.mainloop()

