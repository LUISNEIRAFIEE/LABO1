# Clase base Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}")

# Clase derivada Electrónica
class Electronica(Producto):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)
        self.garantia = garantia

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Garantía: {self.garantia} años")

# Clase derivada Alimentos
class Alimentos(Producto):
    def __init__(self, nombre, precio, fecha_expiracion):
        super().__init__(nombre, precio)
        self.fecha_expiracion = fecha_expiracion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Fecha de expiración: {self.fecha_expiracion}")

# Crear instancias de productos
televisor = Electronica("Televisor", 300, 2)
manzana = Alimentos("Manzana", 1, "2024-12-31")

# Mostrar información de los productos
productos = [televisor, manzana]

for producto in productos:
    producto.mostrar_informacion()
    print()
