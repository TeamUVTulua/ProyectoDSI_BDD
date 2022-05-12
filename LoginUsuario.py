from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class loginUsuario:
    def __init__(self, raizLogin):
        self.raizLogin = raizLogin
        self.raizLogin.title("Sistema de inventario y Ventas MotoSocios")
        self.raizLogin.geometry("1360x768+560+312")
        self.raizLogin.resizable(1, 1)

        # ****** Imagen de fondo ****** #
        self.bg = ImageTk.PhotoImage(file="Imagenes/FondoInterfaz2.png")
        Label(self.raizLogin, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame Login ****** #
        frameLogin = Frame(self.raizLogin, bg="darkgoldenrod")
        frameLogin.place(x=500, y=110, width=345, height=390)
        Label(frameLogin, text="INICIO SESIÓN", font=("times new roman", 25, "bold"), fg="white", bg="darkgoldenrod").place(x=50, y=20)

        # ---------Row 1-----------
        Label(frameLogin, text="Correo: ", font=("times new roman", 16, "bold"), bg="darkgoldenrod", fg="gainsboro").place(
            x=50, y=70)
        self.cuadroTextoCorreo = Entry(frameLogin, font=("times new roman", 16))
        self.cuadroTextoCorreo.place(x=50, y=110)

        # ---------Row 2 ------------------
        Label(frameLogin, text="Contraseña: ", font=("times new roman", 16, "bold"), bg="darkgoldenrod", fg="gainsboro").place(x=50, y=150)
        self.TextoPass = Entry(frameLogin, show="*", font=("times new roman", 16))
        self.TextoPass.place(x=50, y=190)

        ########Id del rol se debe autenticar con el correo##################
        # ----Row #4-------------

        BotonRegistrarse = Button(frameLogin, text="¿Eres nuevo? registrate", command=self.RegistroUsuario_window, font=("times new roman", 10), bd=0, bg="darkgoldenrod", cursor="hand2")
        BotonRegistrarse.place(x=60, y=230, width=200)

        # ---------Row 5----------

        BotonIngresar = Button(frameLogin, text="Ingresar", command=self.abrirUsuarioSegunRol,
                               font=("times new roman", 15), bg="dimgrey", fg="white", bd=0, cursor="hand2")
        BotonIngresar.place(x=60, y=270, width=200)
        # -----Row 6-------------

        BotonSalirR = Button(frameLogin, text="Salir", command=self.raizLogin.quit, font=("times new roman", 15), bg="dimgrey",
                             fg="white", bd=0, cursor="hand2")
        BotonSalirR.place(x=60, y=310, width=200)

    def abrirUsuarioSegunRol(self):

        gestionUsuarios = GestionUsuarios()
        user2 = gestionUsuarios.login_usuario(self.cuadroTextoCorreo.get(), self.TextoPass.get())
        print(user2.get_nombre())
        user = user2
        print(user.get_id_rol())

        if (user.get_id_rol() == 1):
            print("ventana adminCC")
            self.raizLogin.destroy()
            import GUIAdminCentroC as cc
            cc.usuario = user2
            cc.inicio()

        elif (user.get_id_rol() == 2):
            print("ventana adminRR")
            self.raizLogin.destroy()
            import GUIAdminRestaurante as cc
            cc.usuario = user2
            cc.inicio()


        elif (user.get_id_rol() == 3):
            print("ventana OperarioRR")
            self.raizLogin.destroy()
            import GUIOperarioRestau as cc
            cc.usuario = user2
            cc.inicio()
        else:
            messagebox.showinfo("Aviso", "El email o contraseña son incorrectos")

    # Para ir al RegistroUsuario
    def RegistroUsuario_window(self):
        self.raizLogin.destroy()
        mensaje = "cucucucu"
        print(mensaje)
        import RegistroUsuario as p
        p.mimi = mensaje
        p.inicio()

raizLogin = Tk()
obj = loginUsuario(raizLogin)
raizLogin.mainloop()