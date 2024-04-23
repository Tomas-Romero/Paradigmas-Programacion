#Estudiante: Tomas Agustin Romero | Paradigmas de la Programacion 2024

import math


#Creacion de la clase de la Maquina Calculadora
class MaquinaCalculadora:
    def __init__(self, metros=0):
        self.__metros = float(metros)

    #creacion del metodo get
    def get_metros(self):
        return self.__metros
        
    #Creacion de los metodos set
    def set_metros(self, nuevo_metros):
        self.__metros = float(nuevo_metros)
                    
    #Creacion de los metodos
    def metros_a_kilometros(self):
        kilometros = self.__metros/1000
        return kilometros
    
    def metros_a_centimetros(self):
        centimetros = self.__metros * 100
        return centimetros
    
    def calculadora(self):
        texto = (f"Los metros ingresados son: {self.__metros}\nEl calculo a kilometros es: {self.metros_a_kilometros()}\nEl calculo a centimetros es: {self.metros_a_centimetros()}")
        return texto
#Ejemplo de utilizacion
metros_ingresado = input("Ingrese los metros para convertirlos: ")
metros1 = MaquinaCalculadora(metros_ingresado)

print(metros1.calculadora())