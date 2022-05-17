# ****** Librerias Usadas ****** #
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ******#
import Proveedor as us
from gestionProveedor import *
Proveedor=us.Proveedor("","","","")
# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


# ****** Clase GUIGestionProveedor ****** #

class GUIProveedor:
    def __init__(self, GUIProveedor):
        self.GUIProveedor = GUIProveedor
        self.GUIProveedor.title("Sistema de Inventario y Ventas MotoSocios")
        self.GUIProveedor.geometry("1360x768+560+312")
        self.GUIProveedor.resizable(1, 1)
        self.GUIProveedor.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.GUIProveedor.attributes('-fullscreen', True)

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.GUIProveedor, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ******Frame Botones Opciones Side Izq ****** #

        frameGUIRegProd = Frame(self.GUIProveedor, bg="#18344A")
        frameGUIRegProd.place(x=85, y=85, width=480, height=530)
        Label(frameGUIRegProd, text="Gestion de Proveedor", font=("comic sans MS", 23, "bold"), bg="#18344A",
              fg="white").place(x=100, y=30)

        # ****** Boton Agregar Proveedor ****** #

        #BotonAgregarProveedor = Button(frameGUIRegProd, text="Agregar Proveedor", command=self.crear, font=("comic sans MS", 15), bg="gray",fg="white", bd=5, cursor="hand2")
        #BotonAgregarProveedor.place(x=120, y=120, width=240)

        # ****** Boton Modificar Proveedor ******#

        #BotonReportes = Button(frameGUIRegProd, text="Modificar Proveedor",font=("comic sans MS", 15), bg="gray",fg="white", bd=5, cursor="hand2")
        #BotonReportes.place(x=120, y=180, width=240)

        # ******Boton Consultar Proveedor****** #

        #BotonConsultarProveedor = Button(frameGUIRegProd, text="Consultar Proveedor",command=self.consultarEmp, font=("comic sans MS", 15),bg="gray", fg="white", bd=5, cursor="hand2")
        #BotonConsultarProveedor.place(x=120, y=240, width=240)

        # ******Boton Eliminar Proveedor ****** #

        #BotonEliminarProveedor = Button(frameGUIRegProd, text="Eliminar Proveedor",font=("comic sans MS", 15),bg="gray", fg="white", bd=5, cursor="hand2")
        #BotonEliminarProveedor.place(x=120, y=360, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameGUIRegProd, text="Cerrar Sesión", command=self.login_window,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

        # ****** Frame inicio Proveedor Side Der ****** #
        self.frameDerechoEmp = Frame(self.GUIProveedor, bg="#18344A")
        self.frameDerechoEmp.place(x=600, y=85, width=700, height=530)


        # ******* Titulo Frame Proveedor ****** #
        Label(self.frameDerechoEmp, text="Proveedor", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=280, y=20)

        self.scrollbar =Scrollbar(self.frameDerechoEmp)
        self.scrollbar.pack(side=RIGHT, fill=Y)



        self.listboxUsuario = Listbox(self.frameDerechoEmp, width=33, heigh=9, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20))
        self.listboxUsuario.pack()
        #for i in range(100):
         #   self.listboxUsuario.insert(END,i)

        self.CargarInfoUsuarioEnLabels(self.listboxUsuario)

        self.listboxUsuario.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listboxUsuario.yview)


        self.listboxUsuario.place(x=50, y=86)

    def CargarInfoUsuarioEnLabels(self, listboxUsuario):
        gestionUsuarios = gestionProveedor()
        listaDatos = gestionUsuarios.obtenerTodos()

        for x in listaDatos:
            listboxUsuario.insert(END, x)
        
def iniciar():
    GUIProveedor = Tk()
    obj = GUIProveedor(GUIProveedor)
    GUIProveedor.mainloop()
