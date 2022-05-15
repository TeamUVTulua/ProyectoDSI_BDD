
class Cliente:

    def __init__(self,nit,nombre,apellidoPaterno,apellidoMaterno,tipo,dirCalle,dirNumero):
        self.nit = nit
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.tipo = tipo
        self.dirCalle = dirCalle
        self.dirNumero = dirNumero

    def get_nit(self):
        return self.nit

    def get_nombre(self):
        return self.nombre

    def get_apellidoPaterno(self):
        return self.apellidoPaterno

    def get_apellidoMaterno(self):
        return self.apellidoMaterno

    def get_tipoCliente(self):
        return self.tipo

    def get_dirCalle(self):
        return self.dirCalle

    def get_dirNum(self):
        return self.dirNumero

    # -------------------------------------

    def set_nit(self, nit):
        self.nit = nit

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellidoPaterno(self, apellidoPaterno):
        self.apellidoPaterno = apellidoPaterno

    def set_apellidoMaterno(self, apellidoMaterno):
        self.apellidoMaterno = apellidoMaterno

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_dirCalle(self, dirCalle):
        self.dirCalle = dirCalle

    def set_dirNum(self, dirNumero):
        self.dirNumero = dirNumero