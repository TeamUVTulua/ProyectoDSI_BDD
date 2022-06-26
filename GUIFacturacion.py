import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

from gestionFactura import *
from gestionProducto import *
from gestionPedido import *

class GUIFacturacion:
    def __init__(self, rootGUIFacturacion, codFac):
        self.codFac = codFac
        self.rootGUIFacturacion = rootGUIFacturacion
        self.rootGUIFacturacion.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIFacturacion.geometry("1360x768+560+312")
        self.rootGUIFacturacion.resizable(1, 1)
        self.rootGUIFacturacion.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.rootGUIFacturacion.attributes('-fullscreen', True)


        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIFacturacion, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 # ****** Frame Crear Usuario ****** #

        frameCrearFactura = Frame(self.rootGUIFacturacion,bg="#18344A")
        frameCrearFactura.place(x=350, y=75, width=650, height=600)

        Label(frameCrearFactura, text="CREAR VENTA", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=190, y=20)

        # ****** Label ID Crear Usuario ****** #

        Label(frameCrearFactura, text="Codigo: ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=70)
        self.codigo = Entry(frameCrearFactura, font=("comic sans MS", 16))
        self.codigo.place(x=50, y=110)

        # ****** Label Nombre Crear Usuario ****** #

        Label(frameCrearFactura, text="Producto: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=70)

        self.rolPass = ttk.Combobox(frameCrearFactura, font=("comic sans MS", 13), state="readonly", justify=CENTER)

        self.rolPass["values"]
        self.CargarInfoUsuarioEnLabels(self.rolPass)

        self.rolPass.place(x=350, y=110)

        # ****** Label  Crear Usuario ****** #

        Label(frameCrearFactura, text="Codigo de factura: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=150)
        codi = tkinter.StringVar()
        codi.set(self.codFac)



        Label(frameCrearFactura, text=codi.get(), font=("comic sans MS", 16, ), bg="white",
              fg="black").place(x=50, y=190)

        Label(frameCrearFactura, text="Precio Unidad:" , font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=270)

        gesPed = gestionPedido()
        #self.precio = gesPed.obtener_precioCompra(self.rolPass.get())
        print (self.rolPass.get())

        prec = tkinter.StringVar()
        #prec.set(self.precio)

        Label(frameCrearFactura, text=prec.get(), font=("comic sans MS", 16,), bg="white",
              fg="black").place(x=50, y=310)

        self.categoria = self.rolPass

        # ****** Label Crear Factura ****** #

        Label(frameCrearFactura, text="Cantidad Venta: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=150)
        self.cantidad = Entry(frameCrearFactura, font=("comic sans MS", 16))
        self.cantidad.place(x=350, y=190)




        # ****** Boton Guardar Crear Usuario ****** #

        BotonGuardar = Button(frameCrearFactura, text="Facturar", font=("comic sans MS", 15), bd=0,cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

        # ****** Label Volver Crear Usuario ****** #

        BotonLogin = Button(frameCrearFactura, text="Cancelar", font=("comic sans MS", 15) ,bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def CargarInfoUsuarioEnLabels(self, lista):
        gestionFac = gestionFactura()
        listaDatos = gestionFac.obtenerTodosId()
        self.rolPass["values"] = listaDatos

def iniciar(codFac):
    rootGUIFacturacion = Tk()
    obj = GUIFacturacion(rootGUIFacturacion, codFac)
    rootGUIFacturacion.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
