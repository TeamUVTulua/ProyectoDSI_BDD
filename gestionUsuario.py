from tkinter import messagebox
from BaseDatos import *
from Usuario import *
from tkinter.messagebox import showinfo

user = Usuario("", "", "", "", "", "", "", "", "")


class gestionUsuario:

    def registrar_usuario(self, identificacion, nombre_usu, sueldo, telefono_usu, direccion_usu, contraseña, cargo, apellido_usu):
        act = true
        self.base = BaseDatos()
        self.query = "insert    into    empleado    VALUES    (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.base.crear_cursor(self.query, (identificacion, nombre_usu, sueldo, telefono_usu, direccion_usu, contraseña, cargo, apellido_usu, act))
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("Registrado", "El    usuario    ha    sido    registrado    con    exito")
        self.base.cerrar_conexion()

    def login_usuario(self, identificacion, contraseña):
        #try:
        self.base = BaseDatos()
        self.query = "SELECT id_usu, nombre, sueldo, contacto, direccion, contra, cargo, apellido, estado FROM empleado WHERE id_usu =' " + identificacion + "  'and contra='" + contraseña + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print ("aqui")

        for (usu_id, nombre_usu, sueldo_usu, telefono_usu, direccion_usu, contraseña, cargo_usu, apellido_usu,estado_usu) in self.cur:
            self.auxUser=Usuario(usu_id,nombre_usu,sueldo_usu,telefono_usu,direccion_usu,contraseña,cargo_usu,apellido_usu, estado_usu)
            user = self.auxUser
        return user
        #except:
         #   #showinfo.iconbitmap("imagenes\iconointerfaz.ico")
          #  showinfo('Error Inicio de Sesión', 'Usuario o Contraseña Incorrectas')

    def obtenerTodos(self):
        self.base = BaseDatos()
        self.query = "SELECT id_usu, nombre, sueldo, contacto, direccion, contra, cargo, apellido FROM empleado WHERE estado = true"
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

    def buscar_info(self, identificacion):
        self.base = BaseDatos()
        self.query = "SELECT id_usu, nombre, sueldo, contacto, direccion, contra, cargo, apellido FROM empleado WHERE id_usu='" + identificacion + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        bus = self.cur.fetchone()
        #print (bus)
        return bus

    def obtener_id (self, identificador):
        self.base = BaseDatos()
        self.query = "SELECT id_usu FROM empleado WHERE id_usu='" + identificador + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (usu_id) in self.cur:
            print(usu_id)
        return usu_id

    def obtener_nombre (self, identificador):
        self.base = BaseDatos()
        self.query = "SELECT nombre FROM empleado WHERE id_usu='" + identificador + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (nom_id) in self.cur:
            print(nom_id)
        return nom_id

    def obtener_apellido (self, identificador):
        self.base = BaseDatos()
        self.query = "SELECT apellido FROM empleado WHERE id_usu='" + identificador + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (ape_usu) in self.cur:
            print(ape_usu)
        return ape_usu

    def obtener_cargo (self, identificador):
        self.base = BaseDatos()
        self.query = "SELECT cargo FROM empleado WHERE id_usu='" + identificador + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (cargo_usu) in self.cur:
            print(cargo_usu)
        return cargo_usu

    def obtener_direccion (self, identificador):
        self.base = BaseDatos()
        self.query = "SELECT direccion FROM empleado WHERE id_usu='" + identificador + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (dir_usu) in self.cur:
            print(dir_usu)
        return dir_usu

    def obtener_telefono (self, identificador):
        self.base = BaseDatos()
        self.query = "SELECT contacto FROM empleado WHERE id_usu='" + identificador + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)

        for (tel_usu) in self.cur:
            print(tel_usu)
        return tel_usu



    def cambiar_contraseña(self, contraseña, contraseñaActual, identificacion):
        self.base = BaseDatos()
        self.query = "update empleado set contra  = %s where contra = %s and id_usu = %s" #<----
        self.cur = self.base.crear_cursor(self.query, (contraseña, contraseñaActual, identificacion))
        messagebox.showinfo("Cambiada", "La contraseña ha sido cambiada con exito")
        self.base.cerrar_conexion()

    def modificar_identificacion(self, nombre, identificacion):
        print("aquí")
        self.base = BaseDatos()
        self.query = "update empleado set id_usu  = %s where id_usu = %s"  # <----
        self.cur = self.base.crear_cursor(self.query, (nombre, identificacion))
        messagebox.showinfo("modificado", "El nombre ha sido modificado con exito")

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
        messagebox.iconbitmap("Imagenes\iconoInterfaz.ico")
        messagebox.showinfo("modificado", "El telefono ha sido modificado con exito")
        self.base.cerrar_conexion()

##---------------------------------------------
    def deshabilitar_usuario(self, identificacion):
        self.base = BaseDatos()
        self.query = "update empleado set estado  = false where id_usu = '" + identificacion + "'"
        self.cur = self.base.crear_cursor(self.query, (identificacion))
        messagebox.showinfo("deshabilitado", "El usuario ha sido deshabilitado con exito")
        self.base.cerrar_conexion()

    def habilitar_usuario(self, email):
        self.base = BaseDatos()
        self.query = "update Usuario set activo  = true usuario.email_usuario = %s"
        self.cur = self.base.crear_cursor(self.query, (email))
        messagebox.showinfo("habilitado", "El usuario ha sido habilitado con exito")
        self.base.cerrar_conexion()
