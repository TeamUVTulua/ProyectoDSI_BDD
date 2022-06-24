
class Pedido:

    def __init__(self,codigo,producto,proveedor,precioCompra,cantidadCompra):
        self.codgo = codigo
        self.producto = producto
        self.proveedor = proveedor
        self.precioCompra = precioCompra
        self.cantidadCompra = cantidadCompra

    def get_codigo(self):
        return self.codigo

    def get_producto(self):
        return self.producto

    def get_proveedor(self):
        return self.proveedor

    def get_precioCompra(self):
        return self.precioCompra

    def get_cantidadCompra(self):
        return self.cantidadCompra

    # -------------------------------------

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_producto(self, producto):
        self.producto = producto

    def set_proveedor(self, proveedor):
        self.proveedor = proveedor

    def set_precioCompra(self, precioCompra):
        self.precioCompra = precioCompra

    def set_cantidadCompra(self, cantidadCompra):
        self.cantidadCompra = cantidadCompra