class Usuario:
    def __init__(self,tipo,nombre,apellido,fecha,genero,usuario,password,telefono):
        self.tipo = tipo
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.genero = genero
        self.usuario = usuario
        self.password = password
        self.telefono = telefono

class Doctor(Usuario):
    def __init__(self,tipo,nombre,apellido,fecha,genero,usuario,password,especialidad,telefono):
        super().__init__(lado,lado)
        self.usuario = usuario
        self.especialidad = especialidad