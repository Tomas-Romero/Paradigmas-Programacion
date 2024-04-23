#Estudiante: Tomas Agustin Romero | Paradigmas de la Programacion 2024

import math


#Creacion de la clase de Circulo
class Empleado:
    def __init__(self, nombre="tomas", horas_trabajadas=0, tarifa_hora=0):
        self.__nombre = nombre
        self.__horas_trabajadas = float(horas_trabajadas)
        self.__tarifa_hora = float(tarifa_hora)

    #creacion del metodo get
    def get_nombre(self):
        return self.__nombre
    
    def get_horas_trabajadas(self):
        return self.__horas_trabajadas
    
    def get_tarifa_hora(self):
        return self.__tarifa_hora
    
    #Creacion de los metodos set
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    def set_horas_trabajadas(self, nuevo_horas_trabajadas):
        self.__horas_trabajadas = float(nuevo_horas_trabajadas)
    
    def set_tarifa_hora(self, nuevo_tarifa_hora):
        self.__tarifa_hora = float(nuevo_tarifa_hora)
                
    #Creacion de los metodos
    def calculo_salario(self): #Metodo para calcular el salario en base a las horas trabajadas y lo que cobra por hora
        salario = self.__horas_trabajadas * self.__tarifa_hora
        return (f"El salario de {self.__nombre} en cuanto a sus horas trabajadas y la tarifa es de: ${salario}")

    
#Ejemplo de utilizacion
nombre_ingresada = input("Ingrese el nombre del empleado: ")
horas_ingresada = input("Ingrese las horas que trabajo el empleado: ")
tarifa_ingresada = input("Ingrese la tarifa por hora del empleado: ")
empleado1 = Empleado(nombre_ingresada, horas_ingresada, tarifa_ingresada)

print(empleado1.calculo_salario())