
class Proveedor:

    def __init__(self,nit,nombre,contacto,direccion):
        self.nit = nit
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion


    def get_nit(self):
        return self.nit

    def get_nombre(self):
        return self.nombre

    def get_contacto(self):
        return self.contacto

    def get_direccion(self):
        return self.direccion

    # -------------------------------------

    def set_nit(self, nit):
        self.nit = nit

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_contacto(self, contacto):
        self.contacto = contacto

    def set_direccion(self, direccion):
        self.direccion = direccion