
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ****** #

from Producto import *
from gestionProveedor import *

class registroProveedor:

    def __init__(self, rootRegistroProveedor):
        self.rootRegistroProveedor = rootRegistroProveedor
        self.rootRegistroProveedor.title("Registro Proveedor")
        self.rootRegistroProveedor.geometry("1360x768+560+312")
        self.rootRegistroProveedor.resizable(1, 1)

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootRegistroProveedor, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        # ****** Frame Crear Usuario ****** #

        frameCrearUsuario = Frame(self.rootRegistroProveedor,bg="#18344A")
        frameCrearUsuario.place(x=160, y=0, width=650, height=600)

        Label(frameCrearUsuario, text="REGISTRAR PROVEEDOR", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=50, y=20)

        # ****** Label ID Crear Usuario ****** #

        Label(frameCrearUsuario, text="NIT: ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=70)
        self.nit = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.nit.place(x=50, y=110)

        # ****** Label Nombre Crear Usuario ****** #

        Label(frameCrearUsuario, text="Nombre: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=70)
        self.nombre = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.nombre.place(x=350, y=110)

        # ****** Label Contactoido Crear Usuario ****** #

        Label(frameCrearUsuario, text="Contacto: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=150) # REVIDAR CON UN BOX SELECT
        self.Contacto = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.Contacto.place(x=50, y=190)

        # ****** Label Direccionefono Crear Usuario ****** #

        Label(frameCrearUsuario, text="Direccion: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=150)
        self.Direccion = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.Direccion.place(x=350, y=190)

        # ****** Boton Guardar Crear Usuario ****** #

        BotonGuardar = Button(frameCrearUsuario, text="Registrar", command=self.registrar, font=("comic sans MS", 15), bd=0,cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

        # ****** Label Volver Crear Usuario ****** #

        BotonLogin = Button(frameCrearUsuario, text="Volver", command=self.volver , font=("comic sans MS", 15),bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def validacion(self):
        return (len(self.nit.get()) == 0 or len(self.Contacto.get()) == 0)

    def registrar(self):
        if self.validacion():
            messagebox.showinfo("error!", "Los datos son obligatorios")
        else:
            self.gestionUsuario = gestionProducto()
            self.gestionUsuario.registrar_producto(self.nit.get(), self.nombre.get(),self.Contacto.get(),self.Direccion.get())
            self.volver()

        # ****** Para volver al login desde Crear Usuario ****** #
    def volver(self):
        self.rootRegistroProveedor.destroy()
        import GUIGestionProducto as ges
        ges.iniciar()

            # ****** Metodo para iniciar la interfaz desde otra ****** #

def iniciar():
    rootRegistroProveedor = Tk()
    obj = resgistroProducto(rootRegistroProveedor)
    rootRegistroProveedor.mainloop()