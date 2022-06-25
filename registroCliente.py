# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# ****** Metodos de otros archivos ****** #

from Usuario import *
from gestionCliente import *
from tkinter.simpledialog import askstring
class registroCliente:

    def __init__(self, rootRegistroCliente, cargo):
        self.cargo = cargo
        self.rootRegistroCliente = rootRegistroCliente
        self.rootRegistroCliente.title("Registro Usuario")
        self.rootRegistroCliente.geometry("1360x768+560+312")
        self.rootRegistroCliente.resizable(1, 1)

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootRegistroCliente, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        # ****** Frame Crear Usuario ****** #

        frameCrearUsuario = Frame(self.rootRegistroCliente,bg="#18344A")
        frameCrearUsuario.place(x=160, y=0, width=650, height=600)

        Label(frameCrearUsuario, text="REGISTRAR CLIENTE", font=("comic sans MS", 25, "bold"), bg="#18344A",
              fg="white").place(x=50, y=20)

        # ****** Label ID Crear Usuario ****** #

        Label(frameCrearUsuario, text="NIT: ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(x=50, y=70)
        self.ident = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.ident.place(x=50, y=110)

        # ****** Label Nombre Crear Usuario ****** #

        Label(frameCrearUsuario, text="Nombre: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=70)
        self.nombre = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.nombre.place(x=350, y=110)

        # ****** Label Apellido Crear Usuario ****** #

        Label(frameCrearUsuario, text="Apellido 1: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=50, y=150)
        self.apell = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.apell.place(x=50, y=190)

        # ****** Label Telefono Crear Usuario ****** #

        Label(frameCrearUsuario, text="Apellido 2: ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(x=350, y=150)
        self.tel = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.tel.place(x=350, y=190)

        # ****** Label Direccion Crear Usuario ****** #

        Label(frameCrearUsuario, text="Direccion Numero ", font=("comic sans MS", 16, "bold"), bg="#18344A", fg="white").place(
            x=350, y=230)
        self.rolPass = ttk.Combobox(frameCrearUsuario, font=("comic sans MS", 13), state="readonly", justify=CENTER)
        self.rolPass["values"] = ["Esporadico", "Habitual"]
        self.rolPass.place(x=50, y=270)

        # ****** Label Cargo Crear Usuario ****** #



        Label(frameCrearUsuario, text="Tipo Cliente ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(
            x=50, y=230)
        self.dir = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.dir.place(x=350, y=270)

        self.carg = self.rolPass

        # ****** Label Sueldo Crear Usuario ****** #

        Label(frameCrearUsuario, text="Direccion Calle ", font=("comic sans MS", 16, "bold"), bg="#18344A",fg="white").place(x=50, y=310)
        self.sueld = Entry(frameCrearUsuario, font=("comic sans MS", 16))
        self.sueld.place(x=50, y=350)

        Label(frameCrearUsuario, text="Buscar Cliente ", font=("comic sans MS", 16, "bold"), bg="#18344A",
              fg="white").place(
            x=50, y=390)

        # ****** Boton Buscar
        photo = PhotoImage(file="Imagenes/lupa.png")
        BotonBuscar = Button(frameCrearUsuario, text="Buscar", command=self.busc, bd=0, cursor="hand2")
        BotonBuscar.place(x=50, y=430, width=80)


        # ****** Boton Guardar Crear Usuario ****** #

        BotonGuardar = Button(frameCrearUsuario, text="Registrar", command=self.registrar, font=("comic sans MS", 15), bd=0,cursor="hand2")
        BotonGuardar.place(x=50, y=500, width=200)

        # ****** Label Volver Crear Usuario ****** #

        BotonLogin = Button(frameCrearUsuario, text="Volver", command=self.volver , font=("comic sans MS", 15),bd=0, cursor="hand2")
        BotonLogin.place(x=350, y=500, width=200)

    def busc(self):

        self.auxId = askstring('Modificación de información', 'Ingrese el identificador de un empleado')

        gestionClientes = gestionCliente()
        cons = gestionClientes.buscar_info(self.auxId)
        print (cons)
        if (cons == None):
            messagebox.showinfo("Consultar", "El usuario no está registrado")
        else:
            messagebox.showinfo("Consultar", "El usuario está registrado")

    def validacion(self):
        return (len(self.ident.get()) == 0 or len(self.carg.get()) == 0)

    def registrar(self):
        if self.validacion():
            messagebox.showinfo("error!", "Los datos son obligatorios")
        else:
            self.gestionUsuario = gestionCliente()
            self.gestionUsuario.registrar_cliente(self.ident.get(), self.nombre.get(), self.apell.get(),self.tel.get(),self.rolPass.get(), self.dir.get(),self.sueld.get())
            self.volver()

        # ****** Para volver al login desde Crear Usuario ****** #
    def volver(self):
        self.rootRegistroCliente.destroy()
        import GUIGestionCliente as ges
        ges.iniciar(self.cargo)

            # ****** Metodo para iniciar la interfaz desde otra ****** #

def iniciar(cargo):
    rootRegistroCliente = Tk()
    obj = registroCliente(rootRegistroCliente, cargo)
    rootRegistroCliente.mainloop()
