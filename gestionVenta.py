from tkinter import messagebox
from BaseDatos import *
from Venta import *

venta = Venta("", "", "", "","", "")


class gestionVenta:

    # ****** Metodos para registrar ventas en la base de datos ******#

    def registrar_venta(self, codigo_ven, prod_ven, fac_ven, cant_ven, precio_ven, total_ven):
        try:
            self.base = BaseDatos()
            self.query = "insert    into    venta    VALUES    (%s,%s,%s,%s,%s,%s)"
            self.base.crear_cursor(self.query, (codigo_ven, prod_ven, fac_ven, cant_ven, precio_ven, total_ven))
            messagebox.showinfo("Registrado", "La   venta    ha    sido    registrada    con    exito")

            self.base.cerrar_conexion()
        except:
           messagebox.showinfo("Aviso", "venta ya registrada.")

    # ****** Metodo para obtener los datos ******#

    def obtenerTodos(self):
        self.base = BaseDatos()
        self.query = "SELECT codigo, producto, factura, cantidadventa, precioventa , precioventa FROM venta "
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    def total(self, numerofactura):
        self.base = BaseDatos()
        self.query = "SELECT SUM (preciototal) from venta where factura = '" + numerofactura +"'"
        self.cur = self.base.ObtenerDatos(self.query)
        bus = self.cur.fetchone()
        return bus

    # ****** Metodo para consulta de datos ******#

    def consultaEspecificaEnFormaDeLista(self, query):
        self.base = BaseDatos()
        self.query = query
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur


    def consultar_info(self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT codigo, producto, factura, cantidadventa, precioventa FROM venta WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)
        for (cod_ven, prod_ven, fact_ven, cantVen_ven, preVen_ven) in self.cur:
            self.auxUser=venta(cod_ven,prod_ven,fact_ven,cantVen_ven, preVen_ven )
            user = self.auxUser

        return user

    def buscar_info(self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT codigo, producto, factura, cantidadventa, precioventa FROM venta WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        bus = self.cur.fetchone()

        return bus


    # ****** Metodo para la obtencion de datos ******#

    def obtener_codigo (self, cod):
        self.base = BaseDatos()
        self.query = "SELECT codigo FROM venta WHERE codigo ='" + cod + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (cod_prod) in self.cur:
            print(cod_prod)
        return cod_prod

    def obtener_producto (self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT producto FROM venta WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (nom_prod) in self.cur:
            print(nom_prod)
        return nom_prod

    def obtener_factura (self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT factura FROM venta WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (cat_prod) in self.cur:
            print(cat_prod)
        return cat_prod

    def obtener_cantidadTotal (self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT cantidadtotal FROM venta WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (cantidadTotal_prod) in self.cur:
            print(cantidadTotal_prod)
        return cantidadTotal_prod

    def modificar_codigo(self, cod, codigo):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update venta set codigo  = %s where codigo = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (cod, codigo))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

        self.base.cerrar_conexion()

    # ****** Metodo para la modifciacion de los datos ******#

    def modificar_nombre(self, nombre, codigo):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update venta set nombre  = %s where codigo = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (nombre, codigo))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

        self.base.cerrar_conexion()

    def modificar_categoria(self, categoria, codigo):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update venta set categoria  = %s where codigo = %s"  # <----
        self.cur = self.base.crear_cursor(self.query, (categoria, codigo))
        messagebox.showinfo("modificado", "La categoria se ha sido modificado con exito")

        self.base.cerrar_conexion()
    def modificar_cantidad(self, cantidad, codigo):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update venta set cantidad  = %s where codigo = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (cantidad, codigo))
        messagebox.showinfo("modificado", "La cantidad ha sido modificado con exito")

        self.base.cerrar_conexion()

    # ****** Metodo para habilitar ventas ******#

    def deshabilitar_usuario(self, codigo):
        self.base = BaseDatos()
        self.query = "update venta set estado  = false where codigo = '"+ codigo + "'"
        self.cur = self.base.crear_cursor(self.query, (codigo))
        messagebox.showinfo("deshabilitado", "El venta ha sido eliminado con exito")
        self.base.cerrar_conexion()

    # ****** Metodo para deshabilitar ventas ******#

    def habilitar_usuario(self, email):
        self.base = BaseDatos()
        self.query = "update Usuario set activo  = true usuario.email_usuario = %s"
        self.cur = self.base.crear_cursor(self.query, (email))
        mensajeHabilitar = messagebox.showinfo("habilitado", "El venta ha sido habilitado con exito")
        mensajeHabilitar.iconbitmap("Imagenes\iconoInterfaz.ico")
        self.base.cerrar_conexion()
