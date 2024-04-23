#Estudiante: Tomas Agustin Romero | Paradigmas de la Programacion 2024

import math


#Creacion de la clase de Circulo
class Circulo:
    def __init__(self, radio=1):
        self.__radio = float(radio)
        
    #creacion del metodo get
    def get_radio(self):
        return self.__radio
    
    #Creacion de los metodos set
    def set_radio(self, nuevo_radio):
        self.__radio = float(nuevo_radio)
                
    #Creacion de los metodos
    def calculo_area(self): #calculo del area del circulo
        area = math.pi * (self.__radio**2)
        return area
    
    def calculo_circunferencia(self): #calculo del circunferencia del circulo
        circunferencia = self.__radio * 2 * math.pi
        return circunferencia
    
    #metodo para obtener en texto todos los datos y operaciones relacionadas al objeto
    def get_valores(self):
        return (f"Los valores ingresados son:\nRadio: {self.__radio}\nCircunferencia = {self.calculo_circunferencia()}\nÁrea = {self.calculo_area()}")


#Ejemplo de utilizacion
radio_ingresada = input("Ingrese el radio del circulo: ") 
circulo1 = Circulo(radio_ingresada) #Define a una variable una instancia de la clase circulo

print(circulo1.get_valores()) #Imprimimos el texto devuelto por el metodo de los valores