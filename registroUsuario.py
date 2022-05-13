from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# from Usuario import *
#from gestionUsuarios import *
# import LoginUsuario as l
mimi = "Perro"


# mimi=l.mensaje

class registroUsuario:

    def __init__(self, raiz1):
        self.raiz1 = raiz1
        self.raiz1.title("Registro Usuario")
        self.raiz1.geometry("1200x600+0+0")
        self.raiz1.resizable(0, 0)
        # self.raiz1.configure(background="black")
        # --------imagen background------
        self.bg = ImageTk.PhotoImage(file="Imagenes/logo.png")
        Label(self.raiz1, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # -------registrerFrame--------

        miFrame1 = Frame(self.raiz1, bg="saddlebrown")
        miFrame1.place(x=160, y=0, width=650, height=600)

        Label(miFrame1, text="REGISTRATE AQUÍ", font=("times new roman", 25, "bold"), bg="saddlebrown",
              fg="white").place(x=50, y=20)

        # ------Row 1---

        Label(miFrame1, text="Email: ", font=("times new roman", 16, "bold"), bg="saddlebrown", fg="gainsboro").place(x=50, y=70)
        self.EmailPass = Entry(miFrame1, font=("times new roman", 16))
        self.EmailPass.place(x=50, y=110)

        Label(miFrame1, text="Contraseña: ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=350, y=70)
        self.contraPass = Entry(miFrame1, font=("times new roman", 16))
        self.contraPass.place(x=350, y=110)

        # ------Row 2---

        Label(miFrame1, text="Id usuario: ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=50, y=150)
        self.Id_usuPass = Entry(miFrame1, font=("times new roman", 16))
        self.Id_usuPass.place(x=50, y=190)

        Label(miFrame1, text="Fecha de ingreso: ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=350, y=150)
        self.Fecha_IngrePass = Entry(miFrame1, font=("times new roman", 16))
        self.Fecha_IngrePass.place(x=350, y=190)

        # ------Row 3---

        Label(miFrame1, text="Nombre de usuario: ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=50, y=230)
        self.Nombre_usuPass = Entry(miFrame1, font=("times new roman", 16))
        self.Nombre_usuPass.place(x=50, y=270)

        Label(miFrame1, text="Apellido de usuario: ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=350, y=230)
        self.Apelli_usuPass = Entry(miFrame1, font=("times new roman", 16))
        self.Apelli_usuPass.place(x=350, y=270)

        # ------Row 4---

        Label(miFrame1, text="Direccion de usuario: ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=50, y=310)
        self.Direcc_usuPass = Entry(miFrame1, font=("times new roman", 16))
        self.Direcc_usuPass.place(x=50, y=350)

        Label(miFrame1, text="Telefono de usuario: ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=350, y=310)
        self.Tel_usuPass = Entry(miFrame1, font=("times new roman", 16))
        self.Tel_usuPass.place(x=350, y=350)

        # ------Row 5---

        Label(miFrame1, text="Id rol: ", font=("times new roman", 16, "bold"), bg="saddlebrown", fg="gainsboro").place(
            x=50, y=390)
        self.rolPass = ttk.Combobox(miFrame1, font=("times new roman", 13), state="readonly", justify=CENTER)
        self.rolPass["values"] = ["1", "2", "3"]
        self.rolPass.place(x=50, y=430)

        Label(miFrame1, text="Restaurante: ", font=("times new roman", 16, "bold"), bg="saddlebrown",
              fg="gainsboro").place(x=350, y=390)
        self.Nombre_Restaurante = Entry(miFrame1, font=("times new roman", 13))
        # funcion para leer nombres de restaurantes y mostarlos en esta vaina
        self.Nombre_Restaurante.place(x=350, y=430)

        # Por defecto el usuario se registra como activo
        self.Usu_activo = True

        # ------Row 6---
        BotonGuardar = Button(miFrame1, text="Registrar", command=self.registrar, font=("times new roman", 15), bd=0,
                              cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)
        BotonLogin = Button(miFrame1, text="Iniciar sesión", command=self.login_window, font=("times new roman", 15),
                            bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def validacion(self):
        return (len(self.identificacion.get()) == 0 or len(self.contraseña.get()) == 0) #<--

    def registrar(self):

        if self.validacion():
            messagebox.showinfo("error!", "Los datos son obligatorios")
        else:
            self.gestionUsuario = gestionUsuarios()
            self.gestionUsuario.registrar_usuario(self.identifiacaion.get(), self.contraseña.get(), self.sueldo.get(),
                                                  self.telefono.get(),
                                                  self.direccion.get(), self.cargo.get(),
                                                  self.apellido.get())

    # Para ir al Login
    def login_window(self):
        self.raiz1.destroy()
        import LoginUsuario


def inicio():
    raiz1 = Tk()
    obj = registroUsuario(raiz1)
    raiz1.mainloop()