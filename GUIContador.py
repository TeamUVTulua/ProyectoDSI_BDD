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

# ****** Clase GUIContador ****** #


class GUIContador:

    def __init__(self, rootGUIContador):
        self.rootGUIContador = rootGUIContador
        self.rootGUIContador.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIContador.geometry("1360x768+560+312")
        self.rootGUIContador.resizable(1, 1)
        self.rootGUIContador.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.rootGUIContador.attributes('-fullscreen', True)


        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIContador, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame inicio Productos Side Der ****** #

        frameDerechoContador = Frame(self.rootGUIContador, bg="#18344A")
        frameDerechoContador.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoContador, text="Bienvenido, Contador", font=("comic sans MS", 24, "bold"), bg="#18344A",fg="white").place(x=180, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoContador, text="Identificador: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place( x=80, y=100)
        Label(frameDerechoContador, text="Nombre: ", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80, y=140)
        Label(frameDerechoContador, text="Apellido: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=180)
        Label(frameDerechoContador, text="Telefono:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=220)
        Label(frameDerechoContador, text="Direccion:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=260)
        Label(frameDerechoContador, text="Cargo:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=300)


        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(frameDerechoContador, text="Modificar datos", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContraseña = Button(frameDerechoContador, text="Cambiar Contraseña", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContraseña.place(x=380,y=400, width=240)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoContador = Frame(self.rootGUIContador, bg="#18344A")
        frameIzquierdoContador.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoContador, text="Contador", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=170, y=30)

        Home = ImageTk.PhotoImage(file='Imagenes\iconoInterfazinicio.png')
        HomeTamaño = P.subsample(3,3)
        BotonHome = Button(frameIzquierdoContador, text="inicio" , image=HomeTamaño)
        BotonHome.place(x=40, y=40)

        # ****** Boton Consultar Historico de Ventas ****** #

        BotonConsultarHV = Button(frameIzquierdoContador, text="Consultar Historico de Venta", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarHV.place(x=80, y=120, width=320)

        # ****** Boton Consultar Historico de Compras ******#

        BotonConsultarHC = Button(frameIzquierdoContador, text="Consultar Historico de Compras", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarHC.place(x=80, y=180, width=320)

        # ****** Boton Consultar Datos Empleados ****** #

        BotonConsultarDatosEmp = Button(frameIzquierdoContador, text="Consultar Datos  Empleados",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarDatosEmp.place(x=80, y=240, width=320)

        # ******Boton Crear Pago a Empleados ****** #

        BotonCrearPagoEmp = Button(frameIzquierdoContador, text="Crear Pago a Empleados",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearPagoEmp.place(x=80, y=300, width=320)

        # ******Boton Crear Pago a Proveedores ****** #

        BotonCrearPagoProv = Button(frameIzquierdoContador, text="Crear Pago a Proveedores", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearPagoProv.place(x=80, y=360, width=320)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameIzquierdoContador, text="Cerrar Sesión", command=self.rootGUIContador.destroy, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=80, y=420, width=320)

    # ****** Metodo para iniciar la interfaz desde otra ****** #

def iniciar():
     rootGUIContador = Tk()
     obj = GUIContador(rootGUIContador)
     rootGUIContador.mainloop()


rootGUIContador = Tk()
obj = GUIContador(rootGUIContador)
rootGUIContador.mainloop()