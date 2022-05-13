# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
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

        # ****** Logo de Fondo ****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGestCli, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame Botones Opciones Side Izq ****** #

        frameGUIGestCli = Frame(self.rootGestCli, bg="#18344A")
        frameGUIGestCli.place(x=85, y=85, width=480, height=530)
        Label(frameGUIGestCli, text="Gestion Cliente", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=125, y=30)

        # ****** Boton Consultar Clientes ****** #

        BotonConsultarCliente = Button(frameGUIGestCli, text="Consultar Clientes", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarCliente.place(x=120, y=120, width=240)

        # ****** Boton Crear Clientes ****** #

        BotonCrearCliente = Button(frameGUIGestCli, text="Crear Cliente", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearCliente.place(x=120, y=180, width=240)

        # ****** Boton Modificar Clientes ****** #

        BotonListarEmpleados = Button(frameGUIGestCli, text="Modificar Cliente",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonListarEmpleados.place(x=120, y=240, width=240)

        # ******Boton Listar Clientes ****** #

        BotonListarCliente = Button(frameGUIGestCli, text="Listar Clientes",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonListarCliente.place(x=120, y=300, width=240)

        # ******Boton Eliminar Cliente ****** #

        BotonEliminarCliente = Button(frameGUIGestCli, text="Eliminar Cliente", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarCliente.place(x=120, y=360, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameGUIGestCli, text="Cerrar Sesión", command=self.rootGestCli.quit, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

        # ****** Frame inicio Productos Side Der ****** #
        frameInicio = Frame(self.rootGestCli, bg="#18344A")
        frameInicio.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Cliente ****** #
        Label(frameInicio, text="Clientes", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=280, y=20)

        # ******  ****** #
def modificarEmpleado(self):
    # ****** Frame inicio Productos Side Der ****** #
    frameGestEmpl = Frame(self.rootGestCli, bg="#18344A")
    frameGestEmpl.place(x=600, y=85, width=700, height=530)
    # ******* Titulo Frame Bienvenido ****** #
    Label(frameGestEmpl, text="Bienvenido", font=("comic sans MS", 24, "bold"), bg="#18344A", fg="white").place(x=320,y=20)

    # ****** Datos del perfil ****** #
    Label(frameGestEmpl, text="ID:", font=("comic sans MS", 24,), bg="#18344A", fg="white").place(x=80,y=70)
    Label(frameGestEmpl, text="Nombre:", font=("comic sans MS", 24,), bg="#18344A", fg="white").place(x=80, y=130)
    Label(frameGestEmpl, text="Apellido1:", font=("comic sans MS", 24,), bg="#18344A", fg="white").place(x=80, y=190)
    Label(frameGestEmpl, text="Apellido2:", font=("comic sans MS", 24,), bg="#18344A", fg="white").place(x=80, y=250)
    Label(frameGestEmpl, text="Correo: ", font=("comic sans MS", 24), bg="#18344A",fg="white").place(x=80, y=310)
    Label(frameGestEmpl, text="Telefono: ", font=("comic sans MS", 24,), bg="#18344A", fg="white").place(x=80, y=370)
    Label(frameGestEmpl, text="Direccion.", font=("comic sans MS", 24,), bg="#18344A", fg="white").place(x=80, y=430)

    # ****** Boton Modificar Datos ****** #

    BotonModificarDatos = Button(frameGestEmpl, text="Modificar datos", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
    BotonModificarDatos.place(x=210, y=400, width=240)

    self.rootGestCli.destroy()


def gestionProducto(self):
    self.rootGestCli.destroy()
    import GUIGestionProducto as GesProd
    GesProd.GesProdInicio()

def Menuinicio():
    rootGestCli = Tk()
    obj = GUIGestCli(rootGestCli)
    rootGestCli.mainloop()


rootGestCli = Tk()
obj = GUIGestCli(rootGestCli)
rootGestCli.mainloop()