from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

class GUIFacturacion:
    def __init__(self, rootGUIFacturacion):
        self.rootGUIFacturacion = rootGUIFacturacion
        self.rootGUIFacturacion.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIFacturacion.geometry("1360x768+560+312")
        self.rootGUIFacturacion.resizable(1, 1)
        self.rootGUIFacturacion.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.rootGUIFacturacion.attributes('-fullscreen', True)


        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIFacturacion, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

