# ****** Librerias Usadas ****** #

from tkinter import *
from PIL import ImageTk

# ****** Metodos de otros archivos ******#

from gestionUsuario import *
from gestionFactura import *
from gestionPedido import *
usuario=Usuario("","","","","","","","","")

# ******Ventanas de dialogo ******#

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

# ****** Clase GUIContador ****** #


class GUIContador:

    def __init__(self, rootGUIContador):
        self.rootGUIContador = rootGUIContador
        self.rootGUIContador.title("Sistema de Inventario y Ventas MotoSocios")
        self.rootGUIContador.geometry("1366x768")
        self.rootGUIContador.resizable(1, 1)
        self.rootGUIContador.iconbitmap("Imagenes\iconoInterfaz.ico")


        # ******logo de Fondo****** #

        self.bg = ImageTk.PhotoImage(file="Imagenes\FondoInterfaz2.png")
        Label(self.rootGUIContador, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame inicio Productos Side Der ****** #

        self.frameDerechoContador = Frame(self.rootGUIContador, bg="#18344A")
        self.frameDerechoContador.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(self.frameDerechoContador, text="Bienvenido, Contador", font=("comic sans MS", 24, "bold"), bg="#18344A",fg="white").place(x=180, y=20)

        # ****** Datos del perfil ****** #

        Label(self.frameDerechoContador, text="Identificador: ", font=("comic sans MS", 16,), bg="#18344A", fg="white").place( x=80, y=100)
        Label(self.frameDerechoContador, text="Nombre: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80, y=140)
        Label(self.frameDerechoContador, text="Apellido: ", font=("comic sans MS", 16,), bg="#18344A", fg="white").place(x=80, y=180)
        Label(self.frameDerechoContador, text="Telefono:", font=("comic sans MS", 16,), bg="#18344A", fg="white").place(x=80, y=300)
        Label(self.frameDerechoContador, text="Direccion:", font=("comic sans MS", 16,), bg="#18344A", fg="white").place(x=80,y=260)
        Label(self.frameDerechoContador, text="Cargo:", font=("comic sans MS", 16,), bg="#18344A", fg="white").place(x=80,y=220)

        # ****** Cargar datos del vendedor en el frame ****** #
        self.CargarInfoUsuarioEnLabels()
        # ****** Informacion que no se modifica ****** #
        Label(self.frameDerechoContador, text=self.id_usu, font=("comic sans MS", 16,), bg="#18344A", fg="white").place(
            x=270, y=100)
        Label(self.frameDerechoContador, text=self.nombre_usu, font=("comic sans MS", 16), bg="#18344A",
              fg="white").place(
            x=270, y=140)
        Label(self.frameDerechoContador, text=self.apellido_usu, font=("comic sans MS", 16), bg="#18344A",
              fg="white").place(x=270, y=180)
        Label(self.frameDerechoContador, text=self.cargo_usu, font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=270, y=220)

        self.listboxUsuario = Listbox(self.frameDerechoContador, width=25, height=2, bg="#18344A", fg="white",
                                      font=("comic sans MS", 16,))

        self.listboxUsuario.insert(0, self.dir_usu)
        self.listboxUsuario.insert(1, self.tel_usu)

        self.listboxUsuario.place(x=270, y=260)

        # ****** Botones Perfil Propio ****** #

        BotonModificarDatos = Button(self.frameDerechoContador, text="Modificar datos",
                                     command=self.retornarSelecListBoxUsuario,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonModificarDatos.place(x=80, y=400, width=240)

        BotonCambiarContraseña = Button(self.frameDerechoContador, text="Cambiar Contraseña",
                                        command=self.modContraseña,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCambiarContraseña.place(x=380,y=400, width=240)

        # ******Frame Botones Opciones Side Izq ****** #

        frameIzquierdoContador = Frame(self.rootGUIContador, bg="#18344A")
        frameIzquierdoContador.place(x=85, y=85, width=480, height=530)
        Label(frameIzquierdoContador, text="Contador", font=("comic sans MS", 23, "bold"), bg="#18344A", fg="white").place(x=170, y=30)

        # ****** Boton Consultar Historico de Ventas ****** #

        BotonConsultarHV = Button(frameIzquierdoContador, text="Consultar Venta", command = self.mostrarVen,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarHV.place(x=80, y=120, width=320)

        # ****** Boton Consultar Historico de Compras ******#

        BotonConsultarHC = Button(frameIzquierdoContador, text="Consultar Pedido",  command = self.consCompra,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarHC.place(x=80, y=180, width=320)

        # ****** Boton Consultar Datos Empleados ****** #

        BotonConsultarDatosEmp = Button(frameIzquierdoContador, text="Consultar Empleados",command = self.consEmp ,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarDatosEmp.place(x=80, y=240, width=320)

        # ******Boton Crear Pago a Empleados ****** #

        BotonCrearPagoEmp = Button(frameIzquierdoContador, text="Salario Total de Empleados", command = self.salarioTotal,font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearPagoEmp.place(x=80, y=300, width=320)

        # ******Boton Crear Pago a Proveedores ****** #

        BotonCrearPagoProv = Button(frameIzquierdoContador, text="Pago Total a Proveedores", command = self.pagoProv , font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonCrearPagoProv.place(x=80, y=360, width=320)

        # ******Boton Salir ****** #

        BotonSalir = Button(frameIzquierdoContador, text="Cerrar Sesión", command=self.login, font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=80, y=420, width=320)

    # ****** Metodo para iniciar la interfaz desde otra ****** #

    def salarioTotal(self):
        ges = gestionUsuario()
        total =  ges.obtener_salarioTotal()
        total1 = int('.'.join(str(ele) for ele in total))
        tota = str(total1)
        res = messagebox.askyesno(message="¿Desea Pagar el salario de los empleado? \n Salario = " + tota, title="Salario Total")
        if res:
            showinfo('Pagos', 'Salario a Empleados Pagado')
        else:
            showinfo('Pagos', 'No se pagó salario a empleados')

    def pagoProv(self):
        ges = gestionPedido()
        total =  ges.obtener_total()
        res = int('.'.join(str(ele) for ele in total))
        mostrar = str(res)
        res = messagebox.askyesno(message="¿Desea Pagar a los proveedores? \n Pago Total = " + mostrar, title="Pago Total")
        if res:
            showinfo('Pagos', 'Pago a Proveedores Pagado')
        else:
            showinfo('Pagos', 'No se pagó a Proveedores')

    def consEmp(self):
        self.auxId = askstring('Consulta', 'Ingrese el codigo del empelado')
        self.frameDerechoContador.place_forget()
        self.mostrarEmp()
    
    def consVenta(self):
        self.auxId = askstring('Consulta', 'Ingrese el codigo de una venta')

        self.frameDerechoContador.place_forget()
        self.mostrarVenta()

    def mostrarVen(self):
        frameDerechoContador = Frame(self.rootGUIContador, bg="#18344A")
        frameDerechoContador.place(x=600, y=85, width=700, height=530)

        self.listboxUsuario = Listbox(frameDerechoContador, width=50, height=12, bg="#18344A", fg="white",
                                      font=("comic sans MS", 16))

        self.listboxUsuario.get

        self.CargarInfoUsuarioEnLabelsFac(self.listboxUsuario)

        self.listboxUsuario.place(x=25, y=86)
        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoContador, text="Facturas", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=220, y=40)

        BotonConsultarHV = Button(frameDerechoContador, text="Buscar Venta", command=self.consVenta,
                                  font=("comic sans MS", 15), bg="gray", fg="white", bd=5, cursor="hand2")
        BotonConsultarHV.place(x=380,y=450, width=240)

        # ****** Datos del perfil ****** #

    def CargarInfoUsuarioEnLabelsFac(self, listboxUsuario):
        gestionUsuarios =gestionFactura()
        listaDatos = gestionUsuarios.obtenerTodos()

        for x in listaDatos:
            listboxUsuario.insert(END, x)

    def consCompra(self):
        self.auxId = askstring('Consulta', 'Ingrese el codigo de un pedido')
        self.frameDerechoContador.place_forget()
        self.mostrarPedido()
        
    def mostrarVenta(self):
        frameDerechoContador = Frame(self.rootGUIContador, bg="#18344A")
        frameDerechoContador.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoContador, text="Factura", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=220, y=40)

        # ****** Datos del perfil ****** #

        Label(frameDerechoContador, text="Numero Factura: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80, y=90)
        Label(frameDerechoContador, text="Fecha: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                                 y=120)
        Label(frameDerechoContador, text="Tipo de Pago: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80,
            y=150)
        Label(frameDerechoContador, text="Valor Final:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                                  y=180)

        Label(frameDerechoContador, text="Cambio:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80,y=210)

        Label(frameDerechoContador, text="Empleado:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80, y=240)

        Label(frameDerechoContador, text="Cliente:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80, y=270)

        Label(frameDerechoContador, text="Monto Pago:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80, y=300)

        self.CargarInfoUsuarioEnLabels2()

        self.listboxProducto = Listbox(frameDerechoContador, width=25, height=8, bg="#18344A", fg="white",
                                       font=("comic sans MS", 16))

        self.listboxProducto.insert(0, self.num)
        self.listboxProducto.insert(1, self.fecha)
        self.listboxProducto.insert(2, self.tipo)
        self.listboxProducto.insert(3, self.valor)
        self.listboxProducto.insert(4, self.cambio)
        self.listboxProducto.insert(5, self.emp)
        self.listboxProducto.insert(6, self.cli)
        self.listboxProducto.insert(7, self.monto)

        self.listboxProducto.place(x=270, y=90)

    def mostrarPedido(self):
        frameDerechoContador = Frame(self.rootGUIContador, bg="#18344A")
        frameDerechoContador.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoContador, text="Pedido", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=220, y=40)

        # ****** Datos del perfil ****** #

        Label(frameDerechoContador, text="Codigo: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80, y=90)
        Label(frameDerechoContador, text="Producto: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                                 y=120)
        Label(frameDerechoContador, text="Proveedor: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80,
            y=150)
        Label(frameDerechoContador, text="Precio Compra:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                                  y=180)

        Label(frameDerechoContador, text="Cantidad Compra:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80,y=210)

        self.CargarInfoUsuarioEnLabels3()

        self.listboxProducto2 = Listbox(frameDerechoContador, width=25, height=5, bg="#18344A", fg="white",
                                       font=("comic sans MS", 16))

        self.listboxProducto2.insert(0, self.cod)
        self.listboxProducto2.insert(1, self.prod)
        self.listboxProducto2.insert(2, self.prov)
        self.listboxProducto2.insert(3, self.com)
        self.listboxProducto2.insert(4, self.cant)

        self.listboxProducto2.place(x=270, y=90)

    def mostrarEmp(self):
        print("****__")
        frameDerechoContador = Frame(self.rootGUIContador, bg="#18344A")
        frameDerechoContador.place(x=600, y=85, width=700, height=530)

        # ******* Titulo Frame Bienvenido ****** #

        Label(frameDerechoContador, text="Empleado", font=("comic sans MS", 24, "bold"), bg="#18344A",
              fg="white").place(x=220, y=40)

        # ****** Datos del perfil ****** #

        Label(frameDerechoContador, text="Identificacion: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80, y=90)
        Label(frameDerechoContador, text="Nombre: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                                 y=120)
        Label(frameDerechoContador, text="Apellido: ", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80,
            y=150)
        Label(frameDerechoContador, text="Contacto:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(x=80,
                                                                                                                  y=180)

        Label(frameDerechoContador, text="Direccion:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80,y=210)

        Label(frameDerechoContador, text="Cargo:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80, y=240)

        Label(frameDerechoContador, text="Sueldo:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80, y=270)

        Label(frameDerechoContador, text="Estado:", font=("comic sans MS", 16), bg="#18344A", fg="white").place(
            x=80, y=300)

        self.CargarInfoUsuarioEnLabels4()

        self.listboxProducto4 = Listbox(frameDerechoContador, width=25, height=8, bg="#18344A", fg="white",
                                       font=("comic sans MS", 16))

        self.listboxProducto4.insert(0, self.id)
        self.listboxProducto4.insert(1, self.nombre)
        self.listboxProducto4.insert(2, self.apellido)
        self.listboxProducto4.insert(3, self.cont)
        self.listboxProducto4.insert(4, self.dir)
        self.listboxProducto4.insert(5, self.cargo)
        self.listboxProducto4.insert(6, self.sueldo)
        self.listboxProducto4.insert(7, self.estado)

        self.listboxProducto4.place(x=270, y=90)

    
    def CargarInfoUsuarioEnLabels(self):

        self.id_usu = usuario.get_id_usu()
        self.nombre_usu = usuario.get_nombre()
        self.apellido_usu = usuario.get_apellido()
        self.cargo_usu = usuario.get_cargo()
        self.dir_usu = usuario.get_direccion()
        self.tel_usu = usuario.get_telefono()
        self.contraseña_usu = usuario.get_contraseña()

    def retornarSelecListBoxUsuario(self):
        gestionUsuarios = gestionUsuario()
        aux = self.listboxUsuario.curselection()
        if (self.listboxUsuario.selection_includes(0)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese la nueva direccion de usuario')

            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tu direccion quedó:  {}'.format(aux2))

                gestionUsuarios.modificar_direccion(aux2, self.id_usu)
                print(aux2)

        if (self.listboxUsuario.selection_includes(1)):
            print(aux)
            aux2 = askstring('Modificación de información', 'Ingrese la nueva telefono de usuario')
            if (aux2 == None):
                showinfo('Modificación de información', 'No se realizó ningun cambio')
            else:
                showinfo('Modificación de información', 'Tus telefono quedaron: {}'.format(aux2))
                gestionUsuarios.modificar_telefono(aux2, usuario.get_id_usu())
            print(aux2)

    def CargarInfoUsuarioEnLabels2(self):
        gestionUsuarios = gestionFactura()
        self.num = gestionUsuarios.obtener_num(self.auxId)
        self.fecha = gestionUsuarios.obtener_fecha(self.auxId)
        self.tipo = gestionUsuarios.obtener_tipoPago(self.auxId)
        self.valor = gestionUsuarios.obtener_valor(self.auxId)
        self.cambio = gestionUsuarios.obtener_cambio(self.auxId)
        self.emp = gestionUsuarios.obtener_empleado(self.auxId)
        self.cli = gestionUsuarios.obtener_cliente(self.auxId)
        self.monto = gestionUsuarios.obtener_monto(self.auxId)

    def CargarInfoUsuarioEnLabels4(self):
        gestionUsuarios = gestionUsuario()
        self.id = gestionUsuarios.obtener_id(self.auxId)
        self.nombre = gestionUsuarios.obtener_nombre(self.auxId)
        self.sueldo = gestionUsuarios.obtener_sueldo(self.auxId)
        self.cont = gestionUsuarios.obtener_telefono(self.auxId)
        self.dir = gestionUsuarios.obtener_direccion(self.auxId)
        self.cargo = gestionUsuarios.obtener_cargo(self.auxId)
        self.apellido = gestionUsuarios.obtener_apellido(self.auxId)
        self.estado = gestionUsuarios.obtener_estado(self.auxId)

    def CargarInfoUsuarioEnLabels3(self):
        gestionUsuarios = gestionPedido()
        self.cod = gestionUsuarios.obtener_codigo(self.auxId)
        self.prod = gestionUsuarios.obtener_producto(self.auxId)
        self.prov = gestionUsuarios.obtener_proveedor(self.auxId)
        self.com = gestionUsuarios.obtener_precioCompra(self.auxId)
        self.cant = gestionUsuarios.obtener_cantidadCompra(self.auxId)

    def modContraseña(self):
        gestionUsuarios=gestionUsuario()
        nuevaContraseña=""
        confirNuevaContra=""
        contraseñaActual = askstring('Cambiar contraseña', 'Escribe tu contraseña actual')
        if(contraseñaActual==self.contraseña_usu):
            nuevaContraseña=askstring('Cambiar contraseña', 'Escribe tu nueva contraseña')
            if (contraseñaActual==nuevaContraseña):
                showinfo('Cambiar contraseña','La contraseña es igual a la antigua, trata con otra')
            else:
                confirNuevaContra=askstring('Cambiar contraseña', 'Confirma tu nueva contraseña')
                if(nuevaContraseña==confirNuevaContra):
                    showinfo('Cambiar contraseña','Cambio exitoso, vuelve a hacer login')
                    gestionUsuarios.cambiar_contraseña(confirNuevaContra, usuario.get_contraseña(),usuario.get_id_usu())
                    self.login()
                else:
                    showinfo('Cambiar contraseña','Las contraseñas no coinciden')
        if(contraseñaActual==None):
                showinfo('Modificación de información','No se realizó ningun cambio')
        else:
            showinfo('Cambiar contraseña','Contraseña incorrecta')

    # ****** Metodo para iniciar la interfaz desde otra ****** #

    def login(self):
        self.rootGUIContador.destroy()
        import LoginUsuario as l
        l.iniciar()

def iniciar():
     rootGUIContador = Tk()
     obj = GUIContador(rootGUIContador)
     rootGUIContador.mainloop()
