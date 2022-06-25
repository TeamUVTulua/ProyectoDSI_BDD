
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

        #self.frameProd = Frame(self.framePedidos, bg="white")
        #self.frameProd.place(x=350, y=110, width=120, height=50)

        #self.frameProv = Frame(self.framePedidos, bg="white")
        #self.frameProv.place(x=50, y=220, width=120, height=50)

        Label(self.framePedidos, text="REGISTRAR PEDIDO", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=50, y=20)

        # ****** Label ID Crear Usuario ****** #

        Label(self.framePedidos, text="Codigo: ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=70)
        self.nit = Entry(self.framePedidos, font=("comic sans MS", 16))
        self.nit.place(x=50, y=110)

        # ****** Label Nombre Crear Usuario ****** #

        Label(self.framePedidos, text="Producto: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=70)
        '''
        self.scrollbar = Scrollbar(self.frameProd)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listboxPed = Listbox(self.frameProd, width=10, heigh=2, bg="#18344A", fg="white", font=("comic sans MS", 12))
        self.listboxPed.pack()

        self.CargarInfoUsuarioEnLabels(self.listboxPed)

        self.listboxPed.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listboxPed.yview)

        self.listboxPed.place(x=0, y=0)
        '''
        #-------------------------------------------
        # self.nombre = Entry(self.framePedidos, font=("comic sans MS", 16))
        # self.nombre.place(x=350, y=110)

        self.rolPass = ttk.Combobox(self.framePedidos, font=("comic sans MS", 13), state="readonly", justify=CENTER)

        self.rolPass["values"]
        self.CargarInfoUsuarioEnLabels(self.rolPass)

        self.rolPass.place(x=350, y=110)

        #--------------------------
        # ****** Label Contactoido Crear Usuario ****** #

        Label(self.framePedidos, text="Precio: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=280) # REVIDAR CON UN BOX SELECT
        self.Contacto = Entry(self.framePedidos, font=("comic sans MS", 16))
        self.Contacto.place(x=350, y=320)

        # ****** Label Direccionefono Crear Usuario ****** #

        Label(self.framePedidos, text="Cantidad: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=180)
        self.Direccion = Entry(self.framePedidos, font=("comic sans MS", 16))
        self.Direccion.place(x=350, y=220)

        Label(self.framePedidos, text="Proveedor: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=180)

        '''
        self.scrollbarProv = Scrollbar(self.frameProv)
        self.scrollbarProv.pack(side=RIGHT, fill=Y)

        self.listboxProv = Listbox(self.frameProv, width=10, heigh=2, bg="#18344A", fg="white",
                                  font=("comic sans MS", 12))
        self.listboxProv.pack()

        self.CargarInfoUsuarioEnLabelsProv(self.listboxProv)

        self.listboxProv.config(yscrollcommand=self.scrollbarProv.set)
        self.scrollbarProv.config(command=self.listboxProv.yview)

        self.listboxProv.place(x=0, y=0)
        '''
        self.rolPassProv = ttk.Combobox(self.framePedidos, font=("comic sans MS", 13), state="readonly", justify=CENTER)

        self.rolPassProv["values"]
        self.CargarInfoUsuarioEnLabelsProv(self.rolPass)
        self.rolPassProv.place(x=50, y=220)
        #-----------------

        Label(self.framePedidos, text="Buscar Proveedor ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(
            x=50, y=280)

        BotonBuscar = Button(self.framePedidos, text="Buscar", command=self.busc, bd=0, cursor="hand2")
        BotonBuscar.place(x=50, y=380, width=80)



        # ****** Boton Guardar Crear Usuario ****** #

        BotonGuardar = Button(self.framePedidos, text="Registrar", command=self.registrar, font=("comic sans MS", 15), bd=0,cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

        # ****** Label Volver Crear Usuario ****** #

        BotonLogin = Button(self.framePedidos, text="Volver", command=self.volver , font=("comic sans MS", 15),bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def CargarInfoUsuarioEnLabels(self, lista):
        gestionPed = gestionPedido()
        listaDatos = gestionPed.obtenerTodosId()
        self.rolPass["values"] = listaDatos


    def CargarInfoUsuarioEnLabelsProv(self, listboxUsuario):
        gestionPed = gestionPedido()
        listaDatos = gestionPed.obtenerTodosNit()
        self.rolPassProv["values"] = listaDatos

    def validacion(self):
        return (len(self.nit.get()) == 0 or len(self.Contacto.get()) == 0)

    def registrar(self):
        if self.validacion():
            messagebox.showinfo("error!", "Los datos son obligatorios")
        else:
            self.gestionPed = gestionPedido()
            self.gestionPed.registrar_pedido(self.nit.get(), self.rolPass.get(), self.rolPassProv.get(), self.Contacto.get(), self.Direccion.get())
            self.volver()

    def busc(self):

        self.auxId = askstring('Modificación de información', 'Ingrese el identificador de un empleado')

        gestionPed = gestionPedido()
        cons = gestionPed.buscar_info(self.auxId)
        print(cons)
        if (cons == None):
            messagebox.showinfo("Consultar", "El usuario no está registrado")
        else:
            messagebox.showinfo("Consultar", "El usuario está registrado")

        # ****** Para volver al login desde Crear Usuario ****** #
    def volver(self):
        self.rootRegistroPedido.destroy()
        import GUIGestionPedido as ges
        ges.iniciar()

            # ****** Metodo para iniciar la interfaz desde otra ****** #

def iniciar():
    rootRegistroPedido = Tk()
    obj = resgistroPedido(rootRegistroPedido)
    rootRegistroPedido.mainloop()