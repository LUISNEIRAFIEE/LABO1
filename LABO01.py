class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def hacer_sonido(self):
        return "Sonido de animal"
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"
# Crear una instancia de Perro
mi_perro = Perro("Fido", 4)
# Mostrar atributos y métodos
print(f"Mi perro se llama {mi_perro.nombre} y tiene {mi_perro.edad} años.")
print(f"Mi perro dice: {mi_perro.hacer_sonido()}")