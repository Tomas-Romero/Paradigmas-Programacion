#Estudiante: Tomas Agustin Romero | Paradigmas de la Programacion 2024

import math
import random


#Creacion de la clase de Mazo de cartas de poker con 52 cartas
class MazoCartas: 
    def __init__(self):
        self.__mazo = []     
    
    #Debido a que el atributo es privado, creamos un metodo para obtenerlo
    def get_mazo(self):
        return self.__mazo
    
    #El mazo al ser una lista de objetos no se puede imprimir directamente como una lista comun, por lo que creamos un metodo para verlo mas bonito
    def mostrar_mazo(self):
        texto = f"Cantidad de Cartas: '{len(self.__mazo)}'"
        for carta in self.__mazo:
            texto += f"{carta.mostrarCarta()}\n"
        return texto
    #Creacion de los metodos
    def crearMazo(self):
        cartas = []
        palos_validos = ["Corazon", "Trebol", "Diamante", "Pica"]
        valores_validos = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        for palo in palos_validos:
            for valor in valores_validos:
                carta = Carta(palo, valor)
                cartas.append(carta)
        self.__mazo = cartas
        return self
    
    def repartir(self): #Se reparte la ultima carta que esta en el mazo
        carta = self.__mazo.pop()
        return carta.mostrarCarta()
    
    def barajar(self):
        mazo_barajado = []
        if len(self.__mazo) == 52:
            while len(self.__mazo) != 0: #Se van eligiendo cartas aleatorias del mazo para ir barajandolas utilizando random para "apilarlas" en un nuevo mazo barajado
                mazo_barajado.append(self.__mazo.pop(random.randrange(len(self.__mazo))))
            self.__mazo = mazo_barajado
            return self.__mazo
        else:
            self.crearMazo()
            print("Faltaban cartas en el mazo, se han devueto todas las cartas al mazo")
            self.barajar()

    
#Creacion de la clase de Cartas que tiene que tener una pinta y el valor
#Palos validos: [Corazones, Trebol,Diamante, Picas]
#Valores validos: [A, 2,3,4,5,6,7,8,9,10,J,Q,K]
class Carta:
    def __init__(self, palo, valor):
        palos_validos = ["Corazon", "Trebol", "Diamante", "Pica"]
        valores_validos = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        if palo in palos_validos:
            self.__palo = palo
        else:
            print("No es un valor valido para las cartas, Debe ingresar: 'Corazon', 'Trebol', 'Diamante', 'Pica'")
        if valor in valores_validos:
            self.__valor = valor
        else:
            print("No es un valor valido para las cartas, Debe ingresar: [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]")
    
    #Creacion de los metodos
    def mostrarCarta(self):
        texto = f"Palo: {self.__palo}\nValor: {self.__valor}"
        return texto
#Ejemplo de utilizacion para instanciar mazo
# mazo1 = MazoCartas()     
# mazo1.crearMazo()   
# print(mazo1.mostrar_mazo())
# print(mazo1.repartir())
# print(mazo1.mostrar_mazo())

#Ejemplo de utilizacion para barajar
# mazo2 = MazoCartas()
# mazo2.crearMazo()
# print(mazo2.mostrar_mazo())
# mazo2.barajar()
# print(mazo2.mostrar_mazo())
# #Utilizacion si no esta el mazo completo con las 52 cartas
# mazo3 = MazoCartas()
# mazo3.crearMazo()
# print(mazo3.mostrar_mazo())
# mazo2.repartir()
# mazo2.barajar()
# print(mazo2.mostrar_mazo())
