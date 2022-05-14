# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk

# ****** Metodos de otros archivos ******#



# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

# ****** Clase GUIBodeguista ****** #
from GUIVendedor import rootGUIVendedor


class GUIBodeguista:

    def __init__(self, rootGUIBodeguista):
        self.rootGUIBodeguista = rootGUIBodeguista
        self.rootGUIBodeguista.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIBodeguista.geometry("1360x768+560+312")
        self.rootGUIBodeguista.resizable(1, 1)
        self.rootGUIBodeguista.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.rootGUIBodeguista.attributes('-fullscreen', True)


        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIBodeguista, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame inicio Productos Side Der ****** #

        frameDerechoBodeguista = Frame(self.rootGUIBodeguista, bg="#18344A")
        frameDerechoBodeguista.place(x=600, y=85, width=700, height=530)
        BotonHome = Button(self.rootGUIBodeguista, text="inicio", image="iconoInterfazinicio.png")

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoBodeguista, text="Bienvenido, Bodeguista", font=("comic sans MS", 24, "bold"), bg="#18344A",fg="white").place(x=180, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoBodeguista, text="Identificador: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place( x=80, y=100)
        Label(frameDerechoBodeguista, text="Nombre: ", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80, y=140)
        Label(frameDerechoBodeguista, text="Apellido: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=180)
        Label(frameDerechoBodeguista, text="Telefono:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=220)
        Label(frameDerechoBodeguista, text="Direccion:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=260)
        Label(frameDerechoBodeguista, text="Cargo:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=300)


        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(frameDerechoBodeguista, text="Modificar datos", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContraseña = Button(frameDerechoBodeguista, text="Cambiar Contraseña", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContraseña.place(x=380,y=400, width=240)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoBodeguista = Frame(self.rootGUIBodeguista, bg="#18344A")
        frameIzquierdoBodeguista.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoBodeguista, text="Contador", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=170, y=30)

        # ****** Boton Consultar Historico de Ventas ****** #

        BotonConsultarHV = Button(frameIzquierdoBodeguista, text="Consultar Historico de Venta", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarHV.place(x=80, y=120, width=320)

        # ****** Boton Consultar Historico de Compras ******#

        BotonConsultarHC = Button(frameIzquierdoBodeguista, text="Consultar Historico de Compras", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarHC.place(x=80, y=180, width=320)

        # ****** Boton Consultar Datos Empleados ****** #

        BotonConsultarDatosEmp = Button(frameIzquierdoBodeguista, text="Consultar Datos  Empleados",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarDatosEmp.place(x=80, y=240, width=320)

        # ******Boton Crear Pago a Empleados ****** #

        BotonCrearPagoEmp = Button(frameIzquierdoBodeguista, text="Crear Pago a Empleados",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearPagoEmp.place(x=80, y=300, width=320)

        # ******Boton Crear Pago a Proveedores ****** #

        BotonCrearPagoProv = Button(frameIzquierdoBodeguista, text="Crear Pago a Proveedores", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearPagoProv.place(x=80, y=360, width=320)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameIzquierdoBodeguista, text="Cerrar Sesión", command=self.rootGUIBodeguista.destroy, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=80, y=420, width=320)

    # ****** Metodo para iniciar la interfaz desde otra ****** #

def iniciar():
     rootGUIBodeguista = Tk()
     obj = GUIBodeguista(rootGUIBodeguista)
     rootGUIBodeguista.mainloop()


rootGUIBodeguista = Tk()
obj = GUIBodeguista(rootGUIBodeguista)
rootGUIBodeguista.mainloop()