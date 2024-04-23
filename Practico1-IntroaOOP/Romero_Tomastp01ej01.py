#Creacion de la clase de rectangulo
class Rectangulo():
    def __init__(self, base=1, altura=1):
        self.__base = base
        self.__altura = altura
    #creacion del metodo get
    def get_base(self):
        return self.__base
    def get_altura(self):
        return self.__altura
    #Creacion de los metodos set
    def set_base(self, nueva_base):
        self.__base = nueva_base
    def set_altura(self, nueva_altura):
        self.__altura = nueva_altura
    #Creacion de los metodos
    def calculo_area(self):
        area = self.__altura * self.__base
        return area
    def calculo_perimetro(self):
        perimetro = self.__altura * 2 + self.__base * 2
        return perimetro
    def print_valores(self):
        print(f"Los valores ingresados son:\nBase: {self.__base}\nAltura: {self.__altura}\n Perimetro = {self.calculo_perimetro()}\nÁrea = {self.calculo_area()}")
#Ejemplo de utilizacion
base_ingresada = input("Ingrese la base del rectangulo: ") 
altura_ingresada = input("Ingrese la altura del rectangulo: ")
rectangulo1 = Rectangulo(base_ingresada, altura_ingresada)
rectangulo1.print_valores()