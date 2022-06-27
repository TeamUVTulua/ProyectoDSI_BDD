
from tkinter import *
from tkinter import ttk
from PIL import  ImageTk

# ****** Metodos de otros archivos ****** #

from gestionPedido import *
from tkinter.simpledialog import askstring

class resgistroPedido:

    def __init__(self, rootRegistroPedido):
        self.rootRegistroPedido = rootRegistroPedido
        self.rootRegistroPedido.title("Registro Pedido")
        self.rootRegistroPedido.geometry("1366x768")
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

        self.rolPass = ttk.Combobox(self.framePedidos, font=("comic sans MS", 13), state="readonly", justify=CENTER)

        self.rolPass["values"]
        self.CargarInfoUsuarioEnLabels(self.rolPass)

        self.rolPass.place(x=350, y=110)

        # ****** Label Contactoido Crear Usuario ****** #

        Label(self.framePedidos, text="Valor compra: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=280)
        self.Contacto = Entry(self.framePedidos, font=("comic sans MS", 16))
        self.Contacto.place(x=350, y=320)

        # ****** Label Direccionefono Crear Usuario ****** #

        Label(self.framePedidos, text="Cantidad: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=180)
        self.Direccion = Entry(self.framePedidos, font=("comic sans MS", 16))
        self.Direccion.place(x=350, y=220)

        Label(self.framePedidos, text="Proveedor: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=180)

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
            cantidad = int(self.Contacto.get())
            precio = int(self.Direccion.get())
            precioTotal = cantidad * precio
            self.gestionPed.registrar_pedido(self.nit.get(), self.rolPass.get(), self.rolPassProv.get(), self.Contacto.get(), self.Direccion.get(), precioTotal)
            self.volver()

    def busc(self):

        self.auxId = askstring('Modificación de información', 'Ingrese el identificador de un pedido')

        gestionPed = gestionPedido()
        cons = gestionPed.buscar_info(self.auxId)
        print(cons)
        if (cons == None):
            messagebox.showinfo("Consultar", "El pedido no se ha realizado ")
        else:
            messagebox.showinfo("Consultar", "El pedido ya fue realizado")

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