from tkinter import messagebox
from BaseDatos import *


class GestionProducto:

    def registrar_producto(self, codigo, nombre, valor_venta, descripcion):
        self.base = BaseDatos()

        self.query = "insert into producto VALUES (%s,%s,%s,%s,%s,%s)"
        self.base.crear_cursor(self.query, (codigo, 1, nombre, valor_venta, descripcion, 10))
        messagebox.showinfo("Registrado", "El producto ha sido registrado con exito")

        self.base.cerrar_conexion()

    def registrar_producto_preparado(self, codigo, nombre, valor_venta, descripcion, insumo_requerido,
                                     cantidad_requerida):
        self.base = BaseDatos()
        self.base2 = BaseDatos()

        self.query = "insert into producto VALUES (%s,%s,%s,%s,%s,%s)"
        self.base.crear_cursor(self.query, (codigo, 2, nombre, valor_venta, descripcion, 10))
        messagebox.showinfo("Registrado", "El producto ha sido registrado con exito")
        self.query2 = "insert into necesita_ins VALUES (%s,%s,%s,%s)"
        self.base2.crear_cursor(self.query2, (5, codigo, insumo_requerido, cantidad_requerida))

        self.base.cerrar_conexion()
        self.base2.cerrar_conexion()

    def obtenerTodos1(self):
        self.base = BaseDatos()
        self.query = "SELECT cod_prod, tipo, nom_pro, valor_venta_prod, descrip_prod, nit_restau  FROM producto where producto.tipo = '1'"
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    def obtenerTodos2(self):
        self.base = BaseDatos()
        self.query = "SELECT cod_prod, tipo, nom_pro, valor_venta_prod, descrip_prod, nit_restau  FROM producto where producto.tipo = '2'"
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    def registrar_insumo(self, codigo, nombre, costo):
        self.base = BaseDatos()

        self.query = "insert into insumo VALUES (%s,%s,%s)"
        self.base.crear_cursor(self.query, (codigo, nombre, costo))
        messagebox.showinfo("Registrado", "El insumo ha sido registrado con exito")

        self.base.cerrar_conexion()

    def registrar_inventario(self, codigo, codigo_insumo, cantidad, tipo_unidad, observacion, fecha_ingreso):
        self.base = BaseDatos()

        self.query = "insert into inventario VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        self.base.crear_cursor(self.query, (
        codigo, codigo_insumo, fecha_ingreso, cantidad, tipo_unidad, "Laura", 10000, observacion))
        messagebox.showinfo("Registrado", "El producto ha sido registrado con exito")

        self.base.cerrar_conexion()

    def modificar_cantidad(self, cantidad, codigo, codigo_insumo):
        self.base = BaseDatos()
        self.query = "update inventario set cantidad  = '%s' where inventario.codigo = '%s' and inventario.codigo_insumo = '%s'"
        self.cur = self.base.crear_cursor(self.query, (cantidad, codigo, codigo_insumo))
        messagebox.showinfo("modificado", "la cantidad ha sido modificado con exito")
        self.base.cerrar_conexion()

    def modificar_tipo_unidad(self, tipo_unidad, codigo, codigo_insumo):
        self.base = BaseDatos()
        self.query = "update inventario set tipo_unidad  = '%s' where inventario.codigo = '%s' and inventario.codigo_insumo = '%s'"
        self.cur = self.base.crear_cursor(self.query, (tipo_unidad, codigo, codigo_insumo))
        messagebox.showinfo("modificado", "el tipo de unidad ha sido modificado con exito")
        self.base.cerrar_conexion()

    def modificar_observacion(self, observacion, codigo, codigo_insumo):
        self.base = BaseDatos()
        self.query = "update inventario set observacion  = '%s' where inventario.codigo = '%s' and inventario.codigo_insumo = '%s'"
        self.cur = self.base.crear_cursor(self.query, (observacion, codigo, codigo_insumo))
        messagebox.showinfo("modificado", "la observacion ha sido modificado con exito")
        self.base.cerrar_conexion()

    def modificar_fecha_ingreso(self, fecha_ingreso, codigo, codigo_insumo):
        self.base = BaseDatos()
        self.query = "update inventario set fecha_ingreso  = '%s' where inventario.codigo = '%s' and inventario.codigo_insumo = '%s'"
        self.cur = self.base.crear_cursor(self.query, (fecha_ingreso, codigo, codigo_insumo))
        messagebox.showinfo("modificado", "la fecha de ingreso ha sido modificado con exito")
        self.base.cerrar_conexion()
