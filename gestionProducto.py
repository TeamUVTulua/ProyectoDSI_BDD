from tkinter import messagebox
from BaseDatos import *
from Producto import *

prod = Producto("", "", "", "")


class gestionProducto:

    def registrar_producto(self, codigo_pro, nombre_pro, categoria_pro, cantidad_pro):
        self.base = BaseDatos()
        self.query = "insert    into    producto    VALUES    (%s,%s,%s,%s)"
        self.base.crear_cursor(self.query, (codigo_pro, nombre_pro, categoria_pro, cantidad_pro))
        messagebox.showinfo("Registrado", "El    producto    ha    sido    registrado    con    exito")
        self.base.cerrar_conexion()

    def obtenerTodos(self):
        self.base = BaseDatos()
        self.query = "SELECT codigo, nombre, categoria, cantidadtotal FROM producto"
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur


    def consultaEspecificaEnFormaDeLista(self, query):
        self.base = BaseDatos()
        self.query = query
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    def consultar_info(self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT codigo, nombre, categoria, cantidadtotal FROM producto WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)
        for (cod_pro, nombre_pro, cat_pro, cantTotal_pro) in self.cur:
            self.auxUser=Producto(cod_pro,nombre_pro,cat_pro,cantTotal_pro)
            user = self.auxUser

        return user

    def obtener_codigo (self, cod):
        self.base = BaseDatos()
        self.query = "SELECT codigo FROM producto WHERE codigo ='" + cod + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (cod_prod) in self.cur:
            print(cod_prod)
        return cod_prod

    def obtener_nombre (self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT nombre FROM producto WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (nom_prod) in self.cur:
            print(nom_prod)
        return nom_prod

    def obtener_categoria (self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT categoria FROM producto WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (cat_prod) in self.cur:
            print(cat_prod)
        return cat_prod

    def obtener_cantidadTotal (self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT cantidadtotal FROM producto WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (cantidadTotal_prod) in self.cur:
            print(cantidadTotal_prod)
        return cantidadTotal_prod

    def modificar_codigo(self, cod, codigo):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update producto set codigo  = %s where codigo = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (cod, codigo))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

        self.base.cerrar_conexion()


    def modificar_nombre(self, nombre, codigo):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update producto set nombre  = %s where codigo = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (nombre, codigo))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

        self.base.cerrar_conexion()

    def modificar_categoria(self, categoria, codigo):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update producto set categoria  = %s where codigo = %s"  # <----
        self.cur = self.base.crear_cursor(self.query, (categoria, codigo))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "La categoria se ha sido modificado con exito")

        self.base.cerrar_conexion()
    def modificar_cantidad(self, cantidad, codigo):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update producto set cantidad  = %s where codigo = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (cantidad, codigo))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "La cantidad ha sido modificado con exito")

        self.base.cerrar_conexion()

##---------------------------------------------
    def deshabilitar_usuario(self, email):
        self.base = BaseDatos()
        self.query = "update Usuario set activo  = false usuario.email_usuario = %s"
        self.cur = self.base.crear_cursor(self.query, (email))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("deshabilitado", "El usuario ha sido deshabilitado con exito")
        self.base.cerrar_conexion()

    def habilitar_usuario(self, email):
        self.base = BaseDatos()
        self.query = "update Usuario set activo  = true usuario.email_usuario = %s"
        self.cur = self.base.crear_cursor(self.query, (email))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("habilitado", "El usuario ha sido habilitado con exito")
        self.base.cerrar_conexion()
