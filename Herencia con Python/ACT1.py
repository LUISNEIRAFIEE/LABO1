# Clase base Empleado
class Empleado:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}, ID: {self.id}")

    def calcular_salario(self):
        pass  # Este método será definido en las subclases

# Empleado a tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, id, salario_anual):
        super().__init__(nombre, id)
        self.salario_anual = salario_anual

    def calcular_salario(self):
        return self.salario_anual

# Empleado a tiempo parcial
class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, id, tarifa_por_hora, horas_trabajadas):
        super().__init__(nombre, id)
        self.tarifa_por_hora = tarifa_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.tarifa_por_hora * self.horas_trabajadas

# Contratista
class Contratista(Empleado):
    def __init__(self, nombre, id, tarifa_contrato):
        super().__init__(nombre, id)
        self.tarifa_contrato = tarifa_contrato

    def calcular_salario(self):
        return self.tarifa_contrato

# Crear instancias de diferentes tipos de empleados
empleado_full_time = EmpleadoTiempoCompleto("Juan Pérez", 1, 50000)
empleado_part_time = EmpleadoTiempoParcial("Ana López", 2, 20, 25)
contratista = Contratista("Carlos García", 3, 3000)

# Lista de empleados
empleados = [empleado_full_time, empleado_part_time, contratista]

# Mostrar información y calcular salarios
for empleado in empleados:
    empleado.mostrar_informacion()
    print(f"Salario: ${empleado.calcular_salario()}\n")
