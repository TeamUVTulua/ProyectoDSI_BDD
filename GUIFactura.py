# ****** Librerias Usadas ****** #
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from datetime import datetime

# ****** Metodos de Otros Archivos ****** #
from gestionFactura import *
from gestionPedido import *
from gestionVenta import *
from gestionCliente import *
from gestionUsuario import *

# ****** Clase GUIFactura ****** #
class GUIFactura:
    def __init__(self, rootGUIFactura, codFac, emp):
        self.emp = emp
        self.codFac = codFac
        self.rootGUIFactura = rootGUIFactura
        self.rootGUIFactura.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIFactura.geometry("1366x768")
        self.rootGUIFactura.resizable(1, 1)
        self.rootGUIFactura.iconbitmap("Imagenes\iconoInterfaz.ico")


        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIFactura, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

 # ****** Frame Crear Usuario ****** #

        self.frameCrearFactura = Frame(self.rootGUIFactura,bg="#18344A")
        self.frameCrearFactura.place(x=350, y=75, width=650, height=600)

        Label(self.frameCrearFactura, text="Factura", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=190, y=18)


        # ****** Label Crear Factura ****** #

        Label(self.frameCrearFactura, text="Fecha: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=320, y=70)

        self.fecha = datetime.today()

        Label(self.frameCrearFactura, text=self.fecha, font=("comic sans MS", 16,), bg="white",
              fg="black").place(x=320, y=110)

        # ****** Label  Crear Factura ****** #

        Label(self.frameCrearFactura, text="Codigo de factura: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=70)
        codi = tkinter.StringVar()
        codi.set(self.codFac)


        Label(self.frameCrearFactura, text=codi.get(), font=("comic sans MS", 16, ), bg="white",
              fg="black").place(x=50, y=110)

        prec = tkinter.StringVar()

        # ****** Label Crear Factura ****** #

        Label(self.frameCrearFactura, text="Descuento: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=150)
        self.cantidad = Entry(self.frameCrearFactura, font=("comic sans MS", 16, ), width = 10)
        self.cantidad.place(x=50, y=190)

        Label(self.frameCrearFactura, text="Tipo de Pago: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=320, y=150)

        self.rolPass = ttk.Combobox(self.frameCrearFactura, font=("comic sans MS", 13), state="readonly", justify=CENTER)
        self.rolPass["values"] = ["Efectivo", "Tarjeta"]
        self.rolPass.place(x=320, y=190)

        Label(self.frameCrearFactura, text="Valor Final: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=230)

        gestionVen = gestionVenta()
        tot = gestionVen.total(self.codFac)
        res = float('.'.join(str(ele) for ele in tot))
        self.total = int(res)

        Label(self.frameCrearFactura, text = self.total, font=("comic sans MS", 16, ), bg="white",fg="black").place(x=50, y=270)

        Label(self.frameCrearFactura, text="Monto de Pago: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=320, y=230)

        self.monto = Entry(self.frameCrearFactura, font=("comic sans MS", 16,), width=10)
        self.monto.place(x=320, y=270)

        Label(self.frameCrearFactura, text="Cliente: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=390)

        self.clie = Entry(self.frameCrearFactura, font=("comic sans MS", 16,), width=10)
        self.clie.place(x=50, y=430)

        botonAgregar3 = Button(self.frameCrearFactura, text="+", command=self.client,
                               font=("comic sans MS", 10, "bold"),
                               bd=0, cursor="hand2")
        botonAgregar3.place(x=270, y=430, width=25)


        botonAgregar2 = Button(self.frameCrearFactura, text="+", command=self.cambio, font=("comic sans MS", 10, "bold"),
                               bd=0, cursor="hand2")
        botonAgregar2.place(x=620, y=270, width=25)


        Label(self.frameCrearFactura, text="Empleado: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=310)

        Label(self.frameCrearFactura, text=self.emp,font=("comic sans MS", 16, ), bg="white",fg="black").place(x=50, y=350)

        Label(self.frameCrearFactura, text="Cambio: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=320, y=310)


        # ****** Boton Guardar Crear Usuario ****** #



        # ****** Label Volver Crear Usuario ****** #

        BotonLogin = Button(self.frameCrearFactura, text="Terminar", command = self.terminar, font=("comic sans MS", 15) ,bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def terminar(self):
        self.rootGUIFactura.destroy()

    def cambio(self):
        print(self.monto.get())
        mont = float(self.monto.get())
        self.cambio2 = mont - self.total
        if (self.cambio2 < 0):
            messagebox.showinfo("Aviso", "El monto de pago debe ser mayor a 0")
        else:
            Label(self.frameCrearFactura, text=self.cambio2, font=("comic sans MS", 16,), bg="white", fg="black").place(x=320,
                                                                                                              y=350)

    def agr(self):
        gesPed = gestionPedido()
        precio = gesPed.obtener_precioCompra(self.rolPass.get())
        print(self.rolPass.get())
        res = float('.'.join(str(ele) for ele in precio))
        self.precio2 = res * 1.15
        Label(self.frameCrearFactura, text= self.precio2, font=("comic sans MS", 16,), bg="white",
              fg="black").place(x=50, y=310)

        botonAgregar2 = Button(self.frameCrearFactura, text="+", command=self.agr2, font=("comic sans MS", 10, "bold"),
                               bd=0, cursor="hand2")
        botonAgregar2.place(x=620, y=190, width=25)

    def agr2(self):
        print(self.cantidad.get())
        cant=float(self.cantidad.get())
        precioT= self.precio2 * cant
        print (precioT)
        Label(self.frameCrearFactura, text=precioT, font=("comic sans MS", 16,), bg="white", fg="black").place(x=350, y=310)

    def client(self):
        gest = gestionCliente()
        isCli = gest.buscar_info(self.clie.get())

        if (isCli == None):
            ges = gestionUsuario()
            cargo = ges.obtener_cargo(str(self.emp))
            res = str('.'.join(str(ele) for ele in cargo))
            print(res)
            self.frameCrearFactura.place_forget()
            self.crearCliente()

        else:
            BotonGuardar = Button(self.frameCrearFactura, text="Facturar", command=self.facturar,
                                  font=("comic sans MS", 15), bd=0, cursor="hand2")
            BotonGuardar.place(x=50, y=500, width=200)

    def crearCliente(self):
        self.crearCli = Frame(self.rootGUIFactura, bg="#18344A")
        self.crearCli.place(x=160, y=0, width=650, height=600)

        Label(self.crearCli, text="REGISTRAR CLIENTE", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=50, y=20)

        # ****** Label ID Crear Usuario ****** #

        Label(self.crearCli, text="NIT: ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=50,
                                                                                                                   y=70)
        self.ident = Entry(self.crearCli, font=("comic sans MS", 16))
        self.ident.place(x=50, y=110)

        # ****** Label Nombre Crear Usuario ****** #

        Label(self.crearCli, text="Nombre: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=70)
        self.nombre = Entry(self.crearCli, font=("comic sans MS", 16))
        self.nombre.place(x=350, y=110)

        # ****** Label Apellido Crear Usuario ****** #

        Label(self.crearCli, text="Apellido 1: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=150)
        self.apell = Entry(self.crearCli, font=("comic sans MS", 16))
        self.apell.place(x=50, y=190)

        # ****** Label Telefono Crear Usuario ****** #

        Label(self.crearCli, text="Apellido 2: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=150)
        self.tel = Entry(self.crearCli, font=("comic sans MS", 16))
        self.tel.place(x=350, y=190)

        # ****** Label Direccion Crear Usuario ****** #

        Label(self.crearCli, text="Direccion Numero ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(
            x=350, y=230)
        self.rolPass = ttk.Combobox(self.crearCli, font=("comic sans MS", 13), state="readonly", justify=CENTER)
        self.rolPass["values"] = ["Esporadico", "Habitual"]
        self.rolPass.place(x=50, y=270)

        # ****** Label Cargo Crear Usuario ****** #

        Label(self.crearCli, text="Tipo Cliente ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(
            x=50, y=230)
        self.dir = Entry(self.crearCli, font=("comic sans MS", 16))
        self.dir.place(x=350, y=270)

        self.carg = self.rolPass

        # ****** Label Sueldo Crear Usuario ****** #

        Label(self.crearCli, text="Direccion Calle ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=310)
        self.sueld = Entry(self.crearCli, font=("comic sans MS", 16))
        self.sueld.place(x=50, y=350)


        # ****** Boton Buscar
        # ****** Boton Guardar Crear Usuario ****** #

        BotonGuardar = Button(self.crearCli, text="Registrar", command=self.registrar, font=("comic sans MS", 15),
                              bd=0, cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

        # ****** Label Volver Crear Usuario ****** #

    def volver(self):

        self.crearCli.place_forget()
        self.frameCrearFactura.place(x=350, y=75, width=650, height=600)
        BotonGuardar = Button(self.frameCrearFactura, text="Facturar", command=self.facturar,
                              font=("comic sans MS", 15), bd=0, cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

    def validacion(self):
        return (len(self.ident.get()) == 0 or len(self.carg.get()) == 0)

    def registrar(self):
        if self.validacion():
            messagebox.showinfo("error!", "Los datos son obligatorios")
        else:
            self.gestionUsuario = gestionCliente()
            self.gestionUsuario.registrar_cliente(self.ident.get(), self.nombre.get(), self.apell.get(),self.tel.get(),self.rolPass.get(), self.dir.get(),self.sueld.get())
            self.volver()
        
    def facturar(self):
        gestionFac = gestionFactura()
        gestionFac.registrar(self.fecha, self.rolPass.get(), self.total, self.cambio2, self.emp, self.clie.get(),
                             self.monto.get(), self.codFac)
        self.rootGUIFactura.destroy()
        import GUIVendedor as ven
        ven.iniciar()

    def CargarInfoUsuarioEnLabels(self, lista):
        gestionFac = gestionFactura()
        listaDatos = gestionFac.obtenerTodosId()
        self.rolPass["values"] = listaDatos

def iniciar(codFac, emp):
    rootGUIFactura = Tk()
    obj = GUIFactura(rootGUIFactura, codFac, emp)
    rootGUIFactura.mainloop()