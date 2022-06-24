# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk

# ****** Metodos de otros archivos ******#

from gestionUsuario import *
import gestionUsuario as gu
usuario=Usuario("","","","","","","","", "")

# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

# ****** Clase GUIBodeguista ****** #


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

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoBodeguista, text="Bienvenido, Bodeguista", font=("comic sans MS", 24, "bold"), bg="#18344A",fg="white").place(x=180, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoBodeguista, text="Identificador: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place( x=80, y=100)
        Label(frameDerechoBodeguista, text="Nombre: ", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80, y=140)
        Label(frameDerechoBodeguista, text="Apellido: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=180)
        Label(frameDerechoBodeguista, text="Telefono:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80, y=300)
        Label(frameDerechoBodeguista, text="Direccion:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=260)
        Label(frameDerechoBodeguista, text="Cargo:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,y=220)

        # -------- CARGAR DATOS DEL VENDEDOR EN EL FRAME
        self.CargarInfoUsuarioEnLabels()
        # INFORMACIO CARGADA QUE NO SE MODIFICA
        Label(frameDerechoBodeguista, text=self.id_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(
            x=270, y=100)
        Label(frameDerechoBodeguista, text=self.nombre_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(
            x=270, y=140)
        Label(frameDerechoBodeguista, text=self.apellido_usu, font=("comic sans MS", 20,), bg="#18344A",
              fg="white").place(x=270, y=180)
        Label(frameDerechoBodeguista, text=self.cargo_usu, font=("comic sans MS", 20,), bg="#18344A", fg="white").place(
            x=270, y=220)

        self.listboxUsuario = Listbox(frameDerechoBodeguista, width=25, heigh=2, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20,))

        self.listboxUsuario.insert(0, self.dir_usu)
        self.listboxUsuario.insert(1, self.tel_usu)

        self.listboxUsuario.place(x=270, y=260)

        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(frameDerechoBodeguista, text="Modificar datos",
                                     command=self.retornarSelecListBoxUsuario, font=("comic sans MS", 15), bg="gray",
                                     fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContraseña = Button(frameDerechoBodeguista, text="Cambiar Contraseña", command=self.modContraseña,
                                        font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContraseña.place(x=380, y=400, width=240)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoBodeguista = Frame(self.rootGUIBodeguista, bg="#18344A")
        frameIzquierdoBodeguista.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoBodeguista, text="Bodeguista", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=170, y=30)

        # ****** Boton Consultar Historico de Ventas ****** #

        BotonConsultarHV = Button(frameIzquierdoBodeguista, text="Gestionar Productos",command=self.gesInventario, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarHV.place(x=80, y=120, width=320)

        BotonSalir = Button(frameIzquierdoBodeguista, text="Cerrar Sesión", command=self.login, font=("comic sans MS", 15),
                            bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

    def gesInventario(self):
        self.rootGUIBodeguista.destroy()
        import GUIGestionProducto as emp
        emp.iniciar(usuario.get_cargo())

    def login(self):
        self.rootGUIBodeguista.destroy()
        import LoginUsuario as l
        l.iniciar()

    def CargarInfoUsuarioEnLabels(self):

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
        self.rootGUIBodeguista.destroy()
        import LoginUsuario as l
        l.iniciar()

def iniciar():
     rootGUIBodeguista = Tk()
     obj = GUIBodeguista(rootGUIBodeguista)
     rootGUIBodeguista.mainloop()
