from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Usuario import *
import Usuario
from RegistroUsuario import *
from GestionUsuarios import *

# import RegistroUsuario
mensaje = "cdfdfsd"
user = Usuario("", "", "", "", "", "", "", "", "", "", "")


# def prueba():
#   print(mensaje)

class LoginUsuario:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Login Usuario")
        self.raiz.geometry("1200x600+0+0")
        self.raiz.resizable(0, 0)
        # --------imagen Fondo------
        self.bg = ImageTk.PhotoImage(file="Imagenes/imagen3.jpg")
        Label(self.raiz, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # -------loginFrame----------
        miFrame = Frame(self.raiz, bg="darkgoldenrod")
        miFrame.place(x=425, y=105, width=345, height=390)
        Label(miFrame, text="INICIA SESIÓN", font=("times new roman", 25, "bold"), bg="darkgoldenrod",
              fg="white").place(x=50, y=20)

        # ---------Row 1-----------
        Label(miFrame, text="Correo: ", font=("times new roman", 16, "bold"), bg="darkgoldenrod", fg="gainsboro").place(
            x=50, y=70)
        self.cuadroTextoCorreo = Entry(miFrame, font=("times new roman", 16))
        self.cuadroTextoCorreo.place(x=50, y=110)

        # ---------Row 2 ------------------
        Label(miFrame, text="Contraseña: ", font=("times new roman", 16, "bold"), bg="darkgoldenrod",
              fg="gainsboro").place(x=50, y=150)
        self.TextoPass = Entry(miFrame, show="*", font=("times new roman", 16))
        self.TextoPass.place(x=50, y=190)

        ########Id del rol se debe autenticar con el correo##################
        # ----Row #4-------------

        BotonRegistrarse = Button(miFrame, text="¿Eres nuevo? registrate", command=self.RegistroUsuario_window,
                                  font=("times new roman", 10), bd=0, bg="darkgoldenrod", cursor="hand2")
        BotonRegistrarse.place(x=60, y=230, width=200)

        # ---------Row 5----------

        BotonIngresar = Button(miFrame, text="Ingresar", command=self.abrirUsuarioSegunRol,
                               font=("times new roman", 15), bg="dimgrey", fg="white", bd=0, cursor="hand2")
        BotonIngresar.place(x=60, y=270, width=200)
        # -----Row 6-------------

        BotonSalirR = Button(miFrame, text="Salir", command=self.raiz.quit, font=("times new roman", 15), bg="dimgrey",
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
            self.raiz.destroy()
            import GUIAdminCentroC as cc
            cc.usuario = user2
            cc.inicio()

        elif (user.get_id_rol() == 2):
            print("ventana adminRR")
            self.raiz.destroy()
            import GUIAdminRestaurante as cc
            cc.usuario = user2
            cc.inicio()


        elif (user.get_id_rol() == 3):
            print("ventana OperarioRR")
            self.raiz.destroy()
            import GUIOperarioRestau as cc
            cc.usuario = user2
            cc.inicio()
        else:
            messagebox.showinfo("Aviso", "El email o contraseña son incorrectos")

    # Para ir al RegistroUsuario
    def RegistroUsuario_window(self):
        self.raiz.destroy()
        mensaje = "cucucucu"
        print(mensaje)
        import RegistroUsuario as p
        p.mimi = mensaje
        p.inicio()
"""

raiz = Tk()
obj = LoginUsuario(raiz)
raiz.mainloop()