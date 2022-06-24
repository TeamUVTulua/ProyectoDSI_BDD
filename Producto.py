
class Producto:

    def __init__(self,codigo,nombre,categoria,cantidadTotal,estado):
        self.codgo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.cantidadTotal = cantidadTotal
        self.estado = estado

    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def get_categoria(self):
        return self.categoria

    def get_cantidadTotal(self):
        return self.cantidadTotal

    def get_estado(self):
        return self.estado

    # -------------------------------------

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_categoria(self, categoria):
        self.categoria = categoria

    def set_cantidadTotal(self, cantidadTotal):
        self.cantidadTotal = cantidadTotal

    def set_estado(self, estado):
        self.estado = estado