# ****** Librerias Usadas ****** #

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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

        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGestEmp, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoEmp = Frame(self.rootGestEmp, bg="#18344A")
        frameIzquierdoEmp.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoEmp, text="Gestion Empleado", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=100, y=30)

        # ****** Boton Consultar Empleados ****** #

        BotonConsultarEmpleados = Button(frameIzquierdoEmp, text="Consultar Empleado", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarEmpleados.place(x=120, y=120, width=240)

        # ****** Boton Crear Empleados ******#

        BotonCrearEmpleados = Button(frameIzquierdoEmp, text="Crear Empleado", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearEmpleados.place(x=120, y=180, width=240)

        # ******Boton Listar Empleados****** #

        BotonListarEmpleados = Button(frameIzquierdoEmp, text="Listar Empleados",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonListarEmpleados.place(x=120, y=240, width=240)

        # ******Boton Modificar Empleados ****** #

        BotonModificarEmpleados = Button(frameIzquierdoEmp, text="Modificar Empleado",font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarEmpleados.place(x=120, y=300, width=240)

        # ******Boton Eliminar Empleado ****** #

        BotonEliminarProducto = Button(frameIzquierdoEmp, text="Eliminar Empleado", font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonEliminarProducto.place(x=120, y=360, width=240)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameIzquierdoEmp, text="Cerrar Sesión", command=self.rootGestEmp.quit, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=120, y=420, width=240)

        # ****** Frame inicio Productos Side Der ****** #
        frameDerechoEmp = Frame(self.rootGestEmp, bg="#18344A")
        frameDerechoEmp.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Producto ****** #
        Label(frameDerechoEmp, text="Productos", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=280, y=20)

def Menuinicio():
    rootGestEmp = Tk()
    obj = GUIMenuInicial(rootGestEmp)
    rootGestEmp.mainloop()


rootGestEmp = Tk()
obj = GUIMenuInicial(rootGestEmp)
rootGestEmp.mainloop()