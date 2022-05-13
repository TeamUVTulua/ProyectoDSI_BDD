from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from gestionUsuario import *
from BaseDatos import *
from Usuario import *

user = Usuario("", "", "", "", "", "", "", "")

class loginUsuario:
    def __init__(self, rootLogin):
        self.rootLogin = rootLogin
        self.rootLogin.title("Sistema de inventario y Ventas MotoSocios")
        self.rootLogin.geometry("1360x768+560+312")
        self.rootLogin.resizable(1, 1)
        self.rootLogin.iconbitmap("Imagenes\iconoInterfaz.ico")

        # ****** Imagen de fondo ****** #
        self.bg = ImageTk.PhotoImage(file="Imagenes/FondoInterfaz2.png")
        Label(self.rootLogin, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame Login ****** #
        frameLogin = Frame(self.rootLogin, bg="#18344A")
        frameLogin.place(x=500, y=110, width=345, height=450)
        Label(frameLogin, text="INICIO SESIÓN", font=("times new roman", 25, "bold"), bg="#18344A",fg="white").place(x=50, y=20)

        # ****** Label ID ****** #
        Label(frameLogin, text="Identificación: ", font=("times new roman", 16, "bold"), bg="#18344A", fg="white").place( x=50, y=80)
        self.cuadroID = Entry(frameLogin, font=("times new roman", 16),width=22)
        self.cuadroID.place(x=50, y=120)

        # ****** Label contraseña ****** #
        Label(frameLogin, text="Contraseña: ", font=("times new roman", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=160)
        self.cuadroPass = Entry(frameLogin, show="*", font=("times new roman", 16,),width=22)
        self.cuadroPass.place(x=50, y=200)

        # ****** Boton Ingresar ****** #
        BotonOlvidePass = Button(frameLogin, text="Ingresar ", font=("times new roman", 15),bg="gray", fg="white", bd=5, cursor="hand2")
        BotonOlvidePass.place(x=75,y=280, width=200)

        # ****** Boton Salir ****** #

        BotonIngresar = Button(frameLogin, text="Salir", command=self.abrirUsuarioSegunRol, font=("times new roman", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonIngresar.place(x=75, y=330, width=200)

        # ****** Boton Olvide mi contraseña ****** #

        BotonSalirR = Button(frameLogin, text="Olvide mi contraseña", command=self.rootLogin.quit, font=("times new roman", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalirR.place(x=75, y=380, width=200)

    def abrirUsuarioSegunRol(self):

        gestionUsuarios = gestionUsuario()
        user2 = gestionUsuarios.login_usuario(self.cuadroID.get(), self.cuadroPass.get())

        #print(user2.get_nombre())
        user = user2

        #print(user.get_id_rol())

        if (user2.get_cargo() == 'administrador'):
            print("ventana adminCC")
            self.rootLogin.destroy()
            import GUIAdministrador as cc
            cc.usuario = user2
            cc.iniciar()

        elif (user.get_id_rol() == 2):
            print("ventana adminRR")
            self.rootLogin.destroy()
            import GUIAdminRestaurante as cc
            cc.usuario = user2
            cc.inicio()


        elif (user.get_id_rol() == 3):
            print("ventana OperarioRR")
            self.rootLogin.destroy()
            import GUIOperarioRestau as cc
            cc.usuario = user2
            cc.inicio()
        else:
            messagebox.showinfo("Aviso", "El email o contraseña son incorrectos")


rootLogin = Tk()
obj = loginUsuario(rootLogin)
rootLogin.mainloop()