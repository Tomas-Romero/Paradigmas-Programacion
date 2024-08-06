# Clase base Animal
class Animal:
    def __init__(self, raza, nombre, color, edad, estado_salud, genero):
        self.raza = raza
        self.nombre = nombre
        self.color = color
        self.edad = edad
        self.estado_salud = estado_salud
        self.genero = genero
        self.adoptado = False

    def adoptar(self):
        self.adoptado = True

# Clases derivadas de Animal

class Perro(Animal):
    def __init__(self, raza, nombre, color, edad, estado_salud, genero, agresivo, desparacitado):
        super().__init__(raza, nombre, color, edad, estado_salud, genero)
        self.agresivo = agresivo
        self.desparacitado = desparacitado

class Gato(Animal):
    def __init__(self, raza, nombre, color, edad, estado_salud, genero, marca_comida, operado):
        super().__init__(raza, nombre, color, edad, estado_salud, genero)
        self.marca_comida = marca_comida
        self.operado = operado

class Conejo(Animal):
    def __init__(self, raza, nombre, color, edad, estado_salud, genero, tamaño, dieta_especial):
        super().__init__(raza, nombre, color, edad, estado_salud, genero)
        self.tamaño = tamaño  # Puede ser "pequeño", "mediano", "grande"
        self.dieta_especial = dieta_especial  # True o False

class Canario(Animal):
    def __init__(self, raza, nombre, color, edad, estado_salud, genero, tipo_plumaje, canta):
        super().__init__(raza, nombre, color, edad, estado_salud, genero)
        self.tipo_plumaje = tipo_plumaje  # Puede ser "fuerte", "débil"
        self.canta = canta  # True o False

class Tortuga(Animal):
    def __init__(self, raza, nombre, color, edad, estado_salud, genero, especie, habitat):
        super().__init__(raza, nombre, color, edad, estado_salud, genero)
        self.especie = especie
        self.habitat = habitat  # Puede ser "acuático", "terrestre"

class Pez(Animal):
    def __init__(self, raza, nombre, color, edad, estado_salud, genero, tipo_agua, tamaño_pecera):
        super().__init__(raza, nombre, color, edad, estado_salud, genero)
        self.tipo_agua = tipo_agua  # Puede ser "dulce", "salada"
        self.tamaño_pecera = tamaño_pecera  # Litros recomendados para la pecera

# Ejemplo de uso en el programa principal

# Crear instancias de animales
conejo1 = Conejo("Conejo Holandés", "Bunny", "Blanco", 1, "sano", "Macho", tamaño="pequeño", dieta_especial=False)
conejo2 = Conejo("Conejo Rex", "Fluffy", "Gris", 2, "débil", "Hembra", tamaño="mediano", dieta_especial=True)
perro1 = Perro("Golden Retriever", "Max", "Dorado", 3, "sano", "Macho", agresivo=False, desparacitado=True)
perro2 = Perro("Bulldog", "Rocky", "Blanco", 4, "cojo", "Macho", agresivo=False, desparacitado=False)
perro3 = Perro("Pastor Alemán", "Rex", "Negro", 5, "enfermo crónico", "Macho", agresivo=True, desparacitado=True)
gato = Gato("Siames", "Whiskers", "Crema", 2, "sano", "Hembra", marca_comida="Whiskas", operado=True)
canario = Canario("Canario", "Tweety", "Amarillo", 1, "sano", "Macho", tipo_plumaje="fuerte", canta=True)
tortuga = Tortuga("Tortuga Marina", "Shelly", "Verde", 10, "sano", "Hembra", especie="Marina", habitat="acuático")
pez1 = Pez("Goldfish", "Nemo", "Naranja", 1, "sano", "Macho", tipo_agua="dulce", tamaño_pecera=20)
pez2 = Pez("Betta", "Blue", "Azul", 2, "aleta herida", "Macho", tipo_agua="dulce", tamaño_pecera=5)
pez3 = Pez("Cíclido", "Rainbow", "Multicolor", 1, "sano", "Hembra", tipo_agua="dulce", tamaño_pecera=50)
pez4 = Pez("Tetra", "Flash", "Rojo", 1, "sano", "Macho", tipo_agua="dulce", tamaño_pecera=10)
pez5 = Pez("Guppy", "Sparkle", "Amarillo", 1, "sano", "Hembra", tipo_agua="dulce", tamaño_pecera=5)

# Lista de animales en el shelter
animales_guardia = [conejo1, conejo2, perro1, perro2, perro3, gato, canario, tortuga, pez1, pez2, pez3, pez4, pez5]

# Proceso de adopción: Adoptar un conejo, un gato y un perro que no sea agresivo
conejo1.adoptar()
gato.adoptar()

# Encontrar un perro no agresivo para adoptar
for perro in [perro1, perro2, perro3]:
    if not perro.agresivo:
        perro.adoptar()
        break

# Mostrar estado de adopción de los animales
for animal in animales_guardia:
    print(f"{animal.nombre} adoptado: {animal.adoptado}")
