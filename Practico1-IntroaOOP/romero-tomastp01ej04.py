#Estudiante: Tomas Agustin Romero | Paradigmas de la Programacion 2024

import math


#Creacion de la clase de Circulo
class Persona:
    def __init__(self, nombre="Tomas", peso=0, altura=0):
        self.__nombre = nombre
        self.__peso = float(peso)
        self.__altura = float(altura)

    #creacion del metodo get
    def get_nombre(self):
        return self.__nombre
    
    def get_peso(self):
        return self.__peso
    
    def get_altura(self):
        return self.__altura
    
    #Creacion de los metodos set
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    def set_peso(self, nuevo_peso):
        self.__peso = float(nuevo_peso)
    
    def set_altura(self, nuevo_altura):
        self.__altura = float(nuevo_altura)
                
    #Creacion de los metodos
    def calculo_imc(self): #Metodo para calcular el indice de masa corporal en base a la altura y el peso
        imc = self.__peso /(self.__altura **2)
        return (f"El indice de masa corporal de {self.__nombre} es: {imc}")

    
#Ejemplo de utilizacion
nombre_ingresada = input("Ingrese el nombre del empleado: ")
peso = input("Ingrese el peso en kilogramos de la persona: ")
altura = input("Ingrese la altura en metros de la persona (ej: 1.75, 1.84, 1.92): ")
persona1 = Persona(nombre_ingresada, peso, altura)

print(persona1.calculo_imc())