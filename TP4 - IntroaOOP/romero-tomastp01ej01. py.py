#Estudiante: Tomas Agustin Romero | Paradigmas de la Programacion 2024

#Creacion de la clase de rectangulo
class Rectangulo:
    def __init__(self, base=1, altura=1):
        self.__base = float(base)
        self.__altura = float(altura)
        
    #creacion del metodo get
    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura
    
    #Creacion de los metodos set
    def set_base(self, nueva_base):
        self.__base = float(nueva_base)
        
    def set_altura(self, nueva_altura):
        self.__altura = float(nueva_altura)
        
    #Creacion de los metodos
    def calculo_area(self): #calculo del area del rectangulo
        area = self.__altura * self.__base
        return area
    
    def calculo_perimetro(self): #calculo del perimetro del rectangulo
        perimetro = self.__altura * 2 + self.__base * 2
        return perimetro
    
    #metodo para obtener en texto todos los datos y operaciones relacionadas al objeto
    def get_valores(self):
        return (f"Los valores ingresados son:\nBase: {self.__base}\nAltura: {self.__altura}\n Perimetro = {self.calculo_perimetro()}\nÁrea = {self.calculo_area()}")


#Ejemplo de utilizacion
base_ingresada = input("Ingrese la base del rectangulo: ") 
altura_ingresada = input("Ingrese la altura del rectangulo: ")
rectangulo1 = Rectangulo(base_ingresada, altura_ingresada) #Define a una variable una instancia de la clase Rectangulo

print(rectangulo1.get_valores()) #Imprimimos el texto devuelto por el metodo de los valores