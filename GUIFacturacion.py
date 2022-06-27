# ****** Librerias Usadas ****** #
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk

# ****** Metodos de otros archivos ****** #
from gestionFactura import *
from gestionPedido import *
from gestionVenta import *

# ****** Clase GUIFacturacion ****** #
class GUIFacturacion:
    def __init__(self, rootGUIFacturacion, codFac, emp):
        self.emp =emp
        self.codFac = codFac
        self.rootGUIFacturacion = rootGUIFacturacion
        self.rootGUIFacturacion.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIFacturacion.geometry("1366x768")
        self.rootGUIFacturacion.resizable(1, 1)
        self.rootGUIFacturacion.iconbitmap("Imagenes\iconoInterfaz.ico")

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIFacturacion, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

 # ****** Frame Crear Usuario ****** #

        self.frameCrearFactura = Frame(self.rootGUIFacturacion,bg="#18344A")
        self.frameCrearFactura.place(x=350, y=75, width=650, height=600)

        Label(self.frameCrearFactura, text="CREAR VENTA", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=190, y=20)

        # ****** Label ID Crear Usuario ****** #

        Label(self.frameCrearFactura, text="Codigo: ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=70)
        self.codigo = Entry(self.frameCrearFactura, font=("comic sans MS", 16))
        self.codigo.place(x=50, y=110)

        # ****** Label Nombre Crear Usuario ****** #

        Label(self.frameCrearFactura, text="Producto: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=70)

        self.rolPass = ttk.Combobox(self.frameCrearFactura, font=("comic sans MS", 13), state="readonly", justify=CENTER)

        self.rolPass["values"]
        self.CargarInfoUsuarioEnLabels(self.rolPass)

        self.rolPass.place(x=350, y=110)


        # ****** Label  Crear Usuario ****** #

        Label(self.frameCrearFactura, text="Codigo de factura: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=150)
        codi = tkinter.StringVar()
        codi.set(self.codFac)


        Label(self.frameCrearFactura, text=codi.get(), font=("comic sans MS", 16, ), bg="white",
              fg="black").place(x=50, y=190)

        Label(self.frameCrearFactura, text="Precio Unidad:" , font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=270)

        Label(self.frameCrearFactura, text="Precio Total:", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=270)

        prec = tkinter.StringVar()

        botonAgregar = Button(self.frameCrearFactura, text="+", command=self.agr, font=("comic sans MS", 10, "bold"),
                              bd=0, cursor="hand2")
        botonAgregar.place(x=580, y=110, width=25)



        self.categoria = self.rolPass

        # ****** Label Crear Factura ****** #

        Label(self.frameCrearFactura, text="Cantidad Venta: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=150)
        self.cantidad = Entry(self.frameCrearFactura, font=("comic sans MS", 16))
        self.cantidad.place(x=350, y=190)


        # ****** Boton Guardar Crear factura ****** #

        BotonGuardar = Button(self.frameCrearFactura, text="Facturar", command = self.facturar, font=("comic sans MS", 15), bd=0,cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

        # ****** Label Volver Crear Usuario ****** #

        BotonLogin = Button(self.frameCrearFactura, text="Terminar", command = self.terminar, font=("comic sans MS", 15) ,bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def terminar(self):
        self.rootGUIFacturacion.destroy()
        import GUIFactura as fac
        fac.iniciar(self.codFac, self.emp)


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
        self.precioT= self.precio2 * cant
        Label(self.frameCrearFactura, text=self.precioT, font=("comic sans MS", 16,), bg="white", fg="black").place(x=350, y=310)

    def facturar(self):
        gestVen = gestionVenta()
        print(self.codigo.get())
        print(self.rolPass.get())
        print(self.codFac)
        print(self.cantidad.get())
        print(self.precio2)
        gestVen.registrar_venta(self.codigo.get(), self.rolPass.get(), self.codFac, self.cantidad.get(), self.precio2, self.precioT)
        self.rootGUIFacturacion.destroy()
        iniciar(self.codFac, self.emp)

    def CargarInfoUsuarioEnLabels(self, lista):
        gestionFac = gestionFactura()
        listaDatos = gestionFac.obtenerTodosId()
        self.rolPass["values"] = listaDatos

def iniciar(codFac,emp):
    rootGUIFacturacion = Tk()
    obj = GUIFacturacion(rootGUIFacturacion, codFac, emp)
    rootGUIFacturacion.mainloop()
