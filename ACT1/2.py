class Perro:
    contador_perros = 0 # Atributo de clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Perro.contador_perros += 1
    @classmethod
    def cantidad_perros(cls):
        return cls.contador_perros
    @staticmethod
    def es_cachorro(edad):
        return edad < 1
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")
        
# Crear instancias de la clase Perro
perro1 = Perro("Fido", 3)
perro2 = Perro("Max", 0.5)
# Usar método de clase
print(f"Se han creado {Perro.cantidad_perros()} perros.")
# Usar método estático
print(f"¿Es {perro2.nombre} un cachorro? {'Sí' if Perro.es_cachorro(perro2.edad) else 'No'}")