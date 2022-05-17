# ****** Librerias importadas ******#

from tkinter import messagebox

# ****** Metodos importados de otros archivos ******#

from BaseDatos import *
from Cliente import *

cliente = Cliente("", "", "", "", "", "", "")

# ****** Clase gestionCliente ******#

class gestionCliente:

    # ****** Metodo para registrar clientes en la base de datos ******#
    def registrar_cliente(self, nit, nombre_cli, apellidoPa_cli, apellidoMa_cli, tipo_cli, dirCa_cli, dirNu_cli): # <------- revisar
        self.base = BaseDatos()
        self.query = "insert    into    cliente    VALUES    (%s,%s,%s,%s,%s,%s,%s)"
        self.base.crear_cursor(self.query, (nit, nombre_cli, apellidoPa_cli, apellidoMa_cli, tipo_cli, dirCa_cli, dirNu_cli))
        self.base.cerrar_conexion()

    # ****** Metodo para obtener los datos de los clientes de la base de datos ******#
    def obtenerTodos(self):
        self.base = BaseDatos()
        self.query = "SELECT nit, nombre, apellidopaterno, apellidomaterno, tipocliente, dircalle, dirnumero FROM cliente"
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    # ****** Consultar datos en forma de lista ******#
    def consultaEspecificaEnFormaDeLista(self, query):
        self.base = BaseDatos()
        self.query = query
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    # ****** Conexion con la base de datos ******#
    def consultar_info(self, nit):
        self.base = BaseDatos()
        self.query = "SELECT nit, nombre, apellidopaterno, apellidomaterno, tipocliente, dircalle, dirnumero FROM cliente WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (nit_cli, nombre_cli, apellido1_cli, apellido2_cli, tipo_cli, dirCa_cli, dirNu_cli) in self.cur:
            self.auxUser=Cliente(nit_cli,nombre_cli,apellido1_cli,apellido2_cli,tipo_cli,dirCa_cli,dirNu_cli)
            user = self.auxUser
        return user
    
    def obtener_nit(self, nit):
        self.base = BaseDatos()
        self.query = "SELECT nit FROM cliente WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (nit_cli) in self.cur:
            print(nit_cli)
        return nit_cli
        
    def obtener_nombre (self, nit):
        self.base = BaseDatos()
        self.query = "SELECT nombre FROM cliente WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (nom_cli) in self.cur:
            print(nom_cli)
        return nom_cli

    def obtener_apellidoPaterno (self, nit):
        self.base = BaseDatos()
        self.query = "SELECT apellidopaterno FROM cliente WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (apePa_cli) in self.cur:
            print(apePa_cli)
        return apePa_cli

    def obtener_apellidoMaterno(self, nit):
        self.base = BaseDatos()
        self.query = "SELECT apellidomaterno FROM cliente WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (apeMa_cli) in self.cur:
            print(apeMa_cli)
        return apeMa_cli

    def obtener_tipo (self, nit):
        self.base = BaseDatos()
        self.query = "SELECT tipocliente FROM cliente WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (tipo_cli) in self.cur:
            print(tipo_cli)
        return tipo_cli

    def obtener_dirCalle (self, nit):
        self.base = BaseDatos()
        self.query = "SELECT dircalle FROM cliente WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (dirCa_cli) in self.cur:
            print(dirCa_cli)
        return dirCa_cli

    def obtener_dirNumero(self, nit):
        self.base = BaseDatos()
        self.query = "SELECT dirnumero FROM cliente WHERE nit='" + nit + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (dirNum_cli) in self.cur:
            print(dirNum_cli)
        return dirNum_cli

    def modificar_nit(self, nit, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set nit  = %s where nit = %s"
        self.cur = self.base.crear_cursor(self.query, (nit, identificacion))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "El nit ha sido modificado con exito")

    def modificar_nombre(self, nombre, identificacion):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update cliente set nombre  = %s where nit = %s"
        self.cur = self.base.crear_cursor(self.query, (nombre, identificacion))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "El nit ha sido modificado con exito")

    def modificar_apellido1(self, apellido, identificacion):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update cliente set apellidopaterno  = %s where nit = %s"
        self.cur = self.base.crear_cursor(self.query, (apellido, identificacion))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "El apellido Paterno ha sido modificado con exito")

    def modificar_apellido2(self, apellido, identificacion):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update cliente set apellidomaterno  = %s where nit = %s"
        self.cur = self.base.crear_cursor(self.query, (apellido, identificacion))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "El apellido matenro ha sido modificado con exito")

        self.base.cerrar_conexion()
    def modificar_tipo(self, tipo, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set tipocliente  = %s where nit = %s"
        self.cur = self.base.crear_cursor(self.query, (tipo, identificacion))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "El tipo de cliente ha sido modificado con exito")

        self.base.cerrar_conexion()

    def modificar_dirCalle(self, dirCalle, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set dircalle  = %s where nit = %s"
        self.cur = self.base.crear_cursor(self.query, (dirCalle, identificacion))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "La direccion Calle ha sido modificado con exito")
        self.base.cerrar_conexion()

    def modificar_dirNum(self, dirNum, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set dirnumero  = %s where nir = %s"
        self.cur = self.base.crear_cursor(self.query, (dirNum, identificacion))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("Cambiada", "La direccion numero ha sido cambiada con exito")
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