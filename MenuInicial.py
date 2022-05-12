# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ******#

# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


# ****** Clase GUIMenuInicial ****** #

class GUIMenuInicial:
    def __init__(self, rootMenuInicial):
        self.rootMenuInicial = rootMenuInicial
        self.rootMenuInicial.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootMenuInicial.geometry("1360x768+560+312")
        self.rootMenuInicial.resizable(1, 1)
        self.rootMenuInicial.iconbitmap("Imagenes\iconoInterfaz.ico")

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootMenuInicial, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame inicio Productos Side Der ****** #
        frameInicio = Frame(self.rootMenuInicial, bg="#18344A")
        frameInicio.place(x=600, y=85, width=700, height=530)
        # ******* Titulo Frame Bienvenido ****** #
        Label(frameInicio, text="Bienvenido", font=("comic sans MS", 24, "bold"), bg="#18344A", fg="white").place(x=320, y=20)

        # ****** Datos del perfil ****** #
        Label(frameInicio, text="Hola, Administrador", font=("comic sans MS", 24,), bg="#18344A", fg="white").place(x=80, y=70)
        Label(frameInicio, text="Correo: Administrador@motosocios.com", font=("comic sans MS", 24), bg="#18344A", fg="white").place(x=80, y=130)
        Label(frameInicio, text="Telefono: ", font=("comic sans MS", 24,), bg="#18344A", fg="white").place(x=80, y=190)
        Label(frameInicio, text="Direccion", font=("comic sans MS", 24,), bg="#18344A", fg="white").place(x=80, y=250)
        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(frameInicio, text="Modificar datos", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContraseña = Button(frameInicio, text="Cambiar Contraseña", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContraseña.place(x=380,y=400, width=240)



        # ******Frame Botones Opciones Side Izq ****** #

        frameMenuInicial = Frame(self.rootMenuInicial, bg="#18344A")
        frameMenuInicial.place(x=85, y=85, width=480, height=530)
        Label(frameMenuInicial, text="Inicio Administrador", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=100, y=30)

        # ****** Boton Gestiones Empleados ****** #

        BotonGestionarEmpleados = Button(frameMenuInicial, text="Gestionar Empleados", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonGestionarEmpleados.place(x=120, y=120, width=240)

        # ****** Boton Gestionar Clientes ******#

        BotonGestionarClientes = Button(frameMenuInicial, text="Gestionar Clientes", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonGestionarClientes.place(x=120, y=180, width=240)

        # ******Boton Gestionar Inventario****** #

        BotonConsultarProducto = Button(frameMenuInicial, text="Gestionar Inventario",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarProducto.place(x=120, y=240, width=240)

        # ******Boton Gestionar Proveedores ****** #

        BotonListarProductos = Button(frameMenuInicial, text="Gestionar Proveedores",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonListarProductos.place(x=120, y=300, width=240)

        # ******Boton Consultar Historicos ****** #

        BotonEliminarProducto = Button(frameMenuInicial, text="Consultar Historicos", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarProducto.place(x=120, y=360, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameMenuInicial, text="Cerrar Sesión", command=self.rootMenuInicial.quit, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

def gestionProducto(self):
    self.rootMenuInicial.destroy()
    import GUIGestionProducto as GesProd
    GesProd.GesProdInicio()

def Menuinicio():
    rootMenuInicial = Tk()
    obj = GUIMenuInicial(rootMenuInicial)
    rootMenuInicial.mainloop()


rootMenuInicial = Tk()
obj = GUIMenuInicial(rootMenuInicial)
rootMenuInicial.mainloop()
