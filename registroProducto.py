
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ****** #

from Producto import *
from gestionProducto import *

class resgistroProducto:

    def __init__(self, rootRegistroProducto):
        self.rootRegistroProducto = rootRegistroProducto
        self.rootRegistroProducto.title("Registro Usuario")
        self.rootRegistroProducto.geometry("1360x768+560+312")
        self.rootRegistroProducto.resizable(1, 1)

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootRegistroProducto, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        # ****** Frame Crear Usuario ****** #

        frameCrearUsuario = Frame(self.rootRegistroProducto,bg="#18344A")
        frameCrearUsuario.place(x=160, y=0, width=650, height=600)

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
        self.categoria = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.categoria.place(x=50, y=190)

        # ****** Label cantidadefono Crear Usuario ****** #

        Label(frameCrearUsuario, text="Cantidad Total: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=150)
        self.cantidad = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.cantidad.place(x=350, y=190)

        # ****** Boton Guardar Crear Usuario ****** #

        BotonGuardar = Button(frameCrearUsuario, text="Registrar", command=self.registrar, font=("comic sans MS", 15), bd=0,cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

        # ****** Label Volver Crear Usuario ****** #

        BotonLogin = Button(frameCrearUsuario, text="Volver", command=self.volver , font=("comic sans MS", 15),bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def validacion(self):
        return (len(self.codigo.get()) == 0 or len(self.categoria.get()) == 0)

    def registrar(self):
        if self.validacion():
            messagebox.showinfo("error!", "Los datos son obligatorios")
        else:
            self.gestionUsuario = gestionProducto()
            self.gestionUsuario.registrar_producto(self.codigo.get(), self.nombre.get(),self.categoria.get(),self.cantidad.get())
            self.volver()

        # ****** Para volver al login desde Crear Usuario ****** #
    def volver(self):
        self.rootRegistroProducto.destroy()
        import GUIGestionProducto as ges
        ges.iniciar()

            # ****** Metodo para iniciar la interfaz desde otra ****** #

def iniciar():
    rootRegistroProducto = Tk()
    obj = resgistroProducto(rootRegistroProducto)
    rootRegistroProducto.mainloop()