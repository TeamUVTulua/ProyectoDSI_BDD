# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from Usuario import *
from gestionUsuario import *
import gestionUsuario as gu
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

        Label(frameDerechoAdmin, text="Bienvenido", font=("comic sans MS", 24, "bold"), bg="#18344A",fg="white").place(x=320, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoAdmin, text="Identificador: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=60)
        Label(frameDerechoAdmin, text="Nombre: ", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80, y=100)
        Label(frameDerechoAdmin,text="Apellido: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=140)
        Label(frameDerechoAdmin, text="Telefono:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=260)
        Label(frameDerechoAdmin, text="Direccion:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=220)
        Label(frameDerechoAdmin, text="Cargo:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=180)

        self.CargarInfoUsuarioEnLabels()
        # INFORMACIO CARGADA QUE NO SE MODIFICA
        Label(frameDerechoAdmin, text=self.id_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=270, y=60)
        Label(frameDerechoAdmin, text=self.nombre_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=270, y=100)
        Label(frameDerechoAdmin, text=self.apellido_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=270, y=140)
        Label(frameDerechoAdmin, text=self.cargo_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=270, y=180)

        self.listboxUsuario = Listbox(frameDerechoAdmin, width=30, heigh=2, bg="#18344A", fg="white", font=("comic sans MS", 20,))

        self.listboxUsuario.insert(0, self.dir_usu)
        self.listboxUsuario.insert(1, self.tel_usu)

        self.listboxUsuario.place(x=270, y=220)

        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(frameDerechoAdmin, text="Modificar datos", command=self.retornarSelecListBoxUsuario, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
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

    def retornarSelecListBoxUsuario(self):
        gestionUsuarios = gestionUsuario()
        aux = self.listboxUsuario.curselection()
        if (self.listboxUsuario.selection_includes(0)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese la nueva direccion de usuario')

            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tu nombre quedó:  {}'.format(aux2))

                gestionUsuarios.modificar_direccion(aux2, self.id_usu)

                # usuario2=gestionUsuarios.login_usuario(self.email,self.contraseña)
                # usuario=usuario2
                print(aux2)

        if (self.listboxUsuario.selection_includes(1)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese la nueva telefono de usuario')
            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tus telefono quedaron: {}'.format(aux2))
                gestionUsuarios.modificar_telefono(aux2, usuario.get_id_usu())
            print(aux2)

    def CargarInfoUsuarioEnLabels(self):
        #print(usuario.get_nombre())

        self.id_usu = usuario.get_id_usu()
        self.nombre_usu = usuario.get_nombre()
        self.apellido_usu = usuario.get_apellido()
        self.cargo_usu = usuario.get_cargo()
        self.dir_usu = usuario.get_direccion()
        self.tel_usu = usuario.get_telefono()





    # ****** Metodo para iniciar la interfaz desde otra ****** #
def iniciar():
     rootGUIAdministrador = Tk()
     obj = GUIAdministrador(rootGUIAdministrador)
     rootGUIAdministrador.mainloop()
