class Cliente():

    def __init__(self, rut, nombre, apellido, correo, nacionalidad, password):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.nacionalidad = nacionalidad
        self.password = password

    def __repr__(self):
        return self.rut+self.nombre+self.apellido+self.correo+self.nacionalidad+self.password