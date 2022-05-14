from tkinter import messagebox
from BaseDatos import *
from Usuario import *

user = Usuario("", "", "", "", "", "", "", "")


class gestionUsuario:

    def registrar_usuario(self, identificacion, nombre_usu, sueldo, telefono_usu, direccion_usu, contraseña, cargo, apellido_usu):
        self.base = BaseDatos()
        self.query = "insert    into    empleado    VALUES    (%s,%s,%s,%s,%s,%s,%s,%s)"
        self.base.crear_cursor(self.query, (identificacion, nombre_usu, sueldo, telefono_usu, direccion_usu, contraseña, cargo, apellido_usu))
        messagebox.showinfo("Registrado", "El    usuario    ha    sido    registrado    con    exito")
        self.base.cerrar_conexion()

    def login_usuario(self, identificacion, contraseña):
        self.base = BaseDatos()
        self.query = "SELECT id_usu, nombre, sueldo, contacto, direccion, contra, cargo, apellido FROM empleado WHERE id_usu =' " + identificacion + "  'and contra='" + contraseña + "'"
        self.cur = self.base.ObtenerDatos(self.query)

        # auxUser=Usuario(email_usuario,id_rol,contraseña,num_id_usu,fecha_ingreso,nom_usu,apellido,direcc_usu,tel_usu,activo)

        for (usu_id, nombre_usu, sueldo_usu, telefono_usu, direccion_usu, contraseña, cargo_usu, apellido_usu) in self.cur:
            self.auxUser=Usuario(usu_id,nombre_usu,sueldo_usu,telefono_usu,direccion_usu,contraseña,cargo_usu,apellido_usu)
            user = self.auxUser

        return user

    def obtenerTodos(self):
        self.base = BaseDatos()
        self.query = "SELECT id_usu, nombre, sueldo, contacto, direccion, contra, cargo, apellido FROM empleado"
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    def consultaEspecificaEnFormaDeLista(self, query):
        self.base = BaseDatos()
        self.query = query
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    def consultar_info(self, identificacion):
        self.base = BaseDatos()
        self.query = "SELECT id_usu, nombre, sueldo, contacto, direccion, contra, cargo, apellido FROM empleado WHERE id_usu='" + identificacion + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)
        for (usu_id, nombre_usu, sueldo_usu, telefono_usu, direccion_usu, contraseña, cargo_usu, apellido_usu) in self.cur:
            self.auxUser=Usuario(usu_id,nombre_usu,sueldo_usu,telefono_usu,direccion_usu,contraseña,cargo_usu,apellido_usu)
            user = self.auxUser

        return user


    def cambiar_contraseña(self, contraseña, contraseñaActual, identificacion):
        self.base = BaseDatos()
        self.query = "update empleado set contra  = %s where contra = %s and id_usu = %s" #<----
        self.cur = self.base.crear_cursor(self.query, (contraseña, contraseñaActual, identificacion))
        messagebox.showinfo("Cambiada", "La contraseña ha sido cambiada con exito")
        self.base.cerrar_conexion()

    def modificar_nombre(self, nombre, identificacion):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update empleado set nombre  = %s where id_usu = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (nombre, identificacion))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

    def modificar_cargo(self, cargo, identificacion):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update empleado set cargo  = %s where id_usu = %s"  # <----
        self.cur = self.base.crear_cursor(self.query, (cargo, identificacion))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

        self.base.cerrar_conexion()
    def modificar_sueldo(self, sueldo, identificacion):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update empleado set sueldo  = %s where id_usu = %s" # <----
        self.cur = self.base.crear_cursor(self.query, (sueldo, identificacion))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

        self.base.cerrar_conexion()

    def modificar_apellido(self, apellido, identificacion):
        self.base = BaseDatos()
        self.query = "update empleado set apellido  = %s where id_usu = %s"
        self.cur = self.base.crear_cursor(self.query, (apellido, identificacion))
        messagebox.showinfo("modificado", "El apellido ha sido modificado con exito")
        self.base.cerrar_conexion()

    def modificar_direccion(self, direccion_usu, identificacion):
        self.base = BaseDatos()
        self.query = "update empleado set direccion  = %s where id_usu = %s"
        self.cur = self.base.crear_cursor(self.query, (direccion_usu, identificacion))
        messagebox.showinfo("Cambiada", "La direccion ha sido cambiada con exito")
        self.base.cerrar_conexion()

    def modificar_telefono(self, telefono_usu, identificacion):
        self.base = BaseDatos()
        self.query = "update empleado set contacto  = %s where id_usu = %s"
        self.cur = self.base.crear_cursor(self.query, (telefono_usu, identificacion))
        messagebox.showinfo("modificado", "El telefono ha sido modificado con exito")
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
