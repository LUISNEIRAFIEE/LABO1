# Clase base Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def rol_universidad(self):
        pass  # Método polimórfico que será implementado en las subclases

class Departamento:
    def __init__(self, nombre_departamento):
        self.nombre_departamento = nombre_departamento

    def mostrar_informacion(self):
        print(f"Departamento: {self.nombre_departamento}")

class Asignatura:
    def __init__(self, nombre_asignatura):
        self.nombre_asignatura = nombre_asignatura

    def mostrar_informacion(self):
        print(f"Asignatura: {self.nombre_asignatura}")

class Profesor(Persona):
    def __init__(self, nombre, edad, departamento, asignatura):
        super().__init__(nombre, edad)
        self.departamento = departamento  # Composición: Un profesor pertenece a un departamento
        self.asignatura = asignatura  # Composición: Un profesor enseña una asignatura

    def rol_universidad(self):
        print(f"Profesor: {self.nombre} enseña {self.asignatura.nombre_asignatura} en el departamento de {self.departamento.nombre_departamento}.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera, asignaturas):
        super().__init__(nombre, edad)
        self.carrera = carrera  # El estudiante pertenece a una carrera
        self.asignaturas = asignaturas  # Composición: El estudiante cursa varias asignaturas

    def rol_universidad(self):
        print(f"Estudiante: {self.nombre} está estudiando {self.carrera} y cursa las siguientes asignaturas:")
        for asignatura in self.asignaturas:
            asignatura.mostrar_informacion()

departamento_ciencias = Departamento("FACULTAD DE INGENIERIA ELECTRICA Y ELECTRONICA")
asignaturall = Asignatura("Ecuaciones Diferenciales")
asignatural= Asignatura("Economia")

profesor1 = Profesor("Ing. Jorge Cornejo ", 45, departamento_ciencias, asignaturall)

asignaturas_estudiante = [asignaturall, asignatural]
estudiante1 = Estudiante("LUIS FERNANDO", 19, "Ingeniería", asignaturas_estudiante)

personas = [profesor1, estudiante1]

# Mostrar información y comportamiento polimórfico
for persona in personas:
    persona.mostrar_informacion()
    persona.rol_universidad()
    print()
