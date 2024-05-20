#Estudiante: Tomas Agustin Romero | Paradigmas de la Programacion 2024

import math


#Creacion de la clase de la Maquina Calculadora
class Facturador:
    def __init__(self, fechafacturacion, nombrecliente, detalle, preciounitario, cantidad):
        self.__fechafacturacion = fechafacturacion
        self.__nombrecliente = nombrecliente
        self.__detalle = detalle
        self.__preciounitario = preciounitario
        self.__cantidad = cantidad
        self.__preciototal = preciounitario * cantidad

    #creacion del metodo get
    def get_fechafacturacion(self):
        return self.__fechafacturacion
    
    def get_nombrecliente(self):
        return self.__nombrecliente
    
    def get_detalle(self):
        return self.__detalle
    
    def get_preciounitario(self):
        return self.__preciounitario
    
    def get_cantidad(self):
        return self.__cantidad
    
    def get_preciototal(self):
        return self.__preciototal
                    
    #Creacion de los metodos

    def facturarmercaderia(self,fechafacturacion, nombrecliente, detalle, preciounitario, cantidad):
        self.__fechafacturacion = fechafacturacion
        self.__nombrecliente = nombrecliente
        self.__detalle = detalle
        self.__preciounitario = preciounitario
        self.__cantidad = cantidad
        self.__preciototal = preciounitario * cantidad   
        return "Se ha facturado correctamente el producto."
    
    def mostrarFactura(self):
        factura = f"""____________________________________\nLa factura del producto solicitado:\nFecha de Facturacion: {self.__fechafacturacion}\nCliente: {self.__nombrecliente}\nDetalle: {self.__detalle}\nPrecio Unitario: {self.__preciounitario}\nCantidad: {self.__cantidad}\nPrecio Total: {self.__preciototal}\n________________________"""
        return factura
    
#Ejemplo de utilizacion instaciando los datos desde el codigo
producto1 = Facturador("20/5", "Tomas Romero", "Galletas de Chocolate", 500, 45)

print(producto1.mostrarFactura())


#Ejemplo de utilizacion pidiendo los datos por prompt
fecha = input("Ingrese la fecha: ")
nombre = input("Ingrese nombre de cliente: ")
detalle = input("Ingrese el detalle del producto: ")
precio_unitario = float(input("Ingrese el precio unitario en numeros: "))
cantidad = float(input("Ingrese la cantidad del producto en numeros: "))
producto2 = Facturador(fecha, nombre, detalle, precio_unitario, cantidad)

print(producto2.mostrarFactura())
