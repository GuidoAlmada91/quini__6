class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"NOMBRE: {self.nombre, self.apellido}"