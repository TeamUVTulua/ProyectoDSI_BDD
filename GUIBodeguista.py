# ****** Librerias Usadas ****** #

from tkinter import *
from PIL import ImageTk

# ****** Metodos de otros archivos ******#

from gestionUsuario import *
usuario=Usuario("","","","","","","","", "")

# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

# ****** Clase GUIBodeguista ****** #


class GUIBodeguista:

    def __init__(self, rootGUIBodeguista):
        self.rootGUIBodeguista = rootGUIBodeguista
        self.rootGUIBodeguista.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIBodeguista.geometry("1366x768")
        self.rootGUIBodeguista.resizable(1, 1)
        self.rootGUIBodeguista.iconbitmap("Imagenes\iconoInterfaz.ico")


        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIBodeguista, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame inicio Productos Side Der ****** #

        frameDerechoBodeguista = Frame(self.rootGUIBodeguista, bg="#18344A")
        frameDerechoBodeguista.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoBodeguista, text="Bienvenido, Bodeguista", font=("comic sans MS", 24, "bold"), bg="#18344A",fg="white").place(x=180, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoBodeguista, text="Identificador: ", font=("comic sans MS", 16,), bg="#18344A", fg="white").place( x=80, y=100)
        Label(frameDerechoBodeguista, text="Nombre: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80, y=140)
        Label(frameDerechoBodeguista, text="Apellido: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80, y=180)
        Label(frameDerechoBodeguista, text="Telefono:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80, y=300)
        Label(frameDerechoBodeguista, text="Direccion:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,y=260)
        Label(frameDerechoBodeguista, text="Cargo:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,y=220)

        # ****** Cargar datos del vendedor en el frame ****** #
        self.CargarInfoUsuarioEnLabels()
        # ****** Informacion cargada que no se modifica ****** #
        Label(frameDerechoBodeguista, text=self.id_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=270, y=100)
        Label(frameDerechoBodeguista, text=self.nombre_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=270, y=140)
        Label(frameDerechoBodeguista, text=self.apellido_usu, font=("comic sans MS", 16), bg="#18344A",
              fg="white").place(x=270, y=180)
        Label(frameDerechoBodeguista, text=self.cargo_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=270, y=220)

        self.listboxUsuario = Listbox(frameDerechoBodeguista, width=25, height=2, bg="#18344A", fg="white",
                                      font=("comic sans MS", 16,))

        self.listboxUsuario.insert(0, self.dir_usu)
        self.listboxUsuario.insert(1, self.tel_usu)

        self.listboxUsuario.place(x=270, y=260)

        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(frameDerechoBodeguista, text="Modificar datos",
                                     command=self.retornarSelecListBoxUsuario, font=("comic sans MS", 15), bg="gray",
                                     fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContrase??a = Button(frameDerechoBodeguista, text="Cambiar Contrase??a", command=self.modContrase??a,
                                        font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContrase??a.place(x=380, y=400, width=240)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoBodeguista = Frame(self.rootGUIBodeguista, bg="#18344A")
        frameIzquierdoBodeguista.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoBodeguista, text="Bodeguista", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=170, y=30)

        # ****** Boton Consultar Historico de Ventas ****** #

        BotonConsultarHV = Button(frameIzquierdoBodeguista, text="Gestionar Productos",command=self.gesInventario, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarHV.place(x=80, y=120, width=320)

        BotonSalir = Button(frameIzquierdoBodeguista, text="Cerrar Sesi??n", command=self.login, font=("comic sans MS", 15),
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
        self.contrase??a_usu = usuario.get_contrase??a()

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
                showinfo('Modificaci??n de informaci??n', 'Tus telefono quedaron: {}'.format(aux2))
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

    # ****** Metodo para iniciar la interfaz desde otra ****** #
    def login(self):
        self.rootGUIBodeguista.destroy()
        import LoginUsuario as l
        l.iniciar()

def iniciar():
     rootGUIBodeguista = Tk()
     obj = GUIBodeguista(rootGUIBodeguista)
     rootGUIBodeguista.mainloop()
