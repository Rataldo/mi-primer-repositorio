#en este modulo van solo las clases con sus 4 atributos y 2 metodos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return self.nombre

class Cliente(Persona):
    def __init__(self, nombre, edad, direccion, email):
        super().__init__(nombre, edad)
        self.direccion = direccion
        self.email = email

    def comprar(self, producto):
        print(f"{self.nombre} ha comprado: {producto}.")

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        print(f"el email de {self.nombre} se ha actualizado.")


