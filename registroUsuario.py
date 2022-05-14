from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Usuario import *
from gestionUsuario import *

class registroUsuario:

    def __init__(self, raiz1):
        self.raiz1 = raiz1
        self.raiz1.title("Registro Usuario")
        self.raiz1.geometry("1360x768+560+312")
        self.raiz1.resizable(1, 1)
        # self.raiz1.configure(background="black")
        # --------imagen background------
        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.raiz1, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # -------registrerFrame--------

        miFrame1 = Frame(self.raiz1, bg="saddlebrown")
        miFrame1.place(x=160, y=0, width=650, height=600)

        Label(miFrame1, text="REGISTRAR USUARIO", font=("times new roman", 25, "bold"), bg="saddlebrown",
              fg="white").place(x=50, y=20)

        # ------Row 1---

        Label(miFrame1, text="Identificador: ", font=("times new roman", 16, "bold"), bg="saddlebrown", fg="gainsboro").place(x=50, y=70)
        self.ident = Entry(miFrame1, font=("times new roman", 16))
        self.ident.place(x=50, y=110)

        Label(miFrame1, text="Nombre: ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=350, y=70)
        self.nombre = Entry(miFrame1, font=("times new roman", 16))
        self.nombre.place(x=350, y=110)

        # ------Row 2---

        Label(miFrame1, text="Apellido: ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=50, y=150)
        self.apell = Entry(miFrame1, font=("times new roman", 16))
        self.apell.place(x=50, y=190)

        Label(miFrame1, text="Telefono: ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=350, y=150)
        self.tel = Entry(miFrame1, font=("times new roman", 16))
        self.tel.place(x=350, y=190)

        # ------Row 3---

        Label(miFrame1, text="Direccion ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=50, y=230)
        self.dir = Entry(miFrame1, font=("times new roman", 16))
        self.dir.place(x=50, y=270)

        Label(miFrame1, text="Cargo ", font=("times new roman", 16, "bold"), bg="saddlebrown", fg="gainsboro").place(x=350, y=230)
        self.rolPass = ttk.Combobox(miFrame1, font=("times new roman",13), state="readonly", justify=CENTER)
        self.rolPass["values"] = ["vendedor","bodega","contador", "administrador"]
        self.rolPass.place(x=350,y=270)

        self.carg = self.rolPass
        #self.carg = Entry(miFrame1, font=("times new roman", 16))
        #self.carg.place(x=350, y=270)

        # ------Row 4---

        Label(miFrame1, text="Sueldo ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=50, y=310)
        self.sueld = Entry(miFrame1, font=("times new roman", 16))
        self.sueld.place(x=50, y=350)

        self.contraseña = self.ident

        # ------Row 5---



        # ------Row 6---
        BotonGuardar = Button(miFrame1, text="Registrar", command=self.registrar, font=("times new roman", 15), bd=0,
                              cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)
        BotonLogin = Button(miFrame1, text="Volver", command=self.volver, font=("times new roman", 15),
                            bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def validacion(self):
        return (len(self.ident.get()) == 0 or len(self.carg.get()) == 0) #<--

    def registrar(self):

        if self.validacion():
            messagebox.showinfo("error!", "Los datos son obligatorios")
        else:
            self.gestionUsuario = gestionUsuario()
            self.gestionUsuario.registrar_usuario(self.ident.get(), self.nombre.get(), self.sueld.get(),self.tel.get(),
                                                  self.dir.get(), self.contraseña.get(),self.carg.get(),
                                                  self.apell.get())
            self.volver()

    # Para ir al Login
    def volver(self):
        self.raiz1.destroy()
        import GUIGestionEmpleado as ges
        ges.iniciar()


def iniciar():
    raiz1 = Tk()
    obj = registroUsuario(raiz1)
    raiz1.mainloop()