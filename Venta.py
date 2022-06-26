
class Venta:

    def __init__(self,codigo,producto,factura,cantidadVenta,precioVenta, precioTotal):
        self.codgo = codigo
        self.producto = producto
        self.factura = factura
        self.cantidadVenta = cantidadVenta
        self.precioVenta = precioVenta
        self.precioTotal = precioTotal

    def get_codigo(self):
        return self.codigo

    def get_producto(self):
        return self.producto

    def get_factura(self):
        return self.factura

    def get_cantidadVenta(self):
        return self.cantidadVenta

    def get_precioVenta(self):
        return self.precioVenta

    def get_precioTotal(self):
        return self.precioTotal

    # -------------------------------------

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_producto(self, producto):
        self.producto = producto

    def set_factura(self, factura):
        self.factura = factura

    def set_cantidadVenta(self, cantidadVenta):
        self.cantidadVenta = cantidadVenta

    def set_precioVenta(self, precioVenta):
        self.precioVenta = precioVenta

    def set_precioTotal(self, precioTotal):
        self.precioTotal = precioTotal