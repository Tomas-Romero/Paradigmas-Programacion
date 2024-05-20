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
    def factorial(self, numero_ingresado):
        total_factorial = 1
        self.__numero = int(numero_ingresado)
        for i in range(numero_ingresado):
            total_factorial += total_factorial * i
        return total_factorial
    
    def suma(self, n):
        if n <= 0:
            return 0
        else:
            return (n * (n + 1)) // 2
    
    def es_primo(self, numero):
        if numero <= 1:
            return f"{numero} no es un número primo."
        elif numero <= 3:
            return f"{numero} es un número primo."
        elif numero % 2 == 0 or numero % 3 == 0:
            return f"{numero} no es un número primo."
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return f"{numero} no es un número primo."
            i += 6
        return f"{numero} es un número primo."
    
    def tabla_multiplicacion(self, numero):
        tabla = f"La tabla de multiplicación de '{numero}' es\n"
        for i in range(1, 11):
            tabla += f"|| {numero} x {i} = {numero*i} ||\n"
        return tabla
    
    def lista_divisores(self, numero):
        lista = []
        for i in range(1, numero +1):
            if numero % i == 0:
                lista.append(i) 
        return lista
    
#Ejemplo de utilizacion
numero1 = Computo()
print(numero1.factorial(4))
print(numero1.factorial(7))
print(numero1.factorial(15))

print(numero1.suma(4))
print(numero1.suma(7))
print(numero1.suma(15))

print(numero1.es_primo(4))
print(numero1.es_primo(7))
print(numero1.es_primo(15))
print(numero1.es_primo(11))

print(numero1.tabla_multiplicacion(4))
print(numero1.tabla_multiplicacion(7))
print(numero1.tabla_multiplicacion(9))
print(numero1.tabla_multiplicacion(14))

print(numero1.lista_divisores(40))
print(numero1.lista_divisores(70))
print(numero1.lista_divisores(95))
print(numero1.lista_divisores(150))
print(numero1.lista_divisores(110))