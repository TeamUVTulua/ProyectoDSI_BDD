# ****** Librerias Usadas ****** #

from tkinter import *
from PIL import  ImageTk

# ****** Metodos de otros archivos ******#

from gestionUsuario import *
usuario=Usuario("","","","","","","","", "")

# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

# ****** Clase GUIAdministrador ****** #

class GUIAdministrador:
    def __init__(self, rootGUIAdministrador):
        self.rootGUIAdministrador = rootGUIAdministrador
        self.rootGUIAdministrador.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIAdministrador.geometry("1366x768")
        self.rootGUIAdministrador.resizable(1, 1)
        self.rootGUIAdministrador.iconbitmap("Imagenes\iconoInterfaz.ico")

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIAdministrador, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame inicio Productos Side Der ****** #

        frameDerechoAdmin = Frame(self.rootGUIAdministrador, bg="#18344A")
        frameDerechoAdmin.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoAdmin, text="Bienvenido, Administrador", font=("comic sans MS", 24, "bold"), bg="#18344A",fg="white").place(x=160, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoAdmin, text="Identificador: ", font=("comic sans MS", 16,), bg="#18344A", fg="white").place(x=80, y=70)
        Label(frameDerechoAdmin, text="Nombre: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80, y=110)
        Label(frameDerechoAdmin,text="Apellido: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80, y=150)
        Label(frameDerechoAdmin, text="Telefono:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80, y=270)
        Label(frameDerechoAdmin, text="Direccion:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,y=230)
        Label(frameDerechoAdmin, text="Cargo:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,y=190)

        self.CargarInfoUsuarioEnLabels()
        # ******  Imformacion cargada que no se modifica ******#
        Label(frameDerechoAdmin, text=self.id_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=270, y=70)
        Label(frameDerechoAdmin, text=self.nombre_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=270, y=110)
        Label(frameDerechoAdmin, text=self.apellido_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=270, y=150)
        Label(frameDerechoAdmin, text=self.cargo_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=270, y=190)

        self.listboxUsuario = Listbox(frameDerechoAdmin, width=25, height=2, bg="#18344A", fg="white", font=("comic sans MS", 16,))

        self.listboxUsuario.insert(0, self.dir_usu)
        self.listboxUsuario.insert(1, self.tel_usu)

        self.listboxUsuario.place(x=270, y=230)

        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(frameDerechoAdmin, text="Modificar datos", command=self.retornarSelecListBoxUsuario, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContrase??a = Button(frameDerechoAdmin, text="Cambiar Contrase??a", command=self.modContrase??a, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContrase??a.place(x=380,y=400, width=240)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoAdmin = Frame(self.rootGUIAdministrador, bg="#18344A")
        frameIzquierdoAdmin.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoAdmin, text="Inicio Administrador", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=100, y=30)

        # ****** Boton Gestiones Empleados ****** #

        BotonGestionarEmpleados = Button(frameIzquierdoAdmin, text="Gestionar Empleados", command=self.gesEmpleado, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonGestionarEmpleados.place(x=120, y=120, width=240)

        # ****** Boton Gestionar Clientes ******#

        BotonGestionarClientes = Button(frameIzquierdoAdmin, text="Gestionar Clientes",command=self.gesCliente, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonGestionarClientes.place(x=120, y=180, width=240)

        # ******Boton Gestionar Inventario****** #

        BotonConsultarProducto = Button(frameIzquierdoAdmin, text="Gestionar Inventario",command=self.gesInventario, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarProducto.place(x=120, y=240, width=240)

        # ******Boton Gestionar Proveedores ****** #

        BotonListarProductos = Button(frameIzquierdoAdmin, text="Proveedores",command=self.gesProveedor, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonListarProductos.place(x=120, y=300, width=240)

        # ******Boton Consultar Historicos ****** #

        BotonEliminarProducto = Button(frameIzquierdoAdmin, text="Gestionar Pedidos", command=self.pedido,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarProducto.place(x=120, y=360, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameIzquierdoAdmin, text="Cerrar Sesi??n", command=self.login, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

    #****** Cargar Informaci??n en la Base de Datos ******#

    def pedido(self):
        self.rootGUIAdministrador.destroy()
        import GUIGestionPedido as emp
        emp.iniciar()

    def retornarSelecListBoxUsuario(self):
        gestionUsuarios = gestionUsuario()
        aux = self.listboxUsuario.curselection()
        if (self.listboxUsuario.selection_includes(0)):
            print(aux)
            aux2 = askstring('Modificaci??n de informaci??n', 'Ingrese la nueva direccion de usuario')

            if (aux2 == None):
                showinfo('Modificaci??n de informaci??n', 'No se realiz?? ningun cambio')
            else:
                showinfo('Modificaci??n de informaci??n', 'Tu direccion qued??:  {}'.format(aux2))

                gestionUsuarios.modificar_direccion(aux2, self.id_usu)
                print(aux2)

        if (self.listboxUsuario.selection_includes(1)):
            print(aux)
            aux2 = askstring('Modificaci??n de informaci??n', 'Ingrese la nueva telefono de usuario')
            if (aux2 == None):
                showinfo('Modificaci??n de informaci??n', 'No se realiz?? ningun cambio')
            else:
                showinfo('Modificaci??n de informaci??n', 'Tu telefono quedo: {}'.format(aux2))
                gestionUsuarios.modificar_telefono(aux2, usuario.get_id_usu())
            print(aux2)

    def modContrase??a(self):
        gestionUsuarios=gestionUsuario()
        nuevaContrase??a=""
        confirNuevaContra=""
        contrase??aActual = askstring('Cambiar contrase??a', 'Escribe tu contrase??a actual')
        if(contrase??aActual==self.contrase??a_usu):
            nuevaContrase??a=askstring('Cambiar contrase??a', 'Escribe tu nueva contrase??a')
            if (contrase??aActual==nuevaContrase??a):
                showinfo('Cambiar contrase??a','La contrase??a es igual a la antigua, trata con otra')
            else:
                confirNuevaContra=askstring('Cambiar contrase??a', 'Confirma tu nueva contrase??a')
                if(nuevaContrase??a==confirNuevaContra):
                    showinfo('Cambiar contrase??a','Cambio exitoso, vuelve a hacer login')
                    gestionUsuarios.cambiar_contrase??a(confirNuevaContra, usuario.get_contrase??a(),usuario.get_id_usu())
                    self.login()
                else:
                    showinfo('Cambiar contrase??a','Las contrase??as no coinciden')
        if(contrase??aActual==None):
                showinfo('Modificaci??n de informaci??n','No se realiz?? ningun cambio')
        else:
            showinfo('Cambiar contrase??a','Contrase??a incorrecta')

    def login_window(self):

        self.rootGUIAdministrador.destroy()
        import LoginUsuario

    def CargarInfoUsuarioEnLabels(self):

        self.id_usu = usuario.get_id_usu()
        self.nombre_usu = usuario.get_nombre()
        self.apellido_usu = usuario.get_apellido()
        self.cargo_usu = usuario.get_cargo()
        self.dir_usu = usuario.get_direccion()
        self.tel_usu = usuario.get_telefono()
        self.contrase??a_usu = usuario.get_contrase??a()

    def gesEmpleado(self):
        self.rootGUIAdministrador.destroy()
        import GUIGestionEmpleado as emp
        emp.iniciar()

    def gesInventario(self):
        self.rootGUIAdministrador.destroy()
        import GUIGestionProducto as emp
        emp.iniciar(usuario.get_cargo())

    def gesCliente(self):
        self.rootGUIAdministrador.destroy()
        import GUIGestionCliente as emp
        emp.iniciar(usuario.get_cargo())

    def gesProveedor(self):
        self.rootGUIAdministrador.destroy()
        import GUIGestionProveedor as emp
        emp.iniciar()

    def login(self):
        self.rootGUIAdministrador.destroy()
        import LoginUsuario as l
        l.iniciar()

    # ****** Metodo para iniciar la interfaz desde otra ****** #
def iniciar():
     rootGUIAdministrador = Tk()
     obj = GUIAdministrador(rootGUIAdministrador)
     rootGUIAdministrador.mainloop()