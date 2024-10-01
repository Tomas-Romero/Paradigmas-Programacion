import random

#Creacion de la clase vehiculo anteriormente pero esta vez en python
class Vehiculo:
    def __init__(self, marca, modelo, año, color, precio_lavado, tiempo_lavado):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.precio_lavado = precio_lavado
        self.tiempo_lavado = tiempo_lavado
    
    def mostrar_info(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, "
                f"Color: {self.color}, Precio de lavado: ${self.precio_lavado}, "
                f"Tiempo de lavado: {self.tiempo_lavado} minutos")

#se crean las distintas clases hijas
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, color, puertas):
        super().__init__(marca, modelo, año, color, precio_lavado=20, tiempo_lavado=30)
        self.puertas = puertas

    def mostrar_info(self):
        info_basica = super().mostrar_info() #se utiliza el metodo de la clase padre para todos los atributos "heredados"
        return f"{info_basica}, Puertas: {self.puertas}"

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, año, color, capacidad_carga):
        super().__init__(marca, modelo, año, color, precio_lavado=30, tiempo_lavado=40)
        self.capacidad_carga = capacidad_carga
    
    def mostrar_info(self):
        return (super().mostrar_info() + f", Capacidad de carga: {self.capacidad_carga} kg")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, color, cilindrada):
        super().__init__(marca, modelo, año, color, precio_lavado=10, tiempo_lavado=20)
        self.cilindrada = cilindrada
    def mostrar_info(self):
        return (super().mostrar_info() + f", Cilindrada: {self.cilindrada} cc")

class Omnibus(Vehiculo):
    def __init__(self, marca, modelo, año, color, capacidad_pasajeros):
        super().__init__(marca, modelo, año, color, precio_lavado=50, tiempo_lavado=60)
        self.capacidad_pasajeros = capacidad_pasajeros
    
    def mostrar_info(self):
        return (super().mostrar_info() + f", Capacidad de pasajeros: {self.capacidad_pasajeros}")


"Ejemplos de uso"
auto = Auto("Toyota", "Corolla", 2020, "Rojo", 4)
camioneta = Camioneta("Ford", "Ranger", 2018, "Negro", 1000)
moto = Moto("Honda", "CBR600RR", 2019, "Azul", 600)
omnibus = Omnibus("Mercedes-Benz", "Sprinter", 2022, "Blanco", 30)

# Lista de vehículos en el lavadero
vehiculos_en_lavadero = [auto, camioneta, moto, omnibus]

# Mostrar información de todos los vehículos en el lavadero
for vehiculo in vehiculos_en_lavadero:
    print(vehiculo.mostrar_info())