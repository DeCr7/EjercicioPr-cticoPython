#Autor: Dennis Amaru Cruz Abrego
#Versión 1
#Fecha: 09/04/2025

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
            #Se calcula el promedio sumando todos los valores en self.calificaciones y la cantidad de valores en self.calificaciones
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0.0
    
    #Función para mostrar la información del estudiante seleccionado/buscado
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        #Limita el promedio a dos decimales
        print(f"Promedio: {self.promedio():.2f}")

#Función para validar datos enteros
def validarDatosInt(datoInt):
    #Comprueba si el valor introducido es entero y mayor a 0
    return isinstance(datoInt, int) and datoInt > 0

#Función para validar datos flotantes
def validarDatosFloat(datoFloat):
    #Comprueba si el valor introducido es entero y mayor a 0
    return isinstance(datoFloat, float) and 0 <= datoFloat <= 100

#Función para buscar el estudiante
def buscarEstudiante(nombre, opcion):
    #Se define el valor "encontrado" para verificar si el estudiante fue encontrado posteriormente en el código
    encontrado = False
    for estudiante in listaEstudiantes:
        if estudiante.nombre == nombre:
            print("Estudiante encontrado.")
            #En caso de que se busque añadir una calificación
            if opcion == 1:
                calificacionNueva = float(input("Digite la nueva calificación: "))
                if validarDatosFloat(calificacionNueva):
                    estudiante.agregar_calificaciones([calificacionNueva])
                else:
                    print("Calificación no válida.")
            #En caso de que solo se busque mostrar los datos del estudiante
            elif opcion == 2:
                estudiante.mostrar_info()
            encontrado = True
            break
    
    if not encontrado:
        print("Estudiante no encontrado.")

#Función para mostrar el menú
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


#Definición de la lista de estudiantes
listaEstudiantes = []

#Definición de la variable opcion
opcion = 0

#Cuerpo del código, haciendo uso de un while se mantiene el programa corriendo hasta que el usuario salga
while opcion != 5:
    #Llamada a la función de menu()
    opcion = menu()
    
    #Match según la opcion digitada
    match opcion:
        case 1:
            nombreAux = input("Digite el nombre del nuevo estudiante: ")
            edadAux = int(input("Digite la edad del nuevo estudiante: "))
            carreraAux = input("Digite la carrera del nuevo estudiante: ")

            cantidadCalificaciones = int(input("Digite cuántas calificaciones va a ingresar: "))

            calificacionesAux = []
            for i in range(cantidadCalificaciones):
                nota = float(input("Ingrese la calificación: "))
                #Se agrega la nota
                calificacionesAux.append(nota)
                
            #Se agregan los datos nombre, edad y carrera
            estudiante = Estudiante(nombreAux, edadAux, carreraAux)
            #Llamada a la función de agregar calificaciones
            estudiante.agregar_calificaciones(calificacionesAux)
            listaEstudiantes.append(estudiante)

        case 2:
            nombreBuscado = input("Digite el nombre del estudiante: ")
            #Llamada a la primera opción de la función buscarEstudiantes
            buscarEstudiante(nombreBuscado, 1)

        case 3:
            nombreBuscado = input("Digite el nombre del estudiante: ")
            #Llamada a la segunda opción de la función buscarEstudiantes
            buscarEstudiante(nombreBuscado, 2)

        case 4:
            for estudiante in listaEstudiantes:
                #Llamada a la función mostrar_info, hasta que se muestren todos los estudiantes
                estudiante.mostrar_info()

        case _:
            print("Opción no válida")

print("Adiós")