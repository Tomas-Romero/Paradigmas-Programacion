class Complejo:
    def __init__(self, real=0, imaginario=0):
        self.real = real
        self.imaginario = imaginario

    def __repr__(self):
        return f"Complejo({self.real} + {self.imaginario}i)"
    
    def __add__(self, other):
        return Complejo(self.real + other.real, self.imaginario + other.imaginario)
    
    def __sub__(self, other):
        return Complejo(self.real - other.real, self.imaginario - other.imaginario)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginario * other.imaginario
        imaginario_part = self.real * other.imaginario + self.imaginario * other.real
        return Complejo(real_part, imaginario_part)
    
    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginario**2
        real_part = (self.real * other.real + self.imaginario * other.imaginario) / denominator
        imaginario_part = (self.imaginario * other.real - self.real * other.imaginario) / denominator
        return Complejo(real_part, imaginario_part)
    
    def __eq__(self, other):
        return self.real == other.real and self.imaginario == other.imaginario

def main():
    c1 = Complejo(2, 3)  # 2 + 3i
    c2 = Complejo(1, 4)  # 1 + 4i
    
    print("Número complejo 1:", c1)
    print("Número complejo 2:", c2)
    
    # Suma
    suma = c1 + c2
    print(f"Suma: {c1} + {c2} = {suma}")
    
    # Resta
    resta = c1 - c2
    print(f"Resta: {c1} - {c2} = {resta}")
    
    # Multiplicación
    multiplicacion = c1 * c2
    print(f"Multiplicación: {c1} * {c2} = {multiplicacion}")
    
    # División
    division = c1 / c2
    print(f"División: {c1} / {c2} = {division}")
    
    # Comparación
    c3 = Complejo(2, 3)
    print(f"¿Son {c1} y {c3} iguales? {'Sí' if c1 == c3 else 'No'}")

if __name__ == "__main__":
    main()
