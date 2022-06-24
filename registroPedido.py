
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ****** #

from Producto import *
from gestionPedido import *
from tkinter.simpledialog import askstring

class resgistroPedido:

    def __init__(self, rootRegistroPedido):
        self.rootRegistroPedido = rootRegistroPedido
        self.rootRegistroPedido.title("Registro Pedido")
        self.rootRegistroPedido.geometry("1360x768+560+312")
        self.rootRegistroPedido.resizable(1, 1)

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootRegistroPedido, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        # ****** Frame Crear Usuario ****** #

        self.framePedidos = Frame(self.rootRegistroPedido,bg="#18344A")
        self.framePedidos.place(x=160, y=0, width=650, height=600)

        Label(self.framePedidos, text="REGISTRAR PEDIDO", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=50, y=20)

        # ****** Label ID Crear Usuario ****** #

        Label(self.framePedidos, text="Codigo: ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=70)
        self.nit = Entry(self.framePedidos, font=("comic sans MS", 16))
        self.nit.place(x=50, y=110)

        # ****** Label Nombre Crear Usuario ****** #

        Label(self.framePedidos, text="Producto: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=70)
       # self.nombre = Entry(self.framePedidos, font=("comic sans MS", 16))
       # self.nombre.place(x=350, y=110)


        #self.rolPass = ttk.Combobox(self.framePedidos, font=("comic sans MS", 13), state="readonly", justify=CENTER)
        #self.rolPass["values"] = []

        #self.rolPass.place(x=350, y=110)

        self.scrollbar = Scrollbar(self.framePedidos)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listboxPed = Listbox(self.framePedidos, width=40, heigh=1, bg="#18344A", fg="white", font=("comic sans MS", 20))
        self.listboxPed.pack()
        self.CargarInfoUsuarioEnLabels(self.listboxPed)
        self.listboxPed.place(x=350, y=110)
        # ****** Label Contactoido Crear Usuario ****** #

        Label(self.framePedidos, text="Contacto: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=150) # REVIDAR CON UN BOX SELECT
        self.Contacto = Entry(self.framePedidos, font=("comic sans MS", 16))
        self.Contacto.place(x=50, y=190)

        # ****** Label Direccionefono Crear Usuario ****** #

        Label(self.framePedidos, text="Direccion: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=150)
        self.Direccion = Entry(self.framePedidos, font=("comic sans MS", 16))
        self.Direccion.place(x=350, y=190)

        Label(self.framePedidos, text="Buscar Proveedor ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(
            x=50, y=250)

        BotonBuscar = Button(self.framePedidos, text="Buscar", command=self.busc, bd=0, cursor="hand2")
        BotonBuscar.place(x=50, y=300, width=80)



        # ****** Boton Guardar Crear Usuario ****** #

        BotonGuardar = Button(self.framePedidos, text="Registrar", command=self.registrar, font=("comic sans MS", 15), bd=0,cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

        # ****** Label Volver Crear Usuario ****** #

        BotonLogin = Button(self.framePedidos, text="Volver", command=self.volver , font=("comic sans MS", 15),bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def CargarInfoUsuarioEnLabels(self, listboxUsuario):
        gestionPed = gestionPedido()
        listaDatos = gestionPed.obtenerTodos()
        for x in listaDatos:
            listboxUsuario.insert(END, x)

    def validacion(self):
        return (len(self.nit.get()) == 0 or len(self.Contacto.get()) == 0)

    def registrar(self):
        if self.validacion():
            messagebox.showinfo("error!", "Los datos son obligatorios")
        else:
            self.gestionUsuario = gestionProducto()
            self.gestionUsuario.registrar_producto(self.nit.get(), self.nombre.get(),self.Contacto.get(),self.Direccion.get())
            self.volver()

    def busc(self):

        self.auxId = askstring('Modificación de información', 'Ingrese el identificador de un empleado')

        gestionProv = gestionProveedor()
        cons = gestionProv.buscar_info(self.auxId)
        print(cons)
        if (cons == None):
            messagebox.showinfo("Consultar", "El usuario no está registrado")
        else:
            messagebox.showinfo("Consultar", "El usuario está registrado")

        # ****** Para volver al login desde Crear Usuario ****** #
    def volver(self):
        self.rootRegistroPedido.destroy()
        import GUIGestionProducto as ges
        ges.iniciar()

            # ****** Metodo para iniciar la interfaz desde otra ****** #

def iniciar():
    rootRegistroPedido = Tk()
    obj = resgistroPedido(rootRegistroPedido)
    rootRegistroPedido.mainloop()