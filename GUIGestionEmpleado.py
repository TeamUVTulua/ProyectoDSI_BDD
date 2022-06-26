# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Usuario import *
import Usuario as us
from gestionUsuario import *
usuario=us.Usuario("","","","","","","","", "")
# ****** Metodos de otros archivos ******#

# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


# ****** Clase GUIMenuInicial ****** #

class GUIMenuInicial:
    def __init__(self, rootGestEmp):
        self.rootGestEmp = rootGestEmp
        self.rootGestEmp.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGestEmp.geometry("1366x768")
        self.rootGestEmp.resizable(1, 1)
        self.rootGestEmp.iconbitmap("Imagenes\iconoInterfaz.ico")

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGestEmp, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoEmp = Frame(self.rootGestEmp, bg="#18344A")
        frameIzquierdoEmp.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoEmp, text="Gestion Empleado", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=100, y=30)

        # ****** Boton Home ******#

        BotonHome = Button(frameIzquierdoEmp, text="Inicio", command=self.volver,font=("comic sans MS", 15), bg="#18344A", fg="white", bd=5,
                           cursor="hand2")
        BotonHome.place(x=30, y=30, width=70, height=35)

        # ****** Boton Consultar Empleados ****** #

        BotonConsultarEmpleados = Button(frameIzquierdoEmp, text="Consultar Empleado", command=self.consultarEmp , font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarEmpleados.place(x=120, y=130, width=240)

        # ****** Boton Crear Empleados ******#

        BotonCrearEmpleados = Button(frameIzquierdoEmp, text="Crear Empleado", command=self.crear,  font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearEmpleados.place(x=120, y=190, width=240)

        # ******Boton Eliminar Empleado ****** #

        BotonEliminarProducto = Button(frameIzquierdoEmp, text="Eliminar Empleado", command=self.eliminar, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarProducto.place(x=120, y=250, width=240)


        # ****** Frame Productos Side Der ****** #

        self.frameDerechoEmp = Frame(self.rootGestEmp, bg="#18344A")
        self.frameDerechoEmp.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Derecho ****** #
        Label(self.frameDerechoEmp, text="Empleados", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=280, y=20)

        self.listboxUsuario = Listbox(self.frameDerechoEmp, width=40, height=9, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20))

        self.listboxUsuario.get

        self.CargarInfoUsuarioEnLabels(self.listboxUsuario)

        self.listboxUsuario.place(x=50, y=86)

    def consultarEmp(self):
        self.auxId = askstring('Modificación de información', 'Ingrese el identificador de un empleado')
        self.frameDerechoEmp.place_forget()
        self.mostrarEmp()

    def mostrarEmp(self):
        frameDerechoEmp = Frame(self.rootGestEmp, bg="#18344A")
        frameDerechoEmp.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Empleado ****** #

        Label(frameDerechoEmp, text=" Empleados", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=320, y=20)

        # ****** Datos del perfil ****** #

        Label(frameDerechoEmp, text="Identificador: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(
            x=80, y=60)
        Label(frameDerechoEmp, text="Nombre: ", font=("comic sans MS", 20), bg="#18344A", fg="white").place(x=80,
                                                                                                              y=100)
        Label(frameDerechoEmp, text="Apellido: ", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,
                                                                                                                 y=140)
        Label(frameDerechoEmp, text="Telefono:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,
                                                                                                                y=260)
        Label(frameDerechoEmp, text="Direccion:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,
                                                                                                                 y=220)
        Label(frameDerechoEmp, text="Cargo:", font=("comic sans MS", 20,), bg="#18344A", fg="white").place(x=80,
                                                                                                             y=180)

        self.CargarInfoUsuarioEnLabels2()

        self.listboxUsuario = Listbox(frameDerechoEmp, width=25, height=6, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20,))

        self.listboxUsuario.insert(0, self.id_emp)
        self.listboxUsuario.insert(1, self.nom_emp)
        self.listboxUsuario.insert(2, self.ape_emp)
        self.listboxUsuario.insert(3, self.cargo_emp)
        self.listboxUsuario.insert(4, self.dir_emp)
        self.listboxUsuario.insert(5, self.tel_emp)

        self.listboxUsuario.place(x=270, y=70)

        BotonModificarDatos = Button(frameDerechoEmp, text="Modificar datos",
                                     command=self.retornarSelecListBoxUsuario, font=("comic sans MS", 15), bg="gray",
                                     fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

    def retornarSelecListBoxUsuario(self):
        gestionUsuarios = gestionUsuario()
        aux = self.listboxUsuario.curselection()
        if (self.listboxUsuario.selection_includes(0)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese el identificador de usuario')

            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'El nuevo identificador de ususario es: '.format(aux2))

                gestionUsuarios.modificar_identificacion(aux2, self.id_emp)
                print(aux2)

        if (self.listboxUsuario.selection_includes(1)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese el nuevo nombre de usuario')
            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tu nombre quedo: {}'.format(aux2))
                gestionUsuarios.modificar_nombre(aux2, self.id_emp)
            print(aux2)

        if (self.listboxUsuario.selection_includes(2)):
            print(aux)
            aux3 = askstring('Modificación de información', 'Ingrese el nuevo apellido de usuario')
            if (aux3 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tu apellido quedo: {}'.format(aux3))
                gestionUsuarios.modificar_apellido(aux3, self.id_emp)
            print(aux3)

        if (self.listboxUsuario.selection_includes(3)):
            print(aux)
            aux4 = askstring('Modificación de información', 'Ingrese el nuevo cargo de usuario')
            if (aux4 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tu cargo quedo: {}'.format(aux4))
                gestionUsuarios.modificar_cargo(aux4, self.id_emp)
            print(aux4)

        if (self.listboxUsuario.selection_includes(4)):
            print(aux)
            aux5 = askstring('Modificación de información', 'Ingrese la nueva direccion de usuario')
            if (aux5 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tu direccion quedo: {}'.format(aux5))
                gestionUsuarios.modificar_telefono(aux5, self.id_emp)
            print(aux5)

        if (self.listboxUsuario.selection_includes(5)):
            print(aux)
            aux6 = askstring('Modificación de información', 'Ingrese el nuevo telefono de usuario')
            if (aux6 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Informacion de telefono: {}'.format(aux6))
                gestionUsuarios.modificar_telefono(aux6, self.id_emp)
            print(aux6)


    def CargarInfoUsuarioEnLabels2(self):
        gestionUsuarios = gestionUsuario()
        self.id_emp = gestionUsuarios.obtener_id(self.auxId)
        self.nom_emp = gestionUsuarios.obtener_nombre(self.auxId)
        self.ape_emp = gestionUsuarios.obtener_apellido(self.auxId)
        self.cargo_emp = gestionUsuarios.obtener_cargo(self.auxId)
        self.dir_emp = gestionUsuarios.obtener_direccion(self.auxId)
        self.tel_emp = gestionUsuarios.obtener_telefono(self.auxId)
        #self.contraseña_usu = usuario.get_contraseña()

    def login_window(self):
        self.rootGestEmp.destroy()
        import LoginUsuario

    def volver(self):
        self.rootGestEmp.destroy()
        import  GUIAdministrador as adm
        adm.iniciar()

    def modificarEmpleado(self):
        #self.frameDerechoEmp.place_forget()
        #aux = self.listboxUsuario.curselection()
        auxId =askstring('Modificación de información','Ingrese el identificador de un empleado')
        if (auxId.isidentifier() or not auxId.isnumeric()):
            showinfo('Error', 'Ingrese un identificador valido')
        else:
            auxNombre = askstring('Modificación de información', 'Ingrese el nuevo nombre del empleado')
            gestionUsuario.modificar_nombre(self, auxNombre, auxId)
            auxApellido = askstring('Modificación de información', 'Ingrese el nuevo apellido del empleado')
            gestionUsuario.modificar_apellido(self, auxApellido, auxId)

            auxTel = askstring('Modificación de información', 'Ingrese el nuevo telefono del empleado')
            gestionUsuario.modificar_telefono(self, auxTel, auxId)

            auxDir = askstring('Modificación de información', 'Ingrese el nuevo direccion del empleado')
            gestionUsuario.modificar_direccion(self, auxDir, auxId)

            auxSueldo = askstring('Modificación de información', 'Ingrese el nuevo sueldo del empleado')
            gestionUsuario.modificar_sueldo(self, auxSueldo, auxId)

            auxCargo = askstring('Modificación de información', 'Ingrese el nuevo sueldo del empleado')
            gestionUsuario.modificar_cargo(self, auxCargo, auxId)

            self.rootGestEmp.destroy()
            iniciar()

    def CargarInfoUsuarioEnLabels(self, listboxUsuario):
        gestionUsuarios =gestionUsuario()
        listaDatos = gestionUsuarios.obtenerTodos()

        for x in listaDatos:
            listboxUsuario.insert(END, x)

    def crear(self):
        self.rootGestEmp.destroy()
        import registroUsuario as reg
        reg.iniciar()

    def eliminar(self):
        self.auxId = askstring('Eliminar Usuario', 'Ingrese el identificador de un empleado')
        gestionUsuarios = gestionUsuario()
        gestionUsuarios.deshabilitar_usuario(self.auxId )
        self.rootGestEmp.destroy()
        iniciar()

def iniciar():
    rootGestEmp = Tk()
    obj = GUIMenuInicial(rootGestEmp)
    rootGestEmp.mainloop()