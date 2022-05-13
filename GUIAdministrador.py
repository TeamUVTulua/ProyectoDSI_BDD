# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from Usuario import Usuario
import Usuario as us
usuario=us.Usuario("","","","","","","","")

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



        # ******* Titulo Frame Bienvenido ****** #


        # ****** Datos del perfil ****** #

        #--- UserInformationFrame

        frameAdministrador = Frame(self.rootGUIAdministrador, bg="#18344A")
        frameAdministrador.place(x=600, y=85, width=700, height=530)

        Label(frameAdministrador, text="Bienvenido", font=("comic sans MS", 20, "bold"), bg="#18344A",fg="white").place(x=320, y=20)

        Label(frameAdministrador, text="Identificador: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=60)
        Label(frameAdministrador, text="Nombre: Administrador@motosocios.com", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80, y=100)
        Label(frameAdministrador, text="Apellido: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=140)
        Label(frameAdministrador, text="Telefono:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=180)
        Label(frameAdministrador, text="Direccion:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=220)
        Label(frameAdministrador, text="Cargo:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=260)

        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(frameAdministrador, text="Modificar datos", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContraseña = Button(frameAdministrador, text="Cambiar Contraseña", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContraseña.place(x=380,y=400, width=240)

        # ******Frame Botones Opciones Side Izq ****** #

        frameGUIAdministrador = Frame(self.rootGUIAdministrador, bg="#18344A")
        frameGUIAdministrador.place(x=85, y=85, width=480, height=530)
        Label(frameGUIAdministrador, text="Inicio Administrador", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=100, y=30)

        # ****** Boton Gestiones Empleados ****** #

        BotonGestionarEmpleados = Button(frameGUIAdministrador, text="Gestionar Empleados", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonGestionarEmpleados.place(x=120, y=120, width=240)

        # ****** Boton Gestionar Clientes ******#

        BotonGestionarClientes = Button(frameGUIAdministrador, text="Gestionar Clientes", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonGestionarClientes.place(x=120, y=180, width=240)

        # ******Boton Gestionar Inventario****** #

        BotonConsultarProducto = Button(frameGUIAdministrador, text="Gestionar Inventario",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarProducto.place(x=120, y=240, width=240)

        # ******Boton Gestionar Proveedores ****** #

        BotonListarProductos = Button(frameGUIAdministrador, text="Gestionar Proveedores",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonListarProductos.place(x=120, y=300, width=240)

        # ******Boton Consultar Historicos ****** #

        BotonEliminarProducto = Button(frameGUIAdministrador, text="Consultar Historicos", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarProducto.place(x=120, y=360, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameGUIAdministrador, text="Cerrar Sesión", command=self.rootGUIAdministrador.quit, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

    #-- CARGAR INFORMACIO DE LA BD
    def CargarInfoUsuarioEnLabels(self):
        self.id_usu = usuario.get_email()
        self.id_rol = usuario.get_id_rol()
        self.contraseña = usuario.get_contraseña()
        self.id_usuario = usuario.get_id_usuario()
        self.fecha_registro = usuario.get_fecha_ingreso()
        self.nombres_usuario = usuario.get_nombre()
        self.apellidos_usuarios = usuario.get_apellido()
        self.direccion_usuario = usuario.get_direccion()
        self.tel_usuario = usuario.get_telefono()
        self.estado_usuario = usuario.get_estado()

    # ****** Metodo para iniciar la interfaz desde otra ****** #
def iniciar():
     rootGUIAdministrador = Tk()
     obj = GUIAdministrador(rootGUIAdministrador)
     rootGUIAdministrador.mainloop()

# ****** Inicio de la Interfaz ****** #
