# ****** Metodos importados de otros archivos ******#

from BaseDatos import *
from Factura import *

factura = Factura("", "", "", "", "", "", "", "","")


# ****** Clase gestionCliente ******#

class gestionFactura:

    # ****** Metodo para registrar factura en la base de datos ******#

    def registrar_factura(self, num_fac, fecha_fac, des_fac, pago_fac, valor_fac, cambio_fac, emp_fac, cli_fac, monto_fac):
        self.base = BaseDatos()
        self.query = "insert    into    factura    VALUES    (%s,%s,%s,%s,%s,%s,%s,%s, %s)"
        self.base.crear_cursor(self.query,
                               (num_fac, fecha_fac, des_fac, pago_fac, valor_fac, cambio_fac, emp_fac, cli_fac, monto_fac))
        self.base.cerrar_conexion()

    def registrar(self, fecha_fac, pago_fac, valor_fac, cambio_fac, emp_fac, cli_fac, monto_fac, num_fac):
        self.base = BaseDatos()

        fecha = str(fecha_fac)
        pago = str(pago_fac)
        valor = str(valor_fac)
        cambio = str(cambio_fac)
        emp = str(emp_fac)
        cli = str(cli_fac)
        monto = str(monto_fac)
        num = str(num_fac)
        self.query = "update factura set fecha  = '" + fecha + "' , descuento = 10, tipopago = '"+ pago + "', valorfinal = " + valor + ", cambio = "+ cambio +", empleado = "+ emp + ", cliente = "+ cli + ", monto = "+ monto +"  where numerofactura = " + num + ""
        print(self.query)
        self.base.crear_cursor2(self.query)
        self.base.cerrar_conexion()
        messagebox.showinfo("modificado", "El numero de factura ha sido modificado con exito")

    def registrar_codigo(self, num_fac):

        print(num_fac)
        self.base = BaseDatos()
        num = str(num_fac)
        self.query = "INSERT INTO factura (numerofactura) VALUES (" + num_fac + ")"
        print(self.query)
        self.base.crear_cursor2(self.query)
        self.base.cerrar_conexion()

    # ****** Metodo para obtener los datos de las facturas de la base de datos ******#

    def obtenerTodos(self):
        self.base = BaseDatos()
        self.query = "SELECT numerofactura, fecha, descuento, tipopago, valorfinal, cambio, empleado, cliente FROM factura" # --------
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    # ****** Consultar datos en forma de lista ******#

    def consultaEspecificaEnFormaDeLista(self, query):
        self.base = BaseDatos()
        self.query = query
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur

    # ****** Conexion con la base de datos ******#

    def consultar_info(self, numerofactura):
        self.base = BaseDatos()
        self.query = "SELECT numerofactura, fecha, descuento, tipopago, valorfinal, cambio, empleado, cliente FROM factura WHERE numerofactura='" + numerofactura + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        print(self.cur)
        for (num_fac, fecha_fac, des_fac, tipo_fac, val_fac, cambio_fac, emp_fac, cli_fac) in self.cur:
            self.auxUser = Factura(num_fac, fecha_fac, des_fac, tipo_fac, val_fac, cambio_fac, emp_fac,cli_fac )
            user = self.auxUser
        return user

    def buscar_info(self, numerofactura):
        self.base = BaseDatos()
        self.query = "SELECT numerofactura, fecha, descuento, tipopago, valorfinal, cambio, empleado, cliente FROM factura WHERE numerofactura='" + numerofactura + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        bus = self.cur.fetchone()
        return bus


    # ****** Metodos para la obtencion de datos ******#

    def obtener_num(self, numerofactura):
        self.base = BaseDatos()
        self.query = "SELECT numerofactura FROM factura WHERE numerofactura='" + nnumerofacturait + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (numerofactura_cli) in self.cur:
            print(numerofactura_cli)
        return numerofactura_cli

    def obtenerTodosId(self):
        self.base = BaseDatos()
        self.query = "SELECT codigo FROM producto "
        self.cur = self.base.ObtenerTodosLosdatos(self.query)
        return self.cur


    def obtener_fecha(self, numerofactura):
        self.base = BaseDatos()
        self.query = "SELECT fecha FROM factura WHERE numerofactura='" + numerofactura + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (nom_cli) in self.cur:
            print(nom_cli)
        return nom_cli

    def obtener_descuento(self, numerofactura):
        self.base = BaseDatos()
        self.query = "SELECT descuento FROM factura WHERE numerofactura='" + numerofactura + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (apePa_cli) in self.cur:
            print(apePa_cli)
        return apePa_cli

    def obtener_tipoPago(self, numerofactura):
        self.base = BaseDatos()
        self.query = "SELECT tipopago FROM factura WHERE numerofactura='" + numerofactura + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (apeMa_cli) in self.cur:
            print(apeMa_cli)
        return apeMa_cli

    def obtener_valor(self, numerofactura):
        self.base = BaseDatos()
        self.query = "SELECT valorfinal FROM factura WHERE numerofactura='" + numerofactura + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (tipo_cli) in self.cur:
            print(tipo_cli)
        return tipo_cli

    def obtener_cambio(self, numerofactura):
        self.base = BaseDatos()
        self.query = "SELECT cambio FROM factura WHERE numerofactura='" + numerofactura + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (dirCa_cli) in self.cur:
            print(dirCa_cli)
        return dirCa_cli

    def obtener_empleado(self, numerofactura):
        self.base = BaseDatos()
        self.query = "SELECT empleado FROM factura WHERE numerofactura='" + numerofactura + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (dirNum_cli) in self.cur:
            print(dirNum_cli)
        return dirNum_cli

    def obtener_cliente(self, numerofactura):
        self.base = BaseDatos()
        self.query = "SELECT cliente FROM factura WHERE numerofactura='" + numerofactura + "'"
        self.cur = self.base.ObtenerDatos(self.query)
        for (dirNum_cli) in self.cur:
            print(dirNum_cli)
        return dirNum_cli

    # ****** Metodos para modificacion de datos ******#

    def modificar_numerofactura(self, numerofactura, identificacion):
        self.base = BaseDatos()
        self.query = "update factura set numerofactura  = %s where numerofactura = %s"
        self.cur = self.base.crear_cursor(self.query, (numerofactura, identificacion))
        messagebox.showinfo("modificado", "El numero de la factura ha sido modificado con exito", )

    def modificar_nombre(self, nombre, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set nombre  = %s where numerofactura = %s"
        self.cur = self.base.crear_cursor(self.query, (nombre, identificacion))
        messagebox.showinfo("modificado", "El nombre del cliente en la factura ha sido modificado con exito")

    def modificar_apellido1(self, apellido, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set apellidopaterno  = %s where numerofactura = %s"
        self.cur = self.base.crear_cursor(self.query, (apellido, identificacion))
        messagebox.showinfo("modificado", "El apellido Paterno en la factura ha sido modificado con exito")

    def modificar_apellido2(self, apellido, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set apellidomaterno  = %s where numerofactura = %s"
        self.cur = self.base.crear_cursor(self.query, (apellido, identificacion))
        messagebox.showinfo("modificado", "El apellido matenro en la factura ha sido modificado con exito")

        self.base.cerrar_conexion()

    def modificar_tipo(self, tipo, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set tipocliente  = %s where numerofactura = %s"
        self.cur = self.base.crear_cursor(self.query, (tipo, identificacion))
        messagebox.showinfo("modificado", "El tipo de cliente en la ha sido modificado con exito")

        self.base.cerrar_conexion()

    def modificar_dirCalle(self, dirCalle, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set dircalle  = %s where numerofactura = %s"
        self.cur = self.base.crear_cursor(self.query, (dirCalle, identificacion))
        messagebox.showinfo("modificado", "La direccion Calle en la factura ha sido modificado con exito")
        self.base.cerrar_conexion()

    def modificar_dirNum(self, dirNum, identificacion):
        self.base = BaseDatos()
        self.query = "update cliente set dirnumero  = %s where nir = %s"
        self.cur = self.base.crear_cursor(self.query, (dirNum, identificacion))
        messagebox.showinfo("Cambiada", "La direccion numero en la factura ha sido cambiada con exito")
        self.base.cerrar_conexion()

    # ****** Metodo para deshabilitar usuarios ******#

    def deshabilitar_usuario(self, numerofactura):
        self.base = BaseDatos()
        self.query = "update cliente set estado  = false where numerofactura = '" + numerofactura + "'"
        self.cur = self.base.crear_cursor(self.query, (numerofactura))
        messagebox.showinfo("deshabilitado", "El Cliente en ha sido deshabilitado con exito")
        self.base.cerrar_conexion()