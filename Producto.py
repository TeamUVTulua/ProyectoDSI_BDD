
class Producto:

    def __init__(self,codigo,nombre,categoria,cantidadTotal):
        self.codgo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.cantidadTotal = cantidadTotal


    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def get_categoria(self):
        return self.categoria

    def get_cantidadTotal(self):
        return self.cantidadTotal

    # -------------------------------------

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_categoria(self, categoria):
        self.categoria = categoria

    def set_cantidadTotal(self, cantidadTotal):
        self.cantidadTotal = cantidadTotal