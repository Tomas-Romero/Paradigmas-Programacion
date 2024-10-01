class Recorrido:
    def __init__(self, origen, destino, fecha, hora):
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha
        self.__hora = hora
        self.pasajes = self.crear_pasajes()
        self.disponible = True

    def crear_pasajes(self):
        pasajes = []
        for i in range(1, 21):
            pasajes.append(Pasaje(None, None, "Alta", i, 100.0))
            pasajes.append(Pasaje(None, None, "Baja", i, 80.0))
        return pasajes

    def getOrigen(self):
        return self.__origen

    def getDestino(self):
        return self.__destino

    def getFecha(self):
        return self.__fecha

    def getHora(self):
        return self.__hora

    def getDisponible(self):
        return any(p.nombre_pasajero is None for p in self.pasajes)

    def mostrarInfo(self):
        return f"Origen: {self.__origen}, Destino: {self.__destino}, Fecha: {self.__fecha}, Hora: {self.__hora}, Pasajes disponibles: {len([p for p in self.pasajes if p.nombre_pasajero is None])}"

    def reservar_pasaje(self, nombre_pasajero, apellido_pasajero, planta, numero_asiento):
        for pasaje in self.pasajes:
            if pasaje.planta == planta and pasaje.numero_asiento == numero_asiento:
                if pasaje.nombre_pasajero is None:
                    pasaje.nombre_pasajero = nombre_pasajero
                    pasaje.apellido_pasajero = apellido_pasajero
                    print(f"Pasaje reservado para {nombre_pasajero} {apellido_pasajero}.")
                    return True
                else:
                    print("El asiento ya está reservado.")
                    return False
        print("Asiento no encontrado.")
        return False

class Pasaje:
    def __init__(self, nombre_pasajero, apellido_pasajero, planta, numero_asiento, precio):
        self.nombre_pasajero = nombre_pasajero
        self.apellido_pasajero = apellido_pasajero
        self.planta = planta
        self.numero_asiento = numero_asiento
        self.precio = precio

    def __str__(self):
        return (f"Pasaje: {self.nombre_pasajero} {self.apellido_pasajero}, "
                f"Asiento: Planta {self.planta}, Número: {self.numero_asiento}, Precio: ${self.precio}")

class Empresa:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.recorridos = []

    def getNombre(self):
        return self.__nombre

    def agregar_recorrido(self, recorrido):
        self.recorridos.append(recorrido)

    def quitar_recorrido(self, recorrido_eliminar):
        self.recorridos.remove(recorrido_eliminar)

    def __str__(self):
        return f"Empresa: {self.__nombre}, Recorridos: {len(self.recorridos)}"

class Sistema:
    def __init__(self):
        self.empresas = []

    def agregar_empresa(self, empresa):
        self.empresas.append(empresa)

    def mostrar_empresas(self):
        for empresa in self.empresas:
            print(empresa)

    def seleccionar_empresa(self, nombre):
        for empresa in self.empresas:
            if empresa.getNombre() == nombre:
                return empresa
        return None

    def buscar_recorridos(self, empresa, origen, destino):
        resultados = []
        for recorrido in empresa.recorridos:
            if recorrido.getOrigen() == origen and recorrido.getDestino() == destino:
                resultados.append(recorrido)
        return resultados

    def mostrar_menu(self):
        while True:
            print("\nMenú del Sistema de Reservas")
            print("1. Mostrar empresas")
            print("2. Mostrar recorridos de una empresa")
            print("3. Reservar pasaje")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.mostrar_empresas()

            elif opcion == "2":
                nombre_empresa = input("Ingrese el nombre de la empresa: ")
                empresa = self.seleccionar_empresa(nombre_empresa)
                if empresa:
                    print(f"\nRecorridos de {empresa.getNombre()}:")
                    for recorrido in empresa.recorridos:
                        print(recorrido.mostrarInfo())
                else:
                    print("Empresa no encontrada.")

            elif opcion == "3":
                nombre_empresa = input("Ingrese el nombre de la empresa: ")
                empresa = self.seleccionar_empresa(nombre_empresa)
                if empresa:
                    origen = input("Ingrese el origen: ")
                    destino = input("Ingrese el destino: ")
                    recorridos = self.buscar_recorridos(empresa, origen, destino)
                    if recorridos:
                        print("Recorridos disponibles:")
                        for idx, recorrido in enumerate(recorridos, 1):
                            print(f"{idx}. {recorrido.mostrarInfo()}")
                        seleccion = int(input("Seleccione el número del recorrido: ")) - 1
                        if 0 <= seleccion < len(recorridos):
                            recorrido_seleccionado = recorridos[seleccion]
                            nombre_pasajero = input("Nombre del pasajero: ")
                            apellido_pasajero = input("Apellido del pasajero: ")
                            planta = input("Planta (Alta/Baja): ")
                            numero_asiento = int(input("Número de asiento: "))
                            recorrido_seleccionado.reservar_pasaje(nombre_pasajero, apellido_pasajero, planta, numero_asiento)
                        else:
                            print("Selección inválida.")
                    else:
                        print("No hay recorridos disponibles.")
                else:
                    print("Empresa no encontrada.")

            elif opcion == "4":
                print("Saliendo...")
                break

            else:
                print("Opción inválida. Intente de nuevo.")

# Ejemplo para usar
andesmar = Empresa("Andesmar")
buttini = Empresa("Buttini")
recorrido1_andesmar = Recorrido("Mendoza", "Buenos Aires", "2024-08-20", "08:00")
recorrido2_andesmar = Recorrido("Mendoza", "bariloche", "2024-08-21", "09:00")
recorrido3_andesmar = Recorrido("Mendoza", "Msr del plata", "2024-08-22", "10:00")

recorrido1_buttini = Recorrido("Mendoza", "Buenos Aires", "2024-08-20", "08:30")
recorrido2_buttini = Recorrido("Mendoza", "Cordoba", "2024-08-21", "09:30")
recorrido3_buttini = Recorrido("Mendoza", "Alvear", "2024-08-22", "10:30")

# se agregar a cada empresa su recorrido
andesmar.agregar_recorrido(recorrido1_andesmar)
andesmar.agregar_recorrido(recorrido2_andesmar)
andesmar.agregar_recorrido(recorrido3_andesmar)

buttini.agregar_recorrido(recorrido1_buttini)
buttini.agregar_recorrido(recorrido2_buttini)
buttini.agregar_recorrido(recorrido3_buttini)

# se crea sel sistema y agregamos las empresas
sistema = Sistema()
sistema.agregar_empresa(andesmar)
sistema.agregar_empresa(buttini)

# se iniscia el menu
sistema.mostrar_menu()
