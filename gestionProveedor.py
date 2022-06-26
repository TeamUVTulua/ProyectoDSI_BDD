# ****** Librerias usadas ******#

from tkinter import messagebox

# ****** Metodos usados de otros archivos ******#

from BaseDatos import *
from Proveedor import *

proveedor = Proveedor("", "", "", "", "")


# ****** Clase gestionProveedor ******#

class gestionProveedor:

    # ****** Metodo para registrar los datos ******#

    def registrar_proveedor(self, nit_prov, nombre_prov, contacto_prov,direccion_prov):
        act = True
        self.base = BaseDatos()
        self.query = "insert    into    proveedor    VALUES    (%s,%s,%s,%s, %s)"
        self.base.crear_cursor(self.query, (nit_prov, nombre_prov, contacto_prov, direccion_prov, act))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("Registrado", "El    proveedor    ha    sido    registrado    con    exito")
        self.base.cerrar_conexion()

    # ****** Conexion con la base de datos ******#

    def obtenerTodos(self):
        self.base = BaseDatos()
        self.query = "SELECT nit, nombre, contacto, direccion FROM proveedor where estado = true"
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    def buscar_info(self, nit):
        self.base = BaseDatos()
        self.query = "SELECT nit FROM proveedor where nit = '" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        bus = self.cur.fetchone()
        return bus


    def consultaEspecificaEnFormaDeLista(self, query):
        self.base = BaseDatos()
        self.query = query
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    def consultar_info(self, nit):
        self.base = BaseDatos()
        self.query = "SELECT SELECT nit, nombre, contacto, direccion FROM proveedor WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)
        for (nit_prov, nombre_prov, contacto_prov, direccion_prov) in self.cur:
            self.auxUser=Proveedor(nit_prov,nombre_prov,contacto_prov,direccion_prov)
            user = self.auxUser

        return user

    def obtener_nit (self, cod):
        self.base = BaseDatos()
        self.query = "SELECT nit FROM proveedor WHERE nit ='" + cod + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (nit_prov) in self.cur:
            print(nit_prov)
        return nit_prov

    def obtener_nombre (self, nit):
        self.base = BaseDatos()
        self.query = "SELECT nombre FROM proveedor WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (nom_prov) in self.cur:
            print(nom_prov)
        return nom_prov

    def obtener_contacto (self, nit):
        self.base = BaseDatos()
        self.query = "SELECT contacto FROM proveedor WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (cont_prov) in self.cur:
            print(cont_prov)
        return cont_prov

    def obtener_direccion(self, nit):
        self.base = BaseDatos()
        self.query = "SELECT direccion FROM proveedor WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (dir_prov) in self.cur:
            print(dir_prov)
        return dir_prov

    def modificar_nit(self, cod, nit):
        self.base = BaseDatos()
        self.query = "update proveedor set nit  = %s where nit = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (cod, nit))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "El nit ha sido modificado con exito")

        self.base.cerrar_conexion()


    def modificar_nombre(self, nombre, nit):
        self.base = BaseDatos()
        self.query = "update proveedor set nombre  = %s where nit = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (nombre, nit))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

        self.base.cerrar_conexion()

    def modificar_contacto(self, contacto, nit):
        self.base = BaseDatos()
        self.query = "update proveedor set contacto  = %s where nit = %s"  # <----
        self.cur = self.base.crear_cursor(self.query, (contacto, nit))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "La contacto se ha sido modificado con exito")

        self.base.cerrar_conexion()
    def modificar_direccion(self, direccion, nit):
        self.base = BaseDatos()
        self.query = "update proveedor set direccion  = %s where nit = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (direccion, nit))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "La direccion ha sido modificado con exito")

        self.base.cerrar_conexion()

##---------------------------------------------
    def deshabilitar_usuario(self, nit):
        self.base = BaseDatos()
        self.query = "update proveedor set estado  = false where nit = '" + nit +"'"
        self.cur = self.base.crear_cursor(self.query, (nit))
        messagebox.showinfo("deshabilitado", "El proveedor ha sido deshabilitado con exito")
        self.base.cerrar_conexion()

    def habilitar_usuario(self, email):
        self.base = BaseDatos()
        self.query = "update Usuario set activo  = true usuario.email_usuario = %s"
        self.cur = self.base.crear_cursor(self.query, (email))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("habilitado", "El usuario ha sido habilitado con exito")
        self.base.cerrar_conexion()
