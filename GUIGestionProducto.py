# ****** Librerias Usadas ****** #
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ******#

# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


# ****** Clase GUIGestionProducto ****** #

class GUIGestionProducto:
    def __init__(self, rootGUIRegProd):
        self.rootGUIRegProd = rootGUIRegProd
        self.rootGUIRegProd.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIRegProd.geometry("1360x768+560+312")
        self.rootGUIRegProd.resizable(1, 1)
        self.rootGUIRegProd.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.rootGUIRegProd.attributes('-fullscreen', True)

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIRegProd, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ******Frame Botones Opciones Side Izq ****** #

        frameGUIRegProd = Frame(self.rootGUIRegProd, bg="#18344A")
        frameGUIRegProd.place(x=85, y=85, width=480, height=530)
        Label(frameGUIRegProd, text="Gestion de Productos", font=("comic sans MS", 23, "bold"), bg="#18344A",
              fg="white").place(x=100, y=30)

        # ****** Boton Agregar Producto ****** #

        BotonAgregarProducto = Button(frameGUIRegProd, text="Agregar Producto", font=("comic sans MS", 15), bg="gray",fg="white", bd=5, cursor="hand2")
        BotonAgregarProducto.place(x=120, y=120, width=240)

        # ****** Boton Modificar Producto ******#

        BotonReportes = Button(frameGUIRegProd, text="Modificar Producto", font=("comic sans MS", 15), bg="gray",fg="white", bd=5, cursor="hand2")
        BotonReportes.place(x=120, y=180, width=240)

        # ******Boton Consultar Producto****** #

        BotonConsultarProducto = Button(frameGUIRegProd, text="Consultar Producto", font=("comic sans MS", 15),bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarProducto.place(x=120, y=240, width=240)

        # ******Boton Listar Productos ****** #

        BotonListarProductos = Button(frameGUIRegProd, text="Listado de Productos",font=("comic sans MS", 15),bg="gray", fg="white", bd=5, cursor="hand2")
        BotonListarProductos.place(x=120, y=300, width=240)

        # ******Boton Eliminar Producto ****** #

        BotonEliminarProducto = Button(frameGUIRegProd, text="Eliminar Producto",font=("comic sans MS", 15),bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarProducto.place(x=120, y=360, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameGUIRegProd, text="Cerrar Sesión", command=self.rootGUIRegProd.quit,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

        # ****** Frame inicio Productos Side Der ****** #
        frameInicio = Frame(self.rootGUIRegProd, bg="#18344A")
        frameInicio.place(x=600, y=85, width=700, height=530)


        # ******* Titulo Frame Producto ****** #
        Label(frameInicio, text="Productos", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=280, y=20)


def ventanaConsultarProd(self):

            self.rootGUIRegProd2=Tk()
            self.rootGUIRegProd2.title("Sistema de inventario y Ventas MotoSocios")
            self.rootGUIRegProd2.geometry("1360x768+560+312")
            self.rootGUIRegProd2.resizable(1, 1)

            frameGUIRegProd2 = Frame(self.rootGUIRegProd2,bg="#18344A")
            frameGUIRegProd2.place(x=600,y=85,width=700,height=530)

            Label(frameGUIRegProd2,text="Lista Productos", font=("comic sans MS",24, "bold"), bg="#18344A",fg="white").place(x=220,y=20)

            #****** Cargue de datos en el Side der ******#
            # Carga lista de productos

            fder=ttk.Treeview(frameGUIRegProd2, columns=(1,2,3,4,5,6,7),show="headings",height="18")
            fder.place(x=45,width=600,y=80)
            treeScrollBary=ttk.Scrollbar(frameGUIRegProd2, orient="vertical",command=fder.yview)
            treeScrollBarx=ttk.Scrollbar(frameGUIRegProd2, orient="horizontal",command=fder.xview)
            fder.configure(xscrollcommand=treeScrollBarx.set,yscrollcommand=treeScrollBary.set)

            treeScrollBarx.pack(side="bottom", fill="x")
            treeScrollBary.pack(side="right", fill="y")

            fder.heading(1, text ="Codigo")
            fder.heading(2, text ="Nombre")
            fder.heading(3, text ="Cantidad")
            fder.heading(4, text ="Categoria")
            fder.heading(5, text ="P. Compra")
            fder.heading(6, text ="P. Venta")
            fder.heading(7, text ="Prov")

            BotonAgregarProducto=Button(frameGUIRegProd2, text="+ Agregar ",font=("comic sans MS", 15), bg="gray",fg="white",bd=5,cursor="hand2")
            BotonAgregarProducto.place(x=560,y=26,width=100)

            self.rootGUIRegProd2.mainloop()
            

    #****** Ventana Registro Producto ******#

def ventanaRegistroProducto(self):

        self.rootGUIRegProd2=Tk()
        self.rootGUIRegProd2.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIRegProd2.geometry("1360x768+560+312")
        self.rootGUIRegProd2.resizable(1,1)

            # ******Frame Derecho******#

        frameGUIRegProd3= Frame(self.rootGUIRegProd2,bg="#18344A")
        frameGUIRegProd3.place(x=600,y=85,relwidth=1,relheight=1)

        Label(frameGUIRegProd3,text="Agregar Producto ", font=("comic sans MS",25, "bold"), bg="#18344A",fg="white").place(x=50,y=20)

        #****** Frame Derecho ******#

        Label(frameGUIRegProd3,text="CODIGO:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=50,y=86)
        Label(frameGUIRegProd3,text="NOMBRE:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=50,y=126)
        Label(frameGUIRegProd3,text="VALOR VENTA:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=50,y=166)
        Label(frameGUIRegProd3,text="DESCRIPCIÓN:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=50,y=206)

        #****** Entradas de texto ******#

        self.cuadroCodigo=Entry(frameGUIRegProd3,font=("comic sans MS",13), bg="#18344A",fg="black")
        self.cuadroCodigo.place(x=235,y=86)

        self.cuadroNombre=Entry(frameGUIRegProd3,font=("comic sans MS",13), bg="#18344A",fg="black")
        self.cuadroNombre.place(x=235,y=126)

        self.cuadroValorVenta=Entry(frameGUIRegProd3,font=("comic sans MS",13), bg="#18344A",fg="black")
        self.cuadroValorVenta.place(x=235,y=166)

        self.cuadrotexto=Entry(frameGUIRegProd3,font=("comic sans MS",13), bg="#18344A",fg="black")
        self.cuadrotexto.place(x=235,y=206)

        #___---------cOLUMNA 2

        Label(frameGUIRegProd3,text="INSUMO:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=450,y=86)

        self.insumo = Entry(frameGUIRegProd3, font=("comic sans MS",13), bg="#18344A",fg="black")
        self.insumo.place(x=550,y=86,width=150)


        Label(frameGUIRegProd3,text="CANTIDAD:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=450,y=126)

        self.cuadroCantidad=Entry(frameGUIRegProd3,font=("comic sans MS",13), bg="#18344A",fg="black")
        self.cuadroCantidad.place(x=550,y=126,width=50)

        # ****** Botones Producto ******#
        BotonAgregar=Button(frameGUIRegProd3, text="Agregar",font=("comic sans MS", 13), bg="gray",fg="#18344A",bd=0,cursor="hand2")
        BotonAgregar.place(x=450,y=166,width=110)

        BotonQuitar=Button(frameGUIRegProd3, text="Quitar",font=("comic sans MS", 13), bg="gray",fg="#18344A",bd=0,cursor="hand2")
        BotonQuitar.place(x=600,y=166,width=110)

        #Lisbox que muestra insumo seleccionado
        self.listboxinsumo=Listbox(frameGUIRegProd3,width=25,height=5, bg="#18344A",font=("comic sans MS",13))

        self.listboxinsumo.place(x=465,y=206)

        #----final---

        BotonRegistrar=Button(frameGUIRegProd3, text="Finalizar Registro",command=self.registrarPP,font=("comic sans MS", 15), bg="gray",fg="#18344A",bd=0,cursor="hand2")
        BotonRegistrar.place(x=225,y=340,width=300)

        self.rootGUIRegProd2.mainloop()
""""
    def validacionPP(self):
        return (len(self.cuadroCodigo.get())==0 or len(self.cuadroNombre.get())==0)

    def registrarPP(self):

        if self.validacionPP():
            messagebox.showinfo("error!","Los datos son obligatorios")
        else:
            self.gestionProducto=GUIGestionProducto()
            self.gestionProducto.registrar_producto_preparado(self.cuadroCodigo.get(),self.cuadroNombre.get(),
            self.cuadroValorVenta.get(),self.cuadrotexto.get(),self.insumo.get(),self.cuadroCantidad.get())   
   

    #Para ir al usuario
    def usuario(self):
        self.rootGUIRegProd.destroy()
        import GUIAdminRestaurante as cc
        cc.inicio()

    def productoNoPreparado(self):
        self.rootGUIRegProd.destroy()
        import GUIRegistorProducto as cc
        cc.inicio()

    def gestionInsumo(self):
        self.rootGUIRegProd.destroy()
        import GUIgestionInsumo as cc
        cc.inicio()
        
"""

def iniciar():
    rootGUIRegProd = Tk()
    obj = GUIGestionProducto(rootGUIRegProd)
    rootGUIRegProd.mainloop()

