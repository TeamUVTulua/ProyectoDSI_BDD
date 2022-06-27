from BaseDatos import *
from Producto import *

prod = Producto("", "", "", "","")


class gestionProducto:

    # ****** Metodos para registrar productos en la base de datos ******#

    def registrar_producto(self, codigo_pro, nombre_pro, categoria_pro, cantidad_pro):
        try:
            act = True
            self.base = BaseDatos()
            self.query = "insert    into    producto    VALUES    (%s,%s,%s,%s,%s)"
            self.base.crear_cursor(self.query, (codigo_pro, nombre_pro, categoria_pro, cantidad_pro, act))
            messagebox.showinfo("Registrado", "El producto ha sido registrado con exito")
            self.base.cerrar_conexion()
        except:
            messagebox.showinfo("Aviso", "Producto ya registrado.")

    # ****** Metodo para obtener los datos ******#

    def obtenerTodos(self):
        self.base = BaseDatos()
        self.query = "SELECT codigo, nombre, categoria, cantidadtotal FROM producto where estado = true"
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
        self.query = "SELECT codigo, nombre, categoria, cantidadtotal FROM producto WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)
        for (cod_pro, nombre_pro, cat_pro, cantTotal_pro) in self.cur:
            self.auxUser=Producto(cod_pro,nombre_pro,cat_pro,cantTotal_pro)
            user = self.auxUser
            print(self.cur)
        return user

    def buscar_info(self, codigo):
        self.base = BaseDatos()
        self.query = "SELECT codigo, nombre, categoria, cantidadtotal FROM producto WHERE codigo='" + codigo + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        bus = self.cur.fetchone()
        print(self.cur)
        return bus


    # ****** Metodo para la obtencion de datos ******#

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
        messagebox.showinfo("modificado", "El codigo ha sido modificado con exito")

        self.base.cerrar_conexion()

    # ****** Metodo para la modifciacion de los datos ******#

    def modificar_nombre(self, nombre, codigo):
        self.base = BaseDatos()
        self.query = "update producto set nombre  = %s where codigo = %s"
        self.cur = self.base.crear_cursor(self.query, (nombre, codigo))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

        self.base.cerrar_conexion()

    def modificar_categoria(self, categoria, codigo):
        self.base = BaseDatos()
        self.query = "update producto set categoria  = %s where codigo = %s"
        self.cur = self.base.crear_cursor(self.query, (categoria, codigo))
        messagebox.showinfo("modificado", "La categoria se ha sido modificado con exito")

        self.base.cerrar_conexion()
    def modificar_cantidad(self, cantidad, codigo):
        self.base = BaseDatos()
        self.query = "update producto set cantidadtotal   = %s where codigo = %s"
        self.cur = self.base.crear_cursor(self.query, (cantidad, codigo))
        messagebox.showinfo("modificado", "La cantidad ha sido modificado con exito")

        self.base.cerrar_conexion()

    # ****** Metodo para deshabilitar productos ******#

    def deshabilitar_usuario(self, codigo):
        self.base = BaseDatos()
        self.query = "update producto set estado  = false where codigo = '"+ codigo + "'"
        self.cur = self.base.crear_cursor(self.query, (codigo))
        messagebox.showinfo("deshabilitado", "El producto ha sido eliminado con exito")
        self.base.cerrar_conexion()

    # ****** Metodo para habilitar productos ******#

    def habilitar_usuario(self, codigo):
        self.base = BaseDatos()
        self.query = "update producto set estado  = true where codigo = '" + codigo + "'"
        self.cur = self.base.crear_cursor(self.query, (codigo))
        messagebox.showinfo("habilitado", "El producto ha sido habilitado con exito")
        self.base.cerrar_conexion()
