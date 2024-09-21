class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")
# Crear una instancia de la clase Perro
mi_perro = Perro("Fido", 3)
# Acceder a los atributos
print(f"Mi perro se llama {mi_perro.nombre} y tiene {mi_perro.edad}años.")
# Llamar al método ladrar
mi_perro.ladrar()