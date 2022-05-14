# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ******#



# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

# ****** Clase GUIVendedor ****** #

class GUIVendedor:

    def __init__(self, rootGUIVendedor):
        self.rootGUIVendedor = rootGUIVendedor
        self.rootGUIVendedor.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIVendedor.geometry("1360x768+560+312")
        self.rootGUIVendedor.resizable(1, 1)
        self.rootGUIVendedor.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.rootGUIVendedor.attributes('-fullscreen',True)

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIVendedor, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame inicio Productos Side Der ****** #

        frameDerechoVendedor = Frame(self.rootGUIVendedor, bg="#18344A")
        frameDerechoVendedor.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoVendedor, text="Bienvenido, Vendedor", font=("comic sans MS", 24, "bold"), bg="#18344A",fg="white").place(x=180, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoVendedor, text="Identificador: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=100)
        Label(frameDerechoVendedor, text="Nombre: ", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80, y=140)
        Label(frameDerechoVendedor,text="Apellido: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=180)
        Label(frameDerechoVendedor, text="Telefono:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=220)
        Label(frameDerechoVendedor, text="Direccion:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=260)
        Label(frameDerechoVendedor, text="Cargo:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=300)


        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(frameDerechoVendedor, text="Modificar datos", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContraseña = Button(frameDerechoVendedor, text="Cambiar Contraseña", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContraseña.place(x=380,y=400, width=240)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoVendedor = Frame(self.rootGUIVendedor, bg="#18344A")
        frameIzquierdoVendedor.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoVendedor, text="Vendedor", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=170, y=30)

        # ****** Boton Crear Venta ****** #

        BotonCrearVenta = Button(frameIzquierdoVendedor, text="Crear Venta", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearVenta.place(x=120, y=120, width=240)

        # ****** Boton Consultar Venta ******#

        BotonConsultarVenta = Button(frameIzquierdoVendedor, text="Consultar Venta", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarVenta.place(x=120, y=180, width=240)

        # ****** Boton Modificar Venta ****** #

        BotonModificarVenta = Button(frameIzquierdoVendedor, text="Modificar Venta",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarVenta.place(x=120, y=240, width=240)

        # ******Boton Listar Ventas ****** #

        BotonListarVentas = Button(frameIzquierdoVendedor, text="Listar Ventas",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonListarVentas.place(x=120, y=300, width=240)

        # ******Boton Modificar Cliente ****** #

        BotonModificarClientes = Button(frameIzquierdoVendedor, text="Modificar Cliente", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarClientes.place(x=120, y=360, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameIzquierdoVendedor, text="Cerrar Sesión", command=self.rootGUIVendedor.quit, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

    # ****** Metodo para iniciar la interfaz desde otra ****** #

def iniciar():
     rootGUIVendedor = Tk()
     obj = GUIVendedor(rootGUIVendedor)
     rootGUIVendedor.mainloop()

rootGUIVendedor = Tk()
obj = GUIVendedor(rootGUIVendedor)
rootGUIVendedor.mainloop()