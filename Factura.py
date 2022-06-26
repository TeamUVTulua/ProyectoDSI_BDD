# ****** Clase Cliente ******#
class Factura:

    # ****** Definicion de lo que compone la clase Factura ******#

    def __init__(self, num, fecha, descuento, tipoPago, valoFinal, cambio, empleado, cliente, monto):
        self.num = num
        self.fecha = fecha
        self.descuento = descuento
        self.tipoPago = tipoPago
        self.valoFinal = valoFinal
        self.cambio = cambio
        self.empleado = empleado
        self.cliente = cliente
        self.monto = monto

    # ****** Metodos get para la clase Factura ******#

    def get_num(self):
        return self.num

    def get_fecha(self):
        return self.fecha

    def get_descuento(self):
        return self.descuento

    def get_tipoPago(self):
        return self.tipoPago

    def get_valorFinal(self):
        return self.valorFinal

    def get_cambio(self):
        return self.cambio

    def get_empleado(self):
        return self.empleado

    def get_cliente(self):
        return self.cliente

    def get_monto(self):
        return self.monto

    # ****** Metodos set para la clase Factura ******#

    def set_num(self, num):
        self.num = num

    def set_fecha(self, nombre):
        self.fecha = nombre

    def set_descuento(self, descuento):
        self.descuento = descuento

    def set_tipoPago(self, tipoPago):
        self.tipoPago = tipoPago

    def set_valoFinal(self, valoFinal):
        self.valoFinal = valoFinal

    def set_cambio(self, cambio):
        self.cambio = cambio

    def set_empleado(self, empleado):
        self.empleado = empleado

    def set_cliente(self, cliente):
        self.cliente = cliente

    def set_monto(self, monto):
        self.monto = monto