import random

#Ejercicio 1
print("EJERCICIO 1")

class Estudiante():
    def __init__(self, legajo, nombre, carrera, institucion, mail, dni):
        self.__legajo = int(legajo)
        self.__nombre = nombre
        self.__carrera = carrera
        self.__institucion = institucion
        self.__mail = mail
        self.__dni = int(dni)
        self.__materias = []
        self.__notas = []
        self.__finales_aprobados = {}
    
    
    #Definimos los metodos getters
    def get_legajo(self):
        return self.__legajo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_carrera(self):
        return self.__carrera
    
    def get_institucion(self):
        return self.__institucion
    
    def get_mail(self):
        return self.__mail
    
    def get_dni(self):
        return self.__dni
    
    def get_materias(self):
        return self.__materias
    
    def get_notas(self):
        return self.__notas
    
    def get_finales_aprobados(self):
        return self.__finales_aprobados
    
    
    #Definimos los metodos Setters
    def set_legajo(self, nuevo_legajo):
        self.__legajo = int(nuevo_legajo)
        
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    def set_carrera(self, nuevo_carrera):
        self.__carrera = nuevo_carrera
        
    def set_institucion(self, nuevo_institucion):
        self.__institucion = nuevo_institucion
        
    def set_mail(self, nuevo_mail):
        self.__mail = nuevo_mail
        
    def set_dni(self, nuevo_dni):
        self.__dni = int(nuevo_dni)
    
    def set_materias(self, nuevo_materias):
        self.__materias = nuevo_materias
    
    def set_notas(self, nuevo_notas):
        self.__notas = nuevo_notas
        
    def set_finales_aprobados(self, nuevo_finales_aprobados):
        self.__finales_aprobados = nuevo_finales_aprobados
        
        
    #Creamos los métodos
    
    def agregar_materia(self, materia_agregar):
        self.__materias.append(materia_agregar)
        print(f"Se ha agregado la materia '{materia_agregar}' al alumno")
        
    def eliminar_materia(self, materia_eliminar):
        self.__materias.remove(materia_eliminar)
        print(f"Se ha eliminado la materia '{materia_eliminar}' al alumno")
    
    def agregar_nota(self, nota_agregar):
        self.__notas.append(nota_agregar)
        print(f"Se ha agregado la nota '{nota_agregar}' al alumno")
        
    def eliminar_nota(self, nota_eliminar):
        self.__notas.remove(nota_eliminar)
        print(f"Se ha eliminado la nota '{nota_eliminar}' al alumno")
    
    def agregar_final(self, final_agregar, nota_final):
        self.__finales_aprobados[final_agregar] = nota_final
        print(f"Se ha agregado el final '{final_agregar}' al alumno con la nota de '{nota_final}'")
    
    def obtener_promedio(self):
        promedio = sum(self.__notas) / len(self.__notas)
        return promedio
    
    def obtener_promedio_finales(self):
        suma_notas = 0
        for final, nota in self.__finales_aprobados.items():
            suma_notas += int(nota)
        promedio_finales = suma_notas / len(self.__finales_aprobados)
        return promedio_finales
    
    def obtener_informacion(self):
        texto = (f"Nombre: {self.__nombre}\nLegajo: {self.__legajo}\nCarrera: {self.__carrera}\nInstitución: {self.__institucion}\nMail: {self.__mail}\nDni: {self.__dni}\nMaterias: {self.__materias}\n")
        return(texto)
    
    
#Ejemplo de uso
#legajo, nombre, carrera, institucion, mail, dni)

# estudiante_1 = Estudiante(10289, "Tomas Romero", "Ingenieria en Sistemas", "UTN San Rafael", "Tomasromero200310@gmail.com", 44771625)
# estudiante_1.agregar_materia("Paradigmas de la Programacion")
# estudiante_1.agregar_materia("Analisis Matematico II")
# notas = [10,8,7,9,10,8,10,7,6,7,7,9,9,9,9]
# estudiante_1.set_notas(notas)

# print(estudiante_1.obtener_promedio())
# print(estudiante_1.obtener_informacion())

#Ejercicio 8
print("EJERCICIO 8")
lista_estudiantes = []
for i in range(6):
    universidad = "UTN San Rafael"
    nombre = input(f"Ingrese el nombre del estudiante 'N° {i+1}': ")
    legajo = input(f"Ingrese el legajo del estudiante 'N° {i+1}': ")
    carrera = input(f"Ingrese la carrera del estudiante 'N° {i+1}': ")
    dni = input(f"Ingrese el dni del estudiante 'N° {i+1}': ")
    mail = nombre + legajo + "@gmail.com"
    
    estudiante = Estudiante(legajo, nombre, carrera, universidad, mail, dni)
    
    final_agregar = ""
    while final_agregar != 'q':
        final_agregar = input("Ingrese la materia que el alumno rindio el final, si no quiere ingresar mas materias ingrese 'q' : ")
        if final_agregar != 'q':
            nota_final = input("Ingrese el numero entero de la nota del final: ")
            lista_estudiantes[i].agregar_final(final_agregar, nota_final)

#Ejemplo de obtener abanderados
lista_promedios = []
for estudiante in lista_estudiantes:
    promedio = estudiante.obtener_promedio_finales()
    lista_promedios.append(promedio)
abanderado = lista_estudiantes[lista_promedios.index(max(lista_promedios))]
print(abanderado.obtener_informacion())

