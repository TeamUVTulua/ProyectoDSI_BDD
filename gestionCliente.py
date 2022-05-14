from tkinter import messagebox
from BaseDatos import *
from Usuario import *

user = Usuario("", "", "", "", "", "", "", "")


class gestionCliente:

    def registrar_cliente(self, nit, nombre_cli, apellido1_cli, apellido2_cli, tipo_cli, dirCa_cli, dirNu_cli): # <------- revisar
        self.base = BaseDatos()
        self.query = "insert    into    cliente    VALUES    (%s,%s,%s,%s,%s,%s,%s)"
        self.base.crear_cursor(self.query, (nit, nombre_cli, apellido1_cli, apellido2_cli, tipo_cli, dirCa_cli, dirNu_cli))
        self.base.cerrar_conexion()

    def obtenerTodos(self):
        self.base = BaseDatos()
        self.query = "SELECT nit, nombre, apellidopaterno, apellidomaterno, tipocliente, dircalle, dirnumero FROM cliente"
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    def consultaEspecificaEnFormaDeLista(self, query):
        self.base = BaseDatos()
        self.query = query
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    def consultar_info(self, identificacion):
        self.base = BaseDatos()
        self.query = "SELECT nit, nombre, apellidopaterno, apellidomaterno, tipocliente, dircalle, dirnumero FROM cliente WHERE nit='" + identificacion + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)
        for (nit_cli, nombre_cli, apellido1_cli, apellido2_cli, tipo_cli, dirCa_cli, dirNu_cli) in self.cur:
            self.auxUser=Usuario(nit_cli,nombre_cli,apellido1_cli,apellido2_cli,tipo_cli,dirCa_cli,dirNu_cli)
            user = self.auxUser

        return user

    def modificar_nombre(self, nombre, identificacion):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update cliente set nombre  = %s where nit = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (nombre, identificacion))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

    def modificar_apellido1(self, apellido, identificacion):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update cliente set apellidopaterno  = %s where nit = %s"  # <----
        self.cur = self.base.crear_cursor(self.query, (apellido, identificacion))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

    def modificar_apellido2(self, apellido, identificacion):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update cliente set materno  = %s where nit = %s"  # <----
        self.cur = self.base.crear_cursor(self.query, (apellido, identificacion))
        messagebox.showinfo("modificado", "El apellido ha sido modificado con exito")

        self.base.cerrar_conexion()
    def modificar_tipo(self, tipo, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set tipocliente  = %s where nit = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (tipo, identificacion))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

        self.base.cerrar_conexion()

    def modificar_dirCalle(self, dirCalle, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set dircalle  = %s where nit = %s"
        self.cur = self.base.crear_cursor(self.query, (dirCalle, identificacion))
        messagebox.showinfo("modificado", "El apellido ha sido modificado con exito")
        self.base.cerrar_conexion()

    def modificar_dirNum(self, dirNum, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set dirnumero  = %s where nir = %s"
        self.cur = self.base.crear_cursor(self.query, (dirNum, identificacion))
        messagebox.showinfo("Cambiada", "La direccion ha sido cambiada con exito")
        self.base.cerrar_conexion()
##---------------------------------------------
    def deshabilitar_usuario(self, email):
        self.base = BaseDatos()
        self.query = "update Usuario set activo  = false usuario.email_usuario = %s"
        self.cur = self.base.crear_cursor(self.query, (email))
        messagebox.showinfo("deshabilitado", "El usuario ha sido deshabilitado con exito")
        self.base.cerrar_conexion()

    def habilitar_usuario(self, email):
        self.base = BaseDatos()
        self.query = "update Usuario set activo  = true usuario.email_usuario = %s"
        self.cur = self.base.crear_cursor(self.query, (email))
        messagebox.showinfo("habilitado", "El usuario ha sido habilitado con exito")
        self.base.cerrar_conexion()