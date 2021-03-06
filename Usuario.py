# ****** Clase Usuario ****** #
class Usuario:

    def __init__(self,id_usu,nombre,sueldo,telefono,direccion,contraseña,cargo,apellido, estado):
        self.id_usu = id_usu
        self.nombre = nombre
        self.sueldo = sueldo
        self.telefono = telefono
        self.direccion = direccion
        self.contraseña = contraseña
        self.cargo = cargo
        self.apellido = apellido
        self.estado = estado

    # ****** Gest de Usuario ****** #
    def get_id_usu(self):
        return self.id_usu

    def get_contraseña(self):
        return self.contraseña

    def get_cargo(self):
        return self.cargo

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_telefono(self):
        return self.telefono

    def get_direccion(self):
        return self.direccion

    def get_sueldo(self):
        return self.sueldo

    def get_estado(self):
        return self.estado

    # ****** Sets de usuario ****** #
    def set_id_usu(self, id_usu):
        self.id_usu = id_usu

    def set_contraseña(self, contraseña):
        self.contraseña = contraseña

    def set_cargo(self, cargo):
        self.cargo = cargo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_sueldo(self, sueldo):
        self.sueldo = sueldo

    def set_estado(self, estado):
        self.estado = estado