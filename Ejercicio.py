# Dennis Amaru Cruz Abrego
# Versión 1
# 09/04/2025

#Se define la clase Estudiante
class Estudiante:
    #Se define los atributos de la clase
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []
        
    #Función para agregar calificaciones
    def agregar_calificaciones(self, nuevasCalificaciones):
        self.calificaciones.extend(nuevasCalificaciones)
        
    #Función para calcular el promedio
    def promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0.0

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.promedio():.2f}")


def validarDatosInt(datoInt):
    return isinstance(datoInt, int) and datoInt > 0

def validarDatosFloat(datoFloat):
    return isinstance(datoFloat, float) and 0 <= datoFloat <= 100

def buscarEstudiante(nombre, opcion):
    encontrado = False
    for estudiante in listaEstudiantes:
        if estudiante.nombre == nombre:
            print("Estudiante encontrado.")
            if opcion == 1:
                calificacionNueva = float(input("Digite la nueva calificación: "))
                if validarDatosFloat(calificacionNueva):
                    estudiante.agregar_calificaciones([calificacionNueva])
                else:
                    print("Calificación no válida.")
            elif opcion == 2:
                estudiante.mostrar_info()
            encontrado = True
            break
    
    if not encontrado:
        print("Estudiante no encontrado.")


def menu():
    print("+-" * 25)
    print("1. Registrar nuevo estudiante")
    print("2. Agregar calificación a un estudiante")
    print("3. Mostrar información de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir del programa")
    print("+-" * 25)
    opcion = int(input("Escribe una opción: "))
    return opcion


# Lógica principal del programa
listaEstudiantes = []

opcion = 0

while opcion != 5:
    opcion = menu()
    
    match opcion:
        case 1:
            nombreAux = input("Digite el nombre del nuevo estudiante: ")
            edadAux = int(input("Digite la edad del nuevo estudiante: "))
            carreraAux = input("Digite la carrera del nuevo estudiante: ")

            cantidadCalificaciones = int(input("Digite cuántas calificaciones va a ingresar: "))

            calificacionesAux = []
            for i in range(cantidadCalificaciones):
                nota = float(input("Ingrese la calificación: "))
                calificacionesAux.append(nota)

            estudiante = Estudiante(nombreAux, edadAux, carreraAux)
            estudiante.agregar_calificaciones(calificacionesAux)
            listaEstudiantes.append(estudiante)

        case 2:
            nombreBuscado = input("Digite el nombre del estudiante: ")
            buscarEstudiante(nombreBuscado, 1)

        case 3:
            nombreBuscado = input("Digite el nombre del estudiante: ")
            buscarEstudiante(nombreBuscado, 2)

        case 4:
            for estudiante in listaEstudiantes:
                estudiante.mostrar_info()

        case _:
            print("Opción no válida")

print("Adiós")