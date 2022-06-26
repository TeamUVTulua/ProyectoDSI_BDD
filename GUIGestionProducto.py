# ****** Librerias Usadas ****** #
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ******#
import Producto as us
from gestionProducto import *
producto=us.Producto("","","","", "")
# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


# ****** Clase GUIGestionProducto ****** #

class GUIGestionProducto:
    def __init__(self, rootGUIRegProd, cargo):
        self.rootGUIRegProd = rootGUIRegProd
        self.cargo =cargo
        self.rootGUIRegProd.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIRegProd.geometry("1366x768")
        self.rootGUIRegProd.resizable(1, 1)
        self.rootGUIRegProd.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.rootGUIRegProd.attributes('-fullscreen', True)

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIRegProd, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoProd = Frame(self.rootGUIRegProd, bg="#18344A")
        frameIzquierdoProd.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoProd, text="Gestion de Productos", font=("comic sans MS", 23, "bold"), bg="#18344A",
              fg="white").place(x=100, y=30)

        # ****** Boton Home ******#

        BotonHome = Button(frameIzquierdoProd, text="Inicio", command=self.volver,font=("comic sans MS", 15), bg="#18344A", fg="white", bd=5,
                           cursor="hand2")
        BotonHome.place(x=30, y=30, width=70, height=35)

        # ****** Boton Agregar Producto ****** #

        BotonAgregarProducto = Button(frameIzquierdoProd, text="Agregar Producto", command=self.crear, font=("comic sans MS", 15), bg="gray",fg="white", bd=5, cursor="hand2")
        BotonAgregarProducto.place(x=120, y=120, width=240)

        # ******Boton Consultar Producto****** #

        BotonConsultarProducto = Button(frameIzquierdoProd, text="Consultar Producto",command=self.consultarEmp,
                                        font=("comic sans MS", 15),bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarProducto.place(x=120, y=180, width=240)

        # ******Boton Eliminar Producto ****** #

        BotonEliminarProducto = Button(frameIzquierdoProd, text="Eliminar Producto", command=self.eliminar, font=("comic sans MS", 15),bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarProducto.place(x=120, y=260, width=240)

        # ****** Frame inicio Productos Side Der ****** #
        self.frameDerechoProd = Frame(self.rootGUIRegProd, bg="#18344A")
        self.frameDerechoProd.place(x=600, y=85, width=700, height=530)


        # ******* Titulo Frame Producto ****** #
        Label(self.frameDerechoProd, text="Productos", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=280, y=20)

        self.scrollbar =Scrollbar(self.frameDerechoProd)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listboxUsuario = Listbox(self.frameDerechoProd, width=33, heigh=9, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20))
        self.listboxUsuario.pack()

        self.CargarInfoUsuarioEnLabels(self.listboxUsuario)

        self.listboxUsuario.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listboxUsuario.yview)

        self.listboxUsuario.place(x=50, y=86)

    def consultarEmp(self):
        self.auxId = askstring('Modificación de información', 'Ingrese el codigo de un producto')
        self.frameDerechoProd.place_forget()
        self.mostrarEmp()

    def mostrarEmp(self):
        frameDerechoAdmin = Frame(self.rootGUIRegProd, bg="#18344A")
        frameDerechoAdmin.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoAdmin, text=" Modificar", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=320, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoAdmin, text="Codigo: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(
            x=80, y=60)
        Label(frameDerechoAdmin, text="Nombre: ", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80,
                                                                                                              y=100)
        Label(frameDerechoAdmin, text="Categoria: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,
                                                                                                                 y=140)
        Label(frameDerechoAdmin, text="Cantidad:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,
                                                                                                                y=180)

        self.CargarInfoUsuarioEnLabels2()

        self.listboxUsuario = Listbox(frameDerechoAdmin, width=25, heigh=6, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20,))

        self.listboxUsuario.insert(0, self.codigo)
        self.listboxUsuario.insert(1, self.nombre)
        self.listboxUsuario.insert(2, self.categoria)
        self.listboxUsuario.insert(3, self.cantidad)

        self.listboxUsuario.place(x=270, y=60)

        BotonModificarDatos = Button(frameDerechoAdmin, text="Modificar datos",
                                     command=self.retornarSelecListBoxUsuario, font=("comic sans MS", 15), bg="gray",
                                     fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

    def retornarSelecListBoxUsuario(self):
        gestionUsuarios = gestionProducto()
        aux = self.listboxUsuario.curselection()
        if (self.listboxUsuario.selection_includes(0)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese el Codigo de usuario')

            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tu nombre quedó:  {}'.format(aux2))

                gestionUsuarios.modificar_codigo(aux2, self.codigo)
                print(aux2)

        if (self.listboxUsuario.selection_includes(1)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese el nuevo nombre de usuario')
            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tus telefono quedaron: {}'.format(aux2))
                gestionUsuarios.modificar_nombre(aux2, self.codigo)
            print(aux2)

        if (self.listboxUsuario.selection_includes(2)):
            print(aux)
            aux3 = askstring('Modificación de información', 'Ingrese la nueva categoria de usuario')
            if (aux3 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tus telefono quedaron: {}'.format(aux3))
                gestionUsuarios.modificar_categoria(aux3, self.codigo)
            print(aux3)

        if (self.listboxUsuario.selection_includes(3)):
            print(aux)
            aux4 = askstring('Modificación de información', 'Ingrese la nueva cantidad de usuario')
            if (aux4 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tus telefonos quedaron: {}'.format(aux4))
                gestionUsuarios.modificar_cantidad( self.codigo)
            print(aux4)

    def CargarInfoUsuarioEnLabels2(self):
        gestionUsuarios = gestionProducto()
        self.codigo = gestionUsuarios.obtener_codigo(self.auxId)
        self.nombre = gestionUsuarios.obtener_nombre(self.auxId)
        self.categoria = gestionUsuarios.obtener_categoria(self.auxId)
        self.cantidad = gestionUsuarios.obtener_cantidadTotal(self.auxId)

    def crear(self):
        self.rootGUIRegProd.destroy()
        import registroProducto as reg
        reg.iniciar(self.cargo)

    def CargarInfoUsuarioEnLabels(self, listboxUsuario):
        gestionUsuarios = gestionProducto()
        listaDatos = gestionUsuarios.obtenerTodos()

        for x in listaDatos:
            listboxUsuario.insert(END, x)

    def login_window(self):
        self.rootGUIRegProd.destroy()
        import LoginUsuario

    def volver(self):
        self.rootGUIRegProd.destroy()
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
        self.auxId = askstring('Eliminar Producto', 'Ingrese el codigo de un producto')
        gestionProductos = gestionProducto()
        gestionProductos.deshabilitar_usuario(self.auxId )
        self.rootGUIRegProd.destroy()
        iniciar()


def ventanaConsultarProd(self):

            self.rootGUIRegProd2=Tk()
            self.rootGUIRegProd2.title("Sistema de inventario y Ventas MotoSocios")
            self.rootGUIRegProd2.geometry("1360x768+560+312")
            self.rootGUIRegProd2.resizable(1, 1)

            frameIzquierdoProd2 = Frame(self.rootGUIRegProd2,bg="#18344A")
            frameIzquierdoProd2.place(x=600,y=85,width=700,height=530)

            Label(frameIzquierdoProd2,text="Lista Productos", font=("comic sans MS",24, "bold"), bg="#18344A",fg="white").place(x=220,y=20)

            #****** Cargue de datos en el Side der ******#
            # Carga lista de productos

            fder=ttk.Treeview(frameIzquierdoProd2, columns=(1,2,3,4,5,6,7),show="headings",height="18")
            fder.place(x=45,width=600,y=80)
            treeScrollBary=ttk.Scrollbar(frameIzquierdoProd2, orient="vertical",command=fder.yview)
            treeScrollBarx=ttk.Scrollbar(frameIzquierdoProd2, orient="horizontal",command=fder.xview)
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

            BotonAgregarProducto=Button(frameIzquierdoProd2, text="+ Agregar ",font=("comic sans MS", 15), bg="gray",fg="white",bd=5,cursor="hand2")
            BotonAgregarProducto.place(x=560,y=26,width=100)

            self.rootGUIRegProd2.mainloop()
            

    #****** Ventana Registro Producto ******#



def ventanaRegistroProducto(self):

        self.rootGUIRegProd2=Tk()
        self.rootGUIRegProd2.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIRegProd2.geometry("1360x768+560+312")
        self.rootGUIRegProd2.resizable(1,1)

            # ******Frame Derecho******#

        frameIzquierdoProd3= Frame(self.rootGUIRegProd2,bg="#18344A")
        frameIzquierdoProd3.place(x=600,y=85,relwidth=1,relheight=1)

        Label(frameIzquierdoProd3,text="Agregar Producto ", font=("comic sans MS",25, "bold"), bg="#18344A",fg="white").place(x=50,y=20)

        #****** Frame Derecho ******#

        Label(frameIzquierdoProd3,text="CODIGO:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=50,y=86)
        Label(frameIzquierdoProd3,text="NOMBRE:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=50,y=126)
        Label(frameIzquierdoProd3,text="VALOR VENTA:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=50,y=166)
        Label(frameIzquierdoProd3,text="DESCRIPCIÓN:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=50,y=206)

        #****** Entradas de texto ******#

        self.cuadroCodigo=Entry(frameIzquierdoProd3,font=("comic sans MS",13), bg="#18344A",fg="black")
        self.cuadroCodigo.place(x=235,y=86)

        self.cuadroNombre=Entry(frameIzquierdoProd3,font=("comic sans MS",13), bg="#18344A",fg="black")
        self.cuadroNombre.place(x=235,y=126)

        self.cuadroValorVenta=Entry(frameIzquierdoProd3,font=("comic sans MS",13), bg="#18344A",fg="black")
        self.cuadroValorVenta.place(x=235,y=166)

        self.cuadrotexto=Entry(frameIzquierdoProd3,font=("comic sans MS",13), bg="#18344A",fg="black")
        self.cuadrotexto.place(x=235,y=206)

        #___---------Columna 2

        Label(frameIzquierdoProd3,text="INSUMO:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=450,y=86)

        self.insumo = Entry(frameIzquierdoProd3, font=("comic sans MS",13), bg="#18344A",fg="black")
        self.insumo.place(x=550,y=86,width=150)


        Label(frameIzquierdoProd3,text="CANTIDAD:", font=("comic sans MS",13), bg="#18344A",fg="black").place(x=450,y=126)

        self.cuadroCantidad=Entry(frameIzquierdoProd3,font=("comic sans MS",13), bg="#18344A",fg="black")
        self.cuadroCantidad.place(x=550,y=126,width=50)

        # ****** Botones Producto ******#
        BotonAgregar=Button(frameIzquierdoProd3, text="Agregar",font=("comic sans MS", 13), bg="gray",fg="#18344A",bd=0,cursor="hand2")
        BotonAgregar.place(x=450,y=166,width=110)

        BotonQuitar=Button(frameIzquierdoProd3, text="Quitar",font=("comic sans MS", 13), bg="gray",fg="#18344A",bd=0,cursor="hand2")
        BotonQuitar.place(x=600,y=166,width=110)

        #Lisbox que muestra insumo seleccionado
        self.listboxinsumo=Listbox(frameIzquierdoProd3,width=25,height=5, bg="#18344A",font=("comic sans MS",13))

        self.listboxinsumo.place(x=465,y=206)

        #----final---

        BotonRegistrar=Button(frameIzquierdoProd3, text="Finalizar Registro",command=self.registrarPP,font=("comic sans MS", 15), bg="gray",fg="#18344A",bd=0,cursor="hand2")
        BotonRegistrar.place(x=225,y=340,width=300)

        self.rootGUIRegProd2.mainloop()

def iniciar(cargo):
    rootGUIRegProd = Tk()
    obj = GUIGestionProducto(rootGUIRegProd, cargo)
    rootGUIRegProd.mainloop()

