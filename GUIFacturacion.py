from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

class GUIFacturacion:
    def __init__(self, rootGUIFacturacion):
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

        frameCrearUsuario = Frame(self.rootGUIFacturacion,bg="#18344A")
        frameCrearUsuario.place(x=350, y=75, width=650, height=600)

        Label(frameCrearUsuario, text="REGISTRAR PRODUCTO", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=50, y=20)

        # ****** Label ID Crear Usuario ****** #

        Label(frameCrearUsuario, text="Codigo: ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=70)
        self.codigo = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.codigo.place(x=50, y=110)

        # ****** Label Nombre Crear Usuario ****** #

        Label(frameCrearUsuario, text="Nombre: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=70)
        self.nombre = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.nombre.place(x=350, y=110)

        # ****** Label categoriaido Crear Usuario ****** #

        Label(frameCrearUsuario, text="Categoria: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=150) # REVIDAR CON UN BOX SELECT
        self.rolPass = ttk.Combobox(frameCrearUsuario, font=("comic sans MS", 13), state="readonly", justify=CENTER)
        self.rolPass["values"] = ["electrica", "mecanica", "estetica", "varias"]
        self.rolPass.place(x=50, y=190)

        self.categoria = self.rolPass

        # ****** Label cantidadefono Crear Usuario ****** #

        Label(frameCrearUsuario, text="Cantidad Total: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=150)
        self.cantidad = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.cantidad.place(x=350, y=190)

        Label(frameCrearUsuario, text="NIT Proveedor: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=230)
        self.nit_prov = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.nit_prov.place(x=50, y=270)

        Label(frameCrearUsuario, text="Nombre Proveedor: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=230)
        self.nom_prov = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.nom_prov.place(x=350, y=270)

        Label(frameCrearUsuario, text="Contacto Proveedor: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=310)
        self.cont_prov = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.cont_prov.place(x=50, y=350)

        Label(frameCrearUsuario, text="Direccion Proveedor: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=310)
        self.dir_prov = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.dir_prov.place(x=350, y=350)



        # ****** Boton Guardar Crear Usuario ****** #

        BotonGuardar = Button(frameCrearUsuario, text="Registrar", font=("comic sans MS", 15), bd=0,cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

        # ****** Label Volver Crear Usuario ****** #

        BotonLogin = Button(frameCrearUsuario, text="Volver", font=("comic sans MS", 15) ,bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

rootGUIFacturacion = Tk()
obj = GUIFacturacion(rootGUIFacturacion)
rootGUIFacturacion.mainloop()