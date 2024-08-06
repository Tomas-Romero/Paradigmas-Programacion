class Binario:
    def __init__(self, valor):
        # Aseguramos que el valor se almacena como una cadena de dígitos binarios
        self.valor = valor

    def __repr__(self):
        return f"Binario({self.valor})"
    
    def __int__(self):
        # Convertir el valor binario a decimal para operaciones
        return int(self.valor, 2)

    def __add__(self, other):
        resultado_decimal = int(self) + int(other)
        return Binario(bin(resultado_decimal)[2:])
    
    def __sub__(self, other):
        resultado_decimal = int(self) - int(other)
        return Binario(bin(resultado_decimal)[2:])
    
    def __mul__(self, other):
        resultado_decimal = int(self) * int(other)
        return Binario(bin(resultado_decimal)[2:])
    
    def __truediv__(self, other):
        resultado_decimal = int(self) // int(other)
        return Binario(bin(resultado_decimal)[2:])
    
    def __eq__(self, other):
        return self.valor == other.valor

def main():
    b1 = Binario("110")  # 6 en decimal
    b2 = Binario("101")  # 5 en decimal
    
    print("Número binario 1:", b1)
    print("Número binario 2:", b2)
    
    # Suma
    suma = b1 + b2
    print(f"Suma: {b1} + {b2} = {suma}")
    
    # Resta
    resta = b1 - b2
    print(f"Resta: {b1} - {b2} = {resta}")
    
    # Multiplicación
    multiplicacion = b1 * b2
    print(f"Multiplicación: {b1} * {b2} = {multiplicacion}")
    
    # División
    division = b1 / b2
    print(f"División: {b1} / {b2} = {division}")
    
    # Comparación
    b3 = Binario("110")
    print(f"¿Son {b1} y {b3} iguales? {'Sí' if b1 == b3 else 'No'}")

if __name__ == "__main__":
    main()
