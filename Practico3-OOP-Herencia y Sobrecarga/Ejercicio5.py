class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

    def __lt__(self, other):
        return self.edad < other.edad
    
    def __le__(self, other):
        return self.edad <= other.edad
    
    def __gt__(self, other):
        return self.edad > other.edad
    
    def __ge__(self, other):
        return self.edad >= other.edad

def verificar_edad(persona1, persona2):
    if persona1 > persona2 and (persona1.edad - persona2.edad) >= 10:
        return True
    elif persona2 > persona1 and (persona2.edad - persona1.edad) >= 10:
        return True
    else:
        return False

def main():
    print("Ingrese los datos de los invitados (nombre y edad):")
    
    while True:
        try:
            nombre1 = input("Nombre de la primera persona: ")
            edad1 = int(input("Edad de la primera persona: "))
            nombre2 = input("Nombre de la segunda persona: ")
            edad2 = int(input("Edad de la segunda persona: "))

            persona1 = Persona(nombre1, edad1)
            persona2 = Persona(nombre2, edad2)

            if verificar_edad(persona1, persona2):
                print(f"{persona1.nombre} y {persona2.nombre} están habilitados para ingresar a la fiesta.")
            else:
                print(f"{persona1.nombre} y {persona2.nombre} NO están habilitados para ingresar a la fiesta.")

        except ValueError:
            print("Por favor, ingrese una edad válida.")

        continuar = input("¿Desea ingresar otro par de personas? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
