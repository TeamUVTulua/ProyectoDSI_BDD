# ****** Librerias Usadas ****** #
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

# ****** Metodos de otros archivos ******#

from gestionUsuario import *
from BaseDatos import *
from Usuario import *

user = Usuario("", "", "", "", "", "", "", "", "")


# ****** Clase loginUsuario ****** #

class loginUsuario:
    def __init__(self, rootLogin):
        self.rootLogin = rootLogin
        self.rootLogin.title("Sistema de inventario y Ventas MotoSocios")
        self.rootLogin.geometry("1366x768")
        self.rootLogin.resizable(1, 1)
        self.rootLogin.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.rootLogin.attributes('-fullscreen',True)

        # ****** Imagen de fondo ****** #
        self.bg = ImageTk.PhotoImage(file="Imagenes/FondoInterfaz2.png")
        Label(self.rootLogin, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame Login ****** #
        frameLogin = Frame(self.rootLogin, bg="#18344A")
        frameLogin.place(x=500, y=110, width=345, height=450)
        Label(frameLogin, text="INICIO SESIÓN", font=("comic sass MS", 25, "bold"), bg="#18344A",fg="white").place(x=50, y=20)

        # ****** Label ID ****** #
        Label(frameLogin, text="Identificación: ", font=("comic sass MS", 16, "bold"), bg="#18344A", fg="white").place( x=50, y=80)
        self.cuadroID = Entry(frameLogin, font=("comic sass MS", 16),width=22)
        self.cuadroID.place(x=50, y=120)

        # ****** Label contraseña ****** #
        Label(frameLogin, text="Contraseña: ", font=("comic sass MS", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=160)
        self.cuadroPass = Entry(frameLogin, show="*", font=("comic sass MS", 16,),width=22)
        self.cuadroPass.place(x=50, y=200)

        # ****** Boton Ingresar ****** #
        BotonIngresar = Button(frameLogin, text="Ingresar ", command=self.abrirUsuarioSegunRol, font=("comic sass MS", 15),bg="gray", fg="white", bd=5, cursor="hand2")
        BotonIngresar.place(x=75,y=280, width=200)

        # ****** Boton Salir ****** #

        BotonSalir = Button(frameLogin, text="Salir", command=self.rootLogin.destroy,font=("comic sass MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=75, y=330, width=200)

        # ****** Boton Olvide mi contraseña ****** #

        BotonOlvidePass = Button(frameLogin, text="Olvide mi contraseña", font=("comic sass MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonOlvidePass.place(x=75, y=380, width=200)

    def abrirUsuarioSegunRol(self):
            gestionUsuarios = gestionUsuario()
            user2 = gestionUsuarios.login_usuario(self.cuadroID.get(), self.cuadroPass.get())

            user = user2
            if (user2.get_cargo() == 'administrador'):
                self.rootLogin.destroy()
                import GUIAdministrador as cc
                cc.usuario = user2
                cc.iniciar()

            elif (user2.get_cargo() == 'vendedor'):
                self.rootLogin.destroy()
                import GUIVendedor as cc
                cc.usuario = user2
                cc.iniciar()


            elif (user2.get_cargo() == 'bodega'):
                self.rootLogin.destroy()
                import GUIBodeguista as cc
                cc.usuario = user2
                cc.iniciar()

            elif (user2.get_cargo() == 'contador'):
                self.rootLogin.destroy()
                import GUIContador as cc
                cc.usuario = user2
                cc.iniciar()
            else:
                messagebox.showinfo("Aviso", "El email o contraseña son incorrectos")



def iniciar():

    rootLogin = Tk()
    obj = loginUsuario(rootLogin)
    rootLogin.mainloop()

rootLogin = Tk()
obj = loginUsuario(rootLogin)
rootLogin.mainloop()