
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from datetime import datetime

from gestionFactura import *
from gestionProducto import *
from gestionPedido import *
from gestionVenta import *
from gestionCliente import *
from Usuario import *


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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 # ****** Frame Crear Usuario ****** #

        self.frameCrearFactura = Frame(self.rootGUIFactura,bg="#18344A")
        self.frameCrearFactura.place(x=350, y=75, width=650, height=600)

        Label(self.frameCrearFactura, text="Factura", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=190, y=20)

        # ****** Label ID Crear Usuario ****** #

        #Label(self.frameCrearFactura, text="Codigo: ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=70)
        #self.codigo = Entry(self.frameCrearFactura, font=("comic sans MS", 16))
        #self.codigo.place(x=50, y=110)

        # ****** Label Nombre Crear Usuario ****** #

        Label(self.frameCrearFactura, text="Fecha: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=320, y=70)

        self.fecha = datetime.today()

        Label(self.frameCrearFactura, text=self.fecha, font=("comic sans MS", 16,), bg="white",
              fg="black").place(x=320, y=110)

        #self.rolPass = ttk.Combobox(self.frameCrearFactura, font=("comic sans MS", 13), state="readonly", justify=CENTER)

        #self.rolPass["values"]
        #self.CargarInfoUsuarioEnLabels(self.rolPass)

        #self.rolPass.place(x=350, y=110)


        # ****** Label  Crear Usuario ****** #

        Label(self.frameCrearFactura, text="Codigo de factura: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=70)
        codi = tkinter.StringVar()
        codi.set(self.codFac)


        Label(self.frameCrearFactura, text=codi.get(), font=("comic sans MS", 16, ), bg="white",
              fg="black").place(x=50, y=110)

        prec = tkinter.StringVar()
        #prec.set(self.precio)
        #self.categoria = self.rolPass

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

        BotonGuardar = Button(self.frameCrearFactura, text="Facturar", command = self.facturar, font=("comic sans MS", 15), bd=0,cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

        # ****** Label Volver Crear Usuario ****** #

        BotonLogin = Button(self.frameCrearFactura, text="Terminar", command = self.terminar, font=("comic sans MS", 15) ,bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def terminar(self):
        self.rootGUIFactura.destroy()

    def cambio(self):
        print(self.monto.get())
        mont = float(self.monto.get())


        self.cambio2 = mont - self.total
        Label(self.frameCrearFactura, text=self.cambio2, font=("comic sans MS", 16,), bg="white", fg="black").place(x=320,
                                                                                                              y=350)

    def agr(self):
        gesPed = gestionPedido()
        precio = gesPed.obtener_precioCompra(self.rolPass.get())
        print("**")
        print(self.rolPass.get())
        res = float('.'.join(str(ele) for ele in precio))
        self.precio2 = res * 1.15
        Label(self.frameCrearFactura, text= self.precio2, font=("comic sans MS", 16,), bg="white",
              fg="black").place(x=50, y=310)

        botonAgregar2 = Button(self.frameCrearFactura, text="+", command=self.agr2, font=("comic sans MS", 10, "bold"),
                               bd=0, cursor="hand2")
        botonAgregar2.place(x=620, y=190, width=25)

    def agr2(self):
        print("aqui")
        print(self.cantidad.get())
        cant=float(self.cantidad.get())
        precioT= self.precio2 * cant
        print (precioT)
        Label(self.frameCrearFactura, text=precioT, font=("comic sans MS", 16,), bg="white", fg="black").place(x=350, y=310)

    def client(self):
        gest = gestionCliente()
        isCli = gest.buscar_info(self.clie.get())

        if (isCli == None):
            self.rootGUIVendedor.destroy()
            import GUIFacturacion as emp
            emp.iniciar(fact, usuario.get_id_usu())
        else:
            gestionFac = gestionFactura()
            gestionFac.registrar(self.fecha, self.rolPass.get(), self.total, self.cambio2, self.emp, self.clie.get(), self.monto.get(), self.codFac)


    def facturar(self):
        gestVen = gestionVenta()
        print("---")
        print(self.codigo.get())
        print(self.rolPass.get())
        print(self.codFac)
        print(self.cantidad.get())
        print(self.precio2)
        gestVen.registrar_venta(self.codigo.get(), self.rolPass.get(), self.codFac, self.cantidad.get(), self.precio2)
        self.rootGUIFactura.destroy()
        iniciar(self.codFac)

    def CargarInfoUsuarioEnLabels(self, lista):
        gestionFac = gestionFactura()
        listaDatos = gestionFac.obtenerTodosId()
        self.rolPass["values"] = listaDatos

def iniciar(codFac, emp):
    rootGUIFactura = Tk()
    obj = GUIFactura(rootGUIFactura, codFac, emp)
    rootGUIFactura.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
