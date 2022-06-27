# ****** Librerias Usadas ****** #
from tkinter import *
from PIL import ImageTk

# ****** Metodos de otros archivos ******#
import Proveedor as us
from gestionProveedor import *
Proveedor=us.Proveedor("","","","", "")
# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


# ****** Clase GUIGestionProveedor ****** #

class GUIProveedor:
    def __init__(self, rootGUIProveedor):
        self.rootGUIProveedor = rootGUIProveedor
        self.rootGUIProveedor.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIProveedor.geometry("1366x768")
        self.rootGUIProveedor.resizable(1, 1)
        self.rootGUIProveedor.iconbitmap("Imagenes\iconoInterfaz.ico")

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIProveedor, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoProv = Frame(self.rootGUIProveedor, bg="#18344A")
        frameIzquierdoProv.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoProv, text="Gestion de Proveedor", font=("comic sans MS", 23, "bold"), bg="#18344A",
              fg="white").place(x=100, y=30)

        # ****** Boton Home ******#

        BotonHome = Button(frameIzquierdoProv, text="Inicio",command=self.volver,font=("comic sans MS", 15), bg="#18344A", fg="white", bd=5,
                           cursor="hand2")
        BotonHome.place(x=20, y=20, width=70, height=35)


        # ******Boton Consultar Proveedor****** #

        BotonConsultarProveedor = Button(frameIzquierdoProv, text="Consultar Proveedor",command=self.consultarEmp, font=("comic sans MS", 15),bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarProveedor.place(x=120, y=120, width=240)

        # ******Boton Crear Proveedor****** #
        BotonCrearProveedor = Button(frameIzquierdoProv, text="Crear Proveedor", command=self.crear, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearProveedor.place(x=120, y=180, width=240)

        # ******Boton Eliminar Proveedor ****** #

        BotonEliminarProveedor = Button(frameIzquierdoProv, text="Eliminar Cliente", command=self.eliminar, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarProveedor.place(x=120, y=240, width=240)


        # ******Boton Habilitar Proveedor****** #

        BotonHabilitarProveedor = Button(frameIzquierdoProv, text="Eliminar Cliente", command=self.eliminar, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonHabilitarProveedor.place(x=120, y=240, width=240)


        # ****** Frame inicio Proveedor Side Der ****** #
        self.frameDerechoEmp = Frame(self.rootGUIProveedor, bg="#18344A")
        self.frameDerechoEmp.place(x=600, y=85, width=700, height=530)


        # ******* Titulo Frame Proveedor ****** #
        Label(self.frameDerechoEmp, text="Proveedor", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=280, y=20)

        self.scrollbarProv = Scrollbar(self.frameDerechoEmp)
        self.scrollbarProv.pack(side=RIGHT, fill=Y)

        self.scrollbar =Scrollbar(self.frameDerechoEmp)
        self.scrollbar.pack(side=RIGHT, fill=Y)



        self.listboxUsuario = Listbox(self.frameDerechoEmp, width=33, heigh=9, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20))
        self.listboxUsuario.pack()

        self.CargarInfoUsuarioEnLabels(self.listboxUsuario)

        self.listboxUsuario.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listboxUsuario.yview)

        self.listboxUsuario.config(yscrollcommand=self.scrollbarProv.set)
        self.scrollbarProv.config(command=self.listboxUsuario.yview)

        self.listboxUsuario.place(x=50, y=86)

    def crear(self):
        self.rootGUIProveedor.destroy()
        import registroProveedor as reg
        reg.iniciar()

    def eliminar(self):
        self.auxId = askstring('Eliminar Cliente', 'Ingrese el nit de un cliente')
        gestionProv = gestionProveedor()
        gestionProv.deshabilitar_usuario(self.auxId )
        self.rootGUIProveedor.destroy()
        iniciar()

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

        Label(frameDerechoAdmin, text="NIT: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80, y=60)
        Label(frameDerechoAdmin, text="Nombre: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                              y=100)
        Label(frameDerechoAdmin, text="Contacto: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                                 y=140)
        Label(frameDerechoAdmin, text="Direccion:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                                y=180)

        self.CargarInfoUsuarioEnLabels2()

        self.listboxUsuario = Listbox(frameDerechoAdmin, width=25, height=6, bg="#18344A", fg="white",
                                      font=("comic sans MS", 16))

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
        try:
            if (self.listboxUsuario.selection_includes(0)):
                aux2 = askstring('Modificación de información', 'Ingrese el NIT del Proveedor')

                if (aux2 == None):
                    showinfo('Modificación de información', 'No se realizó ningun cambio')
                else:
                    showinfo('Modificación de información', 'El nuevo NIT quedó:  {}'.format(aux2))
                    gestionUsuarios.modificar_nit(aux2, self.nit)
                    self.rootGUIProveedor.destroy()
                    iniciar()
        except:
            showinfo('Error', 'El NIT ya está registrado')

        if (self.listboxUsuario.selection_includes(1)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese el nuevo nombre del Proveedor')
            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'El nuevo Nombre del proveedor quedo: {}'.format(aux2))
                gestionUsuarios.modificar_nombre(aux2, self.nit)
                self.rootGUIProveedor.destroy()
                iniciar()

        if (self.listboxUsuario.selection_includes(2)):
            print(aux)
            aux3 = askstring('Modificación de información', 'Ingrese el nuevo contacto del proveedor')
            if (aux3 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'El nuevo  contacto del proveedor quedó: {}'.format(aux3))
                gestionUsuarios.modificar_contacto(aux3, self.nit)
                self.rootGUIProveedor.destroy()
                iniciar()

        if (self.listboxUsuario.selection_includes(3)):
            print(aux)
            aux4 = askstring('Modificación de información', 'Ingrese la direccion del proveedor')
            if (aux4 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'La nueva direccion del proveedor es: {}'.format(aux4))
                gestionUsuarios.modificar_direccion( self.nit)
                self.rootGUIProveedor.destroy()
                iniciar()

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

    def volver(self):
        self.rootGUIProveedor.destroy()
        import  GUIAdministrador as adm
        adm.iniciar()
        
def iniciar():
    rootGUIProveedor = Tk()
    obj = GUIProveedor(rootGUIProveedor)
    rootGUIProveedor.mainloop()
