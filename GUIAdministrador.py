# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from Usuario import *
usuario=Usuario("","","","","","","","")

# ****** Metodos de otros archivos ******#

# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


# ****** Clase GUIAdministrador ****** #

class GUIAdministrador:
    def __init__(self, rootGUIAdministrador):
        self.rootGUIAdministrador = rootGUIAdministrador
        self.rootGUIAdministrador.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIAdministrador.geometry("1360x768+560+312")
        self.rootGUIAdministrador.resizable(1, 1)
        self.rootGUIAdministrador.iconbitmap("Imagenes\iconoInterfaz.ico")

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIAdministrador, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame inicio Productos Side Der ****** #

        frameDerechoAdmin = Frame(self.rootGUIAdministrador, bg="#18344A")
        frameDerechoAdmin.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoAdmin, text="Bienvenido", font=("comic sans MS", 20, "bold"), bg="#18344A",fg="white").place(x=320, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoAdmin, text="Identificador: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=60)
        Label(frameDerechoAdmin, text="Nombre: ", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80, y=100)
        Label(frameDerechoAdmin,text="Apellido: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=140)
        Label(frameDerechoAdmin, text="Telefono:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=180)
        Label(frameDerechoAdmin, text="Direccion:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=220)
        Label(frameDerechoAdmin, text="Cargo:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=260)

        self.CargarInfoUsuarioEnLabels()
        # INFORMACIO CARGADA QUE NO SE MODIFICA
        Label(frameAdministrador, text=self.iid, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=270, y=60)
        Label(frameAdministrador, text=self.nnn, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=270, y=100)
        #Label(frameAdministrador, text=self.ape, font=("times new roman", 13), bg="khaki3", fg="black").place(x=150, y=140)
        #Label(frameAdministrador, text=self.carg, font=("times new roman", 13), bg="khaki3", fg="black").place(x=150, y=180)
        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(frameDerechoAdmin, text="Modificar datos", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContraseña = Button(frameDerechoAdmin, text="Cambiar Contraseña", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContraseña.place(x=380,y=400, width=240)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoAdmin = Frame(self.rootGUIAdministrador, bg="#18344A")
        frameIzquierdoAdmin.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoAdmin, text="Inicio Administrador", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=100, y=30)

        # ****** Boton Gestiones Empleados ****** #

        BotonGestionarEmpleados = Button(frameIzquierdoAdmin, text="Gestionar Empleados", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonGestionarEmpleados.place(x=120, y=120, width=240)

        # ****** Boton Gestionar Clientes ******#

        BotonGestionarClientes = Button(frameIzquierdoAdmin, text="Gestionar Clientes", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonGestionarClientes.place(x=120, y=180, width=240)

        # ******Boton Gestionar Inventario****** #

        BotonConsultarProducto = Button(frameIzquierdoAdmin, text="Gestionar Inventario",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarProducto.place(x=120, y=240, width=240)

        # ******Boton Gestionar Proveedores ****** #

        BotonListarProductos = Button(frameIzquierdoAdmin, text="Gestionar Proveedores",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonListarProductos.place(x=120, y=300, width=240)

        # ******Boton Consultar Historicos ****** #

        BotonEliminarProducto = Button(frameIzquierdoAdmin, text="Consultar Historicos", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarProducto.place(x=120, y=360, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameIzquierdoAdmin, text="Cerrar Sesión", command=self.rootGUIAdministrador.quit, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

    #****** Cargar Información en la Base de Datos ******#

    def CargarInfoUsuarioEnLabels(self):
        #print(usuario.get_nombre())

        self.iid = usuario.get_id_usu()
        #self.nnn = usuario.get_nombre()


    # ****** Metodo para iniciar la interfaz desde otra ****** #
def iniciar():
     rootGUIAdministrador = Tk()
     obj = GUIAdministrador(rootGUIAdministrador)
     rootGUIAdministrador.mainloop()
