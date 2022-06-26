# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk

# ****** Metodos de otros archivos ******#

from gestionUsuario import *
import gestionUsuario as gu
usuario=Usuario("","","","","","","","","")

# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

# ****** Clase GUIContador ****** #


class GUIContador:

    def __init__(self, rootGUIContador):
        self.rootGUIContador = rootGUIContador
        self.rootGUIContador.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIContador.geometry("1366x768")
        self.rootGUIContador.resizable(1, 1)
        self.rootGUIContador.iconbitmap("Imagenes\iconoInterfaz.ico")


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
        Label(frameDerechoContador, text="Telefono:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=300)
        Label(frameDerechoContador, text="Direccion:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=260)
        Label(frameDerechoContador, text="Cargo:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=220)

        # -------- CARGAR DATOS DEL VENDEDOR EN EL FRAME
        self.CargarInfoUsuarioEnLabels()
        # INFORMACIO CARGADA QUE NO SE MODIFICA
        Label(frameDerechoContador, text=self.id_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(
            x=270, y=100)
        Label(frameDerechoContador, text=self.nombre_usu, font=("comic sans MS", 20,), bg="#18344A",
              fg="white").place(
            x=270, y=140)
        Label(frameDerechoContador, text=self.apellido_usu, font=("comic sans MS", 20,), bg="#18344A",
              fg="white").place(x=270, y=180)
        Label(frameDerechoContador, text=self.cargo_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(
            x=270, y=220)

        self.listboxUsuario = Listbox(frameDerechoContador, width=25, heigh=2, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20,))

        self.listboxUsuario.insert(0, self.dir_usu)
        self.listboxUsuario.insert(1, self.tel_usu)

        self.listboxUsuario.place(x=270, y=260)

        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(frameDerechoContador, text="Modificar datos",
                                     command=self.retornarSelecListBoxUsuario,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContraseña = Button(frameDerechoContador, text="Cambiar Contraseña",
                                        command=self.modContraseña,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContraseña.place(x=380,y=400, width=240)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoContador = Frame(self.rootGUIContador, bg="#18344A")
        frameIzquierdoContador.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoContador, text="Contador", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=170, y=30)

        # DESCOMENTAR

        #Home = ImageTk.PhotoImage(file='Imagenes\iconoInterfazinicio.png')
        #HomeTamaño = P.subsample(3,3)
        #BotonHome = Button(frameIzquierdoContador, text="inicio" , image=HomeTamaño)
        #BotonHome.place(x=40, y=40)

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

        BotonSalir = Button(frameIzquierdoContador, text="Cerrar Sesión", command=self.login, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=80, y=420, width=320)

    # ****** Metodo para iniciar la interfaz desde otra ****** #
    def CargarInfoUsuarioEnLabels(self):
        # print(usuario.get_nombre())

        self.id_usu = usuario.get_id_usu()
        self.nombre_usu = usuario.get_nombre()
        self.apellido_usu = usuario.get_apellido()
        self.cargo_usu = usuario.get_cargo()
        self.dir_usu = usuario.get_direccion()
        self.tel_usu = usuario.get_telefono()
        self.contraseña_usu = usuario.get_contraseña()

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

    def modContraseña(self):
        gestionUsuarios=gestionUsuario()
        nuevaContraseña=""
        confirNuevaContra=""
        contraseñaActual = askstring('Cambiar contraseña', 'Escribe tu contraseña actual')
        if(contraseñaActual==self.contraseña_usu):
            nuevaContraseña=askstring('Cambiar contraseña', 'Escribe tu nueva contraseña')
            if (contraseñaActual==nuevaContraseña):
                showinfo('Cambiar contraseña','La contraseña es igual a la antigua, trata con otra')
            else:
                confirNuevaContra=askstring('Cambiar contraseña', 'Confirma tu nueva contraseña')
                if(nuevaContraseña==confirNuevaContra):
                    showinfo('Cambiar contraseña','Cambio exitoso, vuelve a hacer login')
                    gestionUsuarios.cambiar_contraseña(confirNuevaContra, usuario.get_contraseña(),usuario.get_id_usu())
                    self.login()
                else:
                    showinfo('Cambiar contraseña','Las contraseñas no coinciden')
        if(contraseñaActual==None):
                showinfo('Modificación de información','No se realizó ningun cambio')
        else:
            showinfo('Cambiar contraseña','Contraseña incorrecta')
    # ****** Metodo para iniciar la interfaz desde otra ****** #

    def login(self):
        self.rootGUIContador.destroy()
        import LoginUsuario as l
        l.iniciar()

def iniciar():
     rootGUIContador = Tk()
     obj = GUIContador(rootGUIContador)
     rootGUIContador.mainloop()
