# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Usuario import *
import Usuario as us
from gestionUsuario import *
usuario=us.Usuario("","","","","","","","")
# ****** Metodos de otros archivos ******#

# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


# ****** Clase GUIMenuInicial ****** #

class GUIMenuInicial:
    def __init__(self, rootGestEmp):
        self.rootGestEmp = rootGestEmp
        self.rootGestEmp.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGestEmp.geometry("1360x768+560+312")
        self.rootGestEmp.resizable(1, 1)
        self.rootGestEmp.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.rootGestEmp.attributes('-fullscreen', True)

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGestEmp, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoEmp = Frame(self.rootGestEmp, bg="#18344A")
        frameIzquierdoEmp.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoEmp, text="Gestion Empleado", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=100, y=30)

        # ****** Boton Consultar Empleados ****** #

        BotonConsultarEmpleados = Button(frameIzquierdoEmp, text="Consultar Empleado", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarEmpleados.place(x=120, y=130, width=240)

        # ****** Boton Crear Empleados ******#

        BotonCrearEmpleados = Button(frameIzquierdoEmp, text="Crear Empleado", command=self.crear,  font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearEmpleados.place(x=120, y=190, width=240)

        # ******Boton Modificar Empleados ****** #

        BotonModificarEmpleados = Button(frameIzquierdoEmp, text="Modificar Empleado",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarEmpleados.place(x=120, y=250, width=240)

        # ******Boton Eliminar Empleado ****** #

        BotonEliminarProducto = Button(frameIzquierdoEmp, text="Eliminar Empleado", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarProducto.place(x=120, y=310, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameIzquierdoEmp, text="Cerrar Sesión", command=self.rootGestEmp.quit, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

        # ****** Frame inicio Productos Side Der ****** #
        frameDerechoEmp = Frame(self.rootGestEmp, bg="#18344A")
        frameDerechoEmp.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Producto ****** #
        Label(frameDerechoEmp, text="Empleados", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=280, y=20)

        self.listboxUsuario = Listbox(frameDerechoEmp, width=40, heigh=9, bg="#18344A", fg="white",
                                      font=("comic sans MS", 20))

        self.CargarInfoUsuarioEnLabels(self.listboxUsuario)

        self.listboxUsuario.place(x=50, y=86)

    def CargarInfoUsuarioEnLabels(self, listboxUsuario):
        #print(usuario.get_nombre())
        gestionUsuarios =gestionUsuario()
        listaDatos = gestionUsuarios.obtenerTodos()

        for x in listaDatos:
            listboxUsuario.insert(END, x)



    def crear(self):
        self.rootGestEmp.destroy()
        mensaje="cucucucu"
        print (mensaje)
        import registroUsuario as reg
        reg.iniciar()

def iniciar():
    rootGestEmp = Tk()
    obj = GUIMenuInicial(rootGestEmp)
    rootGestEmp.mainloop()


rootGestEmp = Tk()
obj = GUIMenuInicial(rootGestEmp)
rootGestEmp.mainloop()