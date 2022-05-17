# ****** Librerias Usadas ****** #
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ******#
import Proveedor as us
from gestionProveedor import *
Proveedor=us.Proveedor("","","","")
# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


# ****** Clase GUIGestionProveedor ****** #

class GUIProveedor:
    def __init__(self, rootGUIProveedor):
        self.rootGUIProveedor = rootGUIProveedor
        self.rootGUIProveedor.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIProveedor.geometry("1360x768+560+312")
        self.rootGUIProveedor.resizable(1, 1)
        self.rootGUIProveedor.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.rootGUIProveedor.attributes('-fullscreen', True)

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIProveedor, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoProv = Frame(self.rootGUIProveedor, bg="#18344A")
        frameIzquierdoProv.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoProv, text="Gestion de Proveedor", font=("comic sans MS", 23, "bold"), bg="#18344A",
              fg="white").place(x=100, y=30)

        # ****** Boton Home ******#

        BotonHome = Button(frameIzquierdoProv, text="Inicio", command=self.rootGUIProveedor.destroy,font=("comic sans MS", 15), bg="#18344A", fg="white", bd=5,
                           cursor="hand2")
        BotonHome.place(x=20, y=20, width=70, height=35)


        # ******Boton Consultar Proveedor****** #

        BotonConsultarProveedor = Button(frameIzquierdoProv, text="Consultar Proveedor",command=self.consultarEmp, font=("comic sans MS", 15),bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarProveedor.place(x=120, y=250, width=240)


        # ****** Frame inicio Proveedor Side Der ****** #
        self.frameDerechoEmp = Frame(self.rootGUIProveedor, bg="#18344A")
        self.frameDerechoEmp.place(x=600, y=85, width=700, height=530)


        # ******* Titulo Frame Proveedor ****** #
        Label(self.frameDerechoEmp, text="Proveedor", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=280, y=20)

        self.scrollbar =Scrollbar(self.frameDerechoEmp)
        self.scrollbar.pack(side=RIGHT, fill=Y)



        self.listboxUsuario = Listbox(self.frameDerechoEmp, width=33, heigh=9, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20))
        self.listboxUsuario.pack()
        #for i in range(100):
         #   self.listboxUsuario.insert(END,i)

        self.CargarInfoUsuarioEnLabels(self.listboxUsuario)

        self.listboxUsuario.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listboxUsuario.yview)


        self.listboxUsuario.place(x=50, y=86)

    def consultarEmp(self):
        self.auxId = askstring('Modificación de información', 'Ingrese el NIT del proveedor')
        self.frameDerechoEmp.place_forget()
        self.mostrarEmp()

    def mostrarEmp(self):
        frameDerechoAdmin = Frame(self.rootGUIProveedor, bg="#18344A")
        frameDerechoAdmin.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoAdmin, text=" Modificar", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=320, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoAdmin, text="NIT: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(
            x=80, y=60)
        Label(frameDerechoAdmin, text="Nombre: ", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80,
                                                                                                              y=100)
        Label(frameDerechoAdmin, text="Contacto: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,
                                                                                                                 y=140)
        Label(frameDerechoAdmin, text="Direccion:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,
                                                                                                                y=180)

        self.CargarInfoUsuarioEnLabels2()

        self.listboxUsuario = Listbox(frameDerechoAdmin, width=25, heigh=6, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20,))

        self.listboxUsuario.insert(0, self.nit)
        self.listboxUsuario.insert(1, self.nombre)
        self.listboxUsuario.insert(2, self.contacto)
        self.listboxUsuario.insert(3, self.direccion)

        self.listboxUsuario.place(x=270, y=60)

        BotonModificarDatos = Button(frameDerechoAdmin, text="Modificar datos",
                                     command=self.retornarSelecListBoxUsuario, font=("comic sans MS", 15), bg="gray",
                                     fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

    def retornarSelecListBoxUsuario(self):
        gestionUsuarios = gestionProveedor()
        aux = self.listboxUsuario.curselection()
        if (self.listboxUsuario.selection_includes(0)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese el NIT del Proveedor')

            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tu NIT quedó:  {}'.format(aux2))

                gestionUsuarios.modificar_nit(aux2, self.nit)
                print(aux2)

        if (self.listboxUsuario.selection_includes(1)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese el nuevo nombre del Proveedor')
            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tu Nombre quedó: {}'.format(aux2))
                gestionUsuarios.modificar_nombre(aux2, self.nit)
            print(aux2)

        if (self.listboxUsuario.selection_includes(2)):
            print(aux)
            aux3 = askstring('Modificación de información', 'Ingrese el nuevo contacto del proveedor')
            if (aux3 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tu contacto quedó: {}'.format(aux3))
                gestionUsuarios.modificar_contacto(aux3, self.nit)
            print(aux3)

        if (self.listboxUsuario.selection_includes(3)):
            print(aux)
            aux4 = askstring('Modificación de información', 'Ingrese la direccion del proveedor')
            if (aux4 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tus telefono quedaron: {}'.format(aux4))
                gestionUsuarios.modificar_direccion( self.nit)
            print(aux4)

    def CargarInfoUsuarioEnLabels2(self):
        gestionUsuarios = gestionProveedor()
        self.nit = gestionUsuarios.obtener_nit(self.auxId)
        self.nombre = gestionUsuarios.obtener_nombre(self.auxId)
        self.contacto = gestionUsuarios.obtener_contacto(self.auxId)
        self.direccion = gestionUsuarios.obtener_direccion(self.auxId)

    def CargarInfoUsuarioEnLabels(self, listboxUsuario):
        gestionUsuarios = gestionProveedor()
        listaDatos = gestionUsuarios.obtenerTodos()

        for x in listaDatos:
            listboxUsuario.insert(END, x)

    def login_window(self):

        self.rootGUIProveedor.destroy()
        import LoginUsuario
        
def iniciar():
    rootGUIProveedor = Tk()
    obj = GUIProveedor(rootGUIProveedor)
    rootGUIProveedor.mainloop()
