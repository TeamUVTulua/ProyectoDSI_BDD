# ****** Librerias Usadas ****** #

from tkinter import *
from PIL import  ImageTk

# ****** Metodos de otros archivos ******#

from Usuario import *
import Cliente as us
from gestionCliente import *
cliente=us.Cliente("","","","","","","","")

# ****** Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


# ****** Clase GUIGestCli ****** #

class GUIGestCli:
    def __init__(self, rootGestCli, cargo):
        self.rootGestCli = rootGestCli
        self.cargo = cargo
        self.rootGestCli.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGestCli.geometry("1366x768")
        self.rootGestCli.resizable(1, 1)
        self.rootGestCli.iconbitmap("Imagenes\iconoInterfaz.ico")


        # ****** Logo de Fondo ****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGestCli, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)



        # ****** Frame Botones Opciones Side Izq ****** #

        frameIzquierdoCli = Frame(self.rootGestCli, bg="#18344A")
        frameIzquierdoCli.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoCli, text="Gestion Cliente", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=125, y=30)

        # ****** Boton Home ******#

        BotonHome = Button(frameIzquierdoCli, text="Inicio", command=self.volver ,font=("comic sans MS", 15), bg="#18344A", fg="white", bd=5, cursor="hand2")
        BotonHome.place(x=30, y=30, width=70,height=35)

        # ****** Boton Consultar Clientes ****** #

        BotonConsultarCliente = Button(frameIzquierdoCli, text="Consultar Clientes",command=self.consultarCliente, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarCliente.place(x=120, y=120, width=240)

        # ****** Boton Crear Clientes ****** #

        BotonCrearCliente = Button(frameIzquierdoCli, text="Crear Cliente", command=self.crear,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearCliente.place(x=120, y=180, width=240)

        # ******Boton Eliminar Cliente ****** #

        BotonEliminarCliente = Button(frameIzquierdoCli, text="Eliminar Cliente", command=self.eliminar, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarCliente.place(x=120, y=240, width=240)

        # ******Boton Habilitar Cliente ****** #

        BotonHabilitarCliente = Button(frameIzquierdoCli, text="Habilitar Cliente", command=self.habilitar ,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonHabilitarCliente.place(x=120, y=300, width=240)



        # ****** Frame inicio Productos Side Der ****** #

        self.frameDerechoCli = Frame(self.rootGestCli, bg="#18344A")
        self.frameDerechoCli.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Cliente ****** #

        Label(self.frameDerechoCli, text="Clientes", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=280, y=20)

        self.scrollbar = Scrollbar(self.frameDerechoCli)
        self.scrollbar.pack(side=BOTTOM, fill=X)

        # ****** Datos del perfil ****** #

        self.listboxUsuario = Listbox(self.frameDerechoCli, width=45, height=9, bg="#18344A", fg="white",
                                      font=("comic sans MS", 16))

        self.CargarInfoUsuarioEnLabels(self.listboxUsuario)

        self.listboxUsuario.config(xscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listboxUsuario.yview, orient='horizontal')

        self.listboxUsuario.place(x=35, y=86)

        # ****** Boton Modificar Datos ****** #

    def consultarCliente(self):
        self.auxId = askstring('Modificación de información', 'Ingrese el NIT de un Cliente')
        self.frameDerechoCli.place_forget()
        self.mostrarCli()

    def mostrarCli(self):
        frameDerechoAdmin = Frame(self.rootGestCli, bg="#18344A")
        frameDerechoAdmin.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoAdmin, text=" Modificar", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=320, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoAdmin, text="NIT: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80, y=60)
        Label(frameDerechoAdmin, text="Nombre: ", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80,
                                                                                                              y=100)
        Label(frameDerechoAdmin, text="Apellido 1: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                                 y=140)
        Label(frameDerechoAdmin, text="Apellido 2:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                                y=180)
        Label(frameDerechoAdmin, text="Tipo Cliente :", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                                 y=220)
        Label(frameDerechoAdmin, text="Direccion Calle:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                             y=260)
        Label(frameDerechoAdmin, text="Direccion Numero:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
                                                                                                            x=80,y=300)

        self.CargarInfoUsuarioEnLabels2()

        self.listboxUsuario = Listbox(frameDerechoAdmin, width=20, height=7, bg="#18344A", fg="white",
                                      font=("comic sans MS", 16))

        self.listboxUsuario.insert(0, self.nit_cli)
        self.listboxUsuario.insert(1, self.nom_cli)
        self.listboxUsuario.insert(2, self.apePa_cli)
        self.listboxUsuario.insert(3, self.apeMa_cli)
        self.listboxUsuario.insert(4, self.tipo_cli)
        self.listboxUsuario.insert(5, self.dirCa_cli)
        self.listboxUsuario.insert(6, self.dirNu_cli)

        self.listboxUsuario.place(x=320, y=66)

        BotonModificarDatos = Button(frameDerechoAdmin, text="Modificar datos",
                                     command=self.retornarSelecListBoxUsuario, font=("comic sans MS", 15), bg="gray",
                                     fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)
    
    def retornarSelecListBoxUsuario(self):
        gestionUsuarios = gestionCliente()
        aux = self.listboxUsuario.curselection()
        try:
            if (self.listboxUsuario.selection_includes(0)):
                print(aux)

                aux2 = askstring('Modificación de información', 'Ingrese el NIT de cliente')
                aux2.iconbitmap("Imagenes\iconoInterfaz.ico")

                if (aux2 == None):
                    showinfo('Modificación de información', 'No se realizó ningun cambio')
                else:
                    gestionUsuarios.modificar_nit(aux2, self.nit_cli)
                    showinfo('Modificación de información', 'El nit del cliente quedó: {}'.format(aux2))
                    print(aux2)
                    self.rootGestCli.destroy()
                    iniciar(self.cargo)
        except:
            showinfo('Error', 'El NIT ya está registrado')

        if (self.listboxUsuario.selection_includes(1)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese el nuevo nombre de cliente')
            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'El nombre del cliente es: {}'.format(aux2))
                gestionUsuarios.modificar_nombre(aux2, self.nit_cli)
                self.rootGestCli.destroy()
                iniciar(self.cargo)

        if (self.listboxUsuario.selection_includes(2)):
            print(aux)
            aux3 = askstring('Modificación de información', 'Ingrese el nuevo Apellido Paterno de cliente')
            if (aux3 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'El apellido paterno es : {}'.format(aux3))
                gestionUsuarios.modificar_apellido1(aux3, self.nit_cli)
                self.rootGestCli.destroy()
                iniciar(self.cargo)

        if (self.listboxUsuario.selection_includes(3)):
            print(aux)
            aux4 = askstring('Modificación de información', 'Ingrese el Apellido Materno de cliente')
            if (aux4 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tu apellido materno es: {}'.format(aux4))
                gestionUsuarios.modificar_apellido2(aux4, self.nit_cli)
                self.rootGestCli.destroy()
                iniciar(self.cargo)

        if (self.listboxUsuario.selection_includes(4)):
            print(aux)
            aux5 = askstring('Modificación de información', 'Ingrese el tipo de cliente')
            if (aux5 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'El tipo de cliente cambio a: {}'.format(aux5))
                gestionUsuarios.modificar_telefono(aux5, self.nit_cli)
                self.rootGestCli.destroy()
                iniciar(self.cargo)

        if (self.listboxUsuario.selection_includes(5)):
            print(aux)
            aux6 = askstring('Modificación de información', 'Ingrese la nueva Direccion Calle de cliente')
            if (aux6 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'La Direccion Calle quedo: {}'.format(aux6))
                gestionUsuarios.modificar_dirCalle(aux6, self.nit_cli)
                self.rootGestCli.destroy()
                iniciar(self.cargo)

        if (self.listboxUsuario.selection_includes(6)):
            print(aux)
            aux6 = askstring('Modificación de información', 'Ingrese la nueva Direccion Numero de cliente')
            if (aux6 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'La direccion Numero quedo: {}'.format(aux6))
                gestionUsuarios.modificar_dirNum(aux6, self.nit_cli)
                self.rootGestCli.destroy()
                iniciar(self.cargo)

    def CargarInfoUsuarioEnLabels2(self):
        gestionUsuarios = gestionCliente()
        self.nit_cli = gestionUsuarios.obtener_nit(self.auxId)
        self.nom_cli = gestionUsuarios.obtener_nombre(self.auxId)
        self.apePa_cli = gestionUsuarios.obtener_apellidoPaterno(self.auxId)
        self.apeMa_cli = gestionUsuarios.obtener_apellidoMaterno(self.auxId)
        self.tipo_cli = gestionUsuarios.obtener_tipo(self.auxId)
        self.dirCa_cli = gestionUsuarios.obtener_dirCalle(self.auxId)
        self.dirNu_cli = gestionUsuarios.obtener_dirNumero(self.auxId)

    def crear(self):
        self.rootGestCli.destroy()
        import registroCliente as reg
        reg.iniciar(self.cargo)

    def CargarInfoUsuarioEnLabels(self, listboxUsuario):
        gestionUsuarios =gestionCliente()
        listaDatos = gestionUsuarios.obtenerTodos()

        for x in listaDatos:
            listboxUsuario.insert(END, x)

    def volver(self):
        self.rootGestCli.destroy()
        print (self.cargo)
        if (self.cargo == "administrador"):
            import  GUIAdministrador as adm
            adm.iniciar()

        if (self.cargo == "vendedor"):
            import  GUIVendedor as adm
            adm.iniciar()

        if (self.cargo == "bodega"):
            import  GUIBodeguista as adm
            adm.iniciar()

        if (self.cargo == "contador"):
            import  GUIContador as adm
            adm.iniciar()


    def eliminar(self):
        self.auxId = askstring('Eliminar Cliente', 'Ingrese el nit de un cliente')
        gestionClientes = gestionCliente()
        gestionClientes.deshabilitar_usuario(self.auxId )
        self.rootGestCli.destroy()
        iniciar(self.cargo)

    def habilitar(self):
        self.auxId = askstring('Habilitar Cliente', 'Ingrese el nit de un cliente')
        gestionClientes = gestionCliente()
        gestionClientes.habilitar_usuario(self.auxId )
        self.rootGestCli.destroy()
        iniciar()

def gestionProducto(self):
    self.rootGestCli.destroy()
    import GUIGestionProducto as GesProd
    GesProd.GesProdInicio()

def iniciar(cargo):
    rootGestCli = Tk()
    obj = GUIGestCli(rootGestCli,cargo)
    rootGestCli.mainloop()
