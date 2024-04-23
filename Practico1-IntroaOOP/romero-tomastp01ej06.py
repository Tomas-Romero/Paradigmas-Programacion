#Estudiante: Tomas Agustin Romero | Paradigmas de la Programacion 2024

import math


#Creacion de la clase de la Maquina Calculadora
class Computo:
    def __init__(self):
        self.__numero = 0

    #creacion del metodo get
    def get_numero(self):
        return self.__numero
        
    #Creacion de los metodos set
    def set_numero(self, nuevo_numero):
        self.__numero = float(nuevo_numero)
                    
    #Creacion de los metodos
    def factorial(self):
        total_factorial = 1
        for i in range(self.__numero + 1):
            total_factorial += total_factorial * i
        return total_factorial
    
    
    def calculadora(self):
        texto = (f"Los numero ingresados son: {self.__numero}\nEl calculo a kilonumero es: {self.numero_a_kilonumero()}\nEl calculo a centinumero es: {self.numero_a_centinumero()}")
        return texto
#Ejemplo de utilizacion
numero_ingresado = input("Ingrese los numero para convertirlos: ")
numero1 = Computo()

numero1.set_numero(7)
print(numero1.calculadora())