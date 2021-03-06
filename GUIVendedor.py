# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ******#

from gestionUsuario import *
from gestionProducto import *
from gestionFactura import *
import gestionUsuario as gu
usuario=Usuario("","","","","","","","", "")

# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

# ****** Clase GUIVendedor ****** #

class GUIVendedor:

    def __init__(self, rootGUIVendedor):
        self.rootGUIVendedor = rootGUIVendedor
        self.rootGUIVendedor.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIVendedor.geometry("1366x768")
        self.rootGUIVendedor.resizable(1, 1)
        self.rootGUIVendedor.iconbitmap("Imagenes\iconoInterfaz.ico")

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIVendedor, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame inicio Productos Side Der ****** #

        self.frameDerechoVendedor = Frame(self.rootGUIVendedor, bg="#18344A")
        self.frameDerechoVendedor.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(self.frameDerechoVendedor, text="Bienvenido, Vendedor", font=("comic sans MS", 24, "bold"), bg="#18344A",fg="white").place(x=180, y=20)

        # ****** Datos del perfil ****** #

        Label(self.frameDerechoVendedor, text="Identificador: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80, y=100)
        Label(self.frameDerechoVendedor, text="Nombre: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80, y=140)
        Label(self.frameDerechoVendedor,text="Apellido: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80, y=180)
        Label(self.frameDerechoVendedor, text="Telefono:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80, y=300)
        Label(self.frameDerechoVendedor, text="Direccion:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,y=260)
        Label(self.frameDerechoVendedor, text="Cargo:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,y=220)
        
        #-------- CARGAR DATOS DEL VENDEDOR EN EL FRAME
        self.CargarInfoUsuarioEnLabels()
        # INFORMACIO CARGADA QUE NO SE MODIFICA
        Label(self.frameDerechoVendedor, text=self.id_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=270,y=100)
        Label(self.frameDerechoVendedor, text=self.nombre_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=270, y=140)
        Label(self.frameDerechoVendedor, text=self.apellido_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=270, y=180)
        Label(self.frameDerechoVendedor, text=self.cargo_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=270, y=220)

        self.listboxUsuario = Listbox(self.frameDerechoVendedor, width=25, height=2, bg="#18344A", fg="white",
                                      font=("comic sans MS", 16))

        self.listboxUsuario.insert(0, self.dir_usu)
        self.listboxUsuario.insert(1, self.tel_usu)

        self.listboxUsuario.place(x=270, y=260)


        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(self.frameDerechoVendedor, text="Modificar datos", command=self.retornarSelecListBoxUsuario,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContrase??a = Button(self.frameDerechoVendedor, text="Cambiar Contrase??a", command=self.modContrase??a,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContrase??a.place(x=380,y=400, width=240)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoVendedor = Frame(self.rootGUIVendedor, bg="#18344A")
        frameIzquierdoVendedor.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoVendedor, text="Vendedor", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=170, y=30)

        # ****** Boton Crear Venta ****** #

        BotonCrearVenta = Button(frameIzquierdoVendedor, text="Gestion de Clientes",command=self.gesCliente, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearVenta.place(x=120, y=120, width=240)

        # ****** Boton Consultar Venta ******#

        BotonConsultarVenta = Button(frameIzquierdoVendedor, text="Lista de Productos", command=self.lisProductos, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarVenta.place(x=120, y=180, width=240)

        # ****** Boton Modificar Venta ****** #

        BotonModificarVenta = Button(frameIzquierdoVendedor, text="Lista de Usuarios",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarVenta.place(x=120, y=240, width=240)

        BotonFactura = Button(frameIzquierdoVendedor, text="Hacer Factura", command=self.hacerFactura, font=("comic sans MS", 15),
                                    bg="gray", fg="white", bd=5, cursor="hand2")
        BotonFactura.place(x=120, y=300, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameIzquierdoVendedor, text="Cerrar Sesi??n", command=self.login2, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

    def lisProductos(self):
        self.frameDerechoVendedor.place_forget()
        self.mostrarProd()

    def hacerFactura(self):
        self.auxId = askstring('Consulta', 'Ingrese el codigo de un pedido')

        gestionFacturas = gestionFactura()
        fact= self.auxId
        cons=gestionFacturas.buscar_info(self.auxId)
        print(cons)
        if (cons == None):
            gesFac = gestionFactura()
            gesFac.registrar_codigo(fact)
            self.rootGUIVendedor.destroy()
            import GUIFacturacion as emp
            emp.iniciar(fact, usuario.get_id_usu())
        else:
            messagebox.showinfo("Consultar", "La factura est?? registrado")

    def  mostrarProd(self):
        self.frameDerechoEmp = Frame(self.rootGUIVendedor, bg="#18344A")
        self.frameDerechoEmp.place(x=600, y=85, width=700, height=530)

        self.scrollbar = Scrollbar(self.frameDerechoEmp)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listboxUsuario = Listbox(self.frameDerechoEmp, width=33, heigh=9, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20))
        self.listboxUsuario.pack()


        self.CargarInfoUsuarioEnLabels3(self.listboxUsuario)

        self.listboxUsuario.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listboxUsuario.yview)

        self.listboxUsuario.place(x=50, y=86)

    def CargarInfoUsuarioEnLabels3(self, listboxUsuario):
        gestionUsuarios = gestionProducto()
        listaDatos = gestionUsuarios.obtenerTodos()

        for x in listaDatos:
            listboxUsuario.insert(END, x)


    def gesCliente(self):
        self.rootGUIVendedor.destroy()
        import GUIGestionCliente as emp
        emp.iniciar(usuario.get_cargo())

    # ****** Metodo para iniciar la interfaz desde otra ****** #
    def CargarInfoUsuarioEnLabels(self):

        self.id_usu = usuario.get_id_usu()
        self.nombre_usu = usuario.get_nombre()
        self.apellido_usu = usuario.get_apellido()
        self.cargo_usu = usuario.get_cargo()
        self.dir_usu = usuario.get_direccion()
        self.tel_usu = usuario.get_telefono()
        self.contrase??a_usu = usuario.get_contrase??a()

    def retornarSelecListBoxUsuario(self):
        gestionUsuarios = gestionUsuario()
        aux = self.listboxUsuario.curselection()
        if (self.listboxUsuario.selection_includes(0)):
            aux2 = askstring('Modificaci??n de informaci??n', 'Ingrese la nueva direccion de usuario')

            if (aux2 == None):
                showinfo('Modificaci??n de informaci??n', 'No se realiz?? ningun cambio')
            else:
                showinfo('Modificaci??n de informaci??n', 'Tu nombre qued??:  '.format(aux2))

                gestionUsuarios.modificar_direccion(aux2, self.id_usu)

        if (self.listboxUsuario.selection_includes(1)):
            aux2 = askstring('Modificaci??n de informaci??n', 'Ingrese la nueva telefono de usuario')
            if (aux2 == None):
                showinfo('Modificaci??n de informaci??n', 'No se realiz?? ningun cambio')
            else:
                showinfo('Modificaci??n de informaci??n', 'Tus telefono quedaron: '.format(aux2))
                gestionUsuarios.modificar_telefono(aux2, usuario.get_id_usu())

    def modContrase??a(self):
        gestionUsuarios=gestionUsuario()
        nuevaContrase??a=""
        confirNuevaContra=""
        contrase??aActual = askstring('Cambiar contrase??a', 'Escribe tu contrase??a actual')
        if(contrase??aActual==self.contrase??a_usu):
            nuevaContrase??a=askstring('Cambiar contrase??a', 'Escribe tu nueva contrase??a')
            if (contrase??aActual==nuevaContrase??a):
                showinfo('Cambiar contrase??a','La contrase??a es igual a la antigua, trata con otra')
            else:
                confirNuevaContra=askstring('Cambiar contrase??a', 'Confirma tu nueva contrase??a')
                if(nuevaContrase??a==confirNuevaContra):
                    showinfo('Cambiar contrase??a','Cambio exitoso, vuelve a hacer login')
                    gestionUsuarios.cambiar_contrase??a(confirNuevaContra, usuario.get_contrase??a(),usuario.get_id_usu())
                    self.login2()
                else:
                    showinfo('Cambiar contrase??a','Las contrase??as no coinciden')
        if(contrase??aActual==None):
                showinfo('Modificaci??n de informaci??n','No se realiz?? ningun cambio')
        else:
            showinfo('Cambiar contrase??a','Contrase??a incorrecta')

    def login2(self):
        self.rootGUIVendedor.destroy()


def iniciar():
     rootGUIVendedor = Tk()
     obj = GUIVendedor(rootGUIVendedor)
     rootGUIVendedor.mainloop()
