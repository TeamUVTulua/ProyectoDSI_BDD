# ****** Librerias usadas ******#

from tkinter import messagebox
from BaseDatos import *
from Pedido import *

pedido = Pedido("", "", "", "","")

# ****** clase gestionPedido ******#

class gestionPedido:

    # ****** Metodos para registrar productos en la base de datos ******#

    def registrar_pedido(self, codigo_ped, producto_ped, proveedor_ped, precio_ped, cantidad_ped):
        try:
            self.base = BaseDatos()
            self.query = "insert    into    surtido    VALUES    (%s,%s,%s,%s,%s)"
            self.base.crear_cursor(self.query, (codigo_ped, producto_ped, proveedor_ped, precio_ped, cantidad_ped))
            messagebox.showinfo("Registrado", "El pedido ha sido registrado con exito")
            self.base.cerrar_conexion()
        except:
            messagebox.showinfo("Aviso", "El pedido ya se encuentra registrado.")

    # ****** Metodo para obtener los datos ******#

    def obtenerTodos(self):
        self.base = BaseDatos()
        self.query = "SELECT * FROM surtido "
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        print(self.cur)
        return self.cur

    def obtenerTodosId(self):
        self.base = BaseDatos()
        self.query = "SELECT codigo FROM producto "
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        print(self.cur)
        return self.cur

    def obtenerTodosNit(self):
        self.base = BaseDatos()
        self.query = "SELECT nit FROM proveedor "
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        print(self.cur)
        return self.cur

    # ****** Metodo para consulta de datos ******#

    def consultaEspecificaEnFormaDeLista(self, query):
        self.base = BaseDatos()
        self.query = query
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        print(self.cur)
        return self.cur


    def consultar_info(self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT * FROM surtido WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)
        for (cod_ped, prod_ped, prov_ped, precio_ped, cant_ped) in self.cur:
            self.auxUser=Pedido(cod_ped,prod_ped,prov_ped,precio_ped,cant_ped)
            user = self.auxUser

        return user

    def buscar_info(self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT * FROM surtido WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)
        bus = self.cur.fetchone()
        return bus


    # ****** Metodo para la obtencion de datos ******#

    def obtener_codigo (self, cod):
        self.base = BaseDatos()
        self.query = "SELECT codigo FROM surtido WHERE codigo ='" + cod + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (cod_prod) in self.cur:
            print(cod_prod)
        return cod_prod

    def obtener_producto (self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT producto FROM surtido WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (prod_ped) in self.cur:
            print(prod_ped)
        return prod_ped

    def obtener_proveedor (self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT proveedor FROM surtido WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (prov_ped) in self.cur:
            print(prov_ped)
        return prov_ped

    def obtener_precioCompra (self, codigo):
        self.base = BaseDatos()
        print ("aquii")
        self.query = "SELECT preciocompra FROM surtido WHERE codigo ='" + codigo + "'"
        print(self.query)
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (precio) in self.cur:
            print(precio)
        return precio

    def obtener_cantidadCompra (self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT cantidadcompra FROM surtido WHERE codigo='" + codigo + "'"

        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (cantidadCompra_ped) in self.cur:
            print(cantidadCompra_ped)
        return cantidadCompra_ped

    # ****** Metodo para la modifciacion de los datos ******#

    def modificar_codigo(self, cod, codigo):
        self.base = BaseDatos()
        self.query = "update surtido set codigo  = %s where codigo = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (cod, codigo))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

        self.base.cerrar_conexion()

    def modificar_nombre(self, nombre, codigo):
        self.base = BaseDatos()
        self.query = "update producto set nombre  = %s where codigo = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (nombre, codigo))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

        self.base.cerrar_conexion()

    def modificar_categoria(self, categoria, codigo):
        self.base = BaseDatos()
        self.query = "update producto set categoria  = %s where codigo = %s"  # <----
        self.cur = self.base.crear_cursor(self.query, (categoria, codigo))
        messagebox.showinfo("modificado", "La categoria se ha sido modificado con exito")

        self.base.cerrar_conexion()
    def modificar_cantidad(self, cantidad, codigo):
        self.base = BaseDatos()
        self.query = "update producto set cantidad  = %s where codigo = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (cantidad, codigo))
        messagebox.showinfo("modificado", "La cantidad ha sido modificado con exito")

        self.base.cerrar_conexion()

    # ****** Metodo para deshabilitar productos ******#

    def deshabilitar_producto(self, codigo):
        self.base = BaseDatos()
        self.query = "update producto set estado  = false where codigo = '"+ codigo + "'"
        self.cur = self.base.crear_cursor(self.query, (codigo))
        messagebox.showinfo("deshabilitado", "El producto ha sido eliminado con exito")
        self.base.cerrar_conexion()

    # ****** Metodo para habilitar productos ******#

    def habilitar_producto(self, email):
        self.base = BaseDatos()
        self.query = "update Usuario set activo  = true usuario.email_usuario = %s"
        self.cur = self.base.crear_cursor(self.query, (email))
        mensajeHabilitar = messagebox.showinfo("habilitado", "El producto ha sido habilitado con exito")
        mensajeHabilitar.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.base.cerrar_conexion()
