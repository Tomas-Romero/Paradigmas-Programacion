class Persona:
    def __init__(self, nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.edad = edad
        self.dni = dni
        self.celular = celular
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_tipo_usuario(self):
        return "persona"

class Cliente(Persona):
    def __init__(self, nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento, frecuente, ultima_visita):
        super().__init__(nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento)
        self.frecuente = frecuente
        self.ultima_visita = ultima_visita

    def obtener_tipo_usuario(self):
        return "cliente"

class Empleado(Persona):
    def __init__(self, nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento, legajo, seccion, disponible_extras, antiguedad, nivel_acceso):
        super().__init__(nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento)
        self.legajo = legajo
        self.seccion = seccion
        self.disponible_extras = disponible_extras
        self.antiguedad = antiguedad
        self.nivel_acceso = nivel_acceso

    def obtener_tipo_usuario(self):
        return "empleado"

class Administrador(Empleado):
    def __init__(self, nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento, legajo, seccion, disponible_extras, antiguedad):
        super().__init__(nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento, legajo, seccion, disponible_extras, antiguedad, "admin")

class Gerente(Empleado):
    def __init__(self, nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento, legajo, seccion, disponible_extras, antiguedad):
        super().__init__(nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento, legajo, seccion, disponible_extras, antiguedad, "gerente")

class Vendedor(Empleado):
    def __init__(self, nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento, legajo, seccion, disponible_extras, antiguedad):
        super().__init__(nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento, legajo, seccion, disponible_extras, antiguedad, "vendedor")

class Tecnico(Empleado):
    def __init__(self, nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento, legajo, seccion, disponible_extras, antiguedad):
        super().__init__(nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento, legajo, seccion, disponible_extras, antiguedad, "tecnico")


def guardar_usuarios(usuarios, filename):
    with open(f"{filename}", 'w') as file:
        for usuario in usuarios:
            tipo = usuario.obtener_tipo_usuario()
            if tipo == "cliente":
                file.write(f"{usuario.apellido},{usuario.nombre},{usuario.direccion},{usuario.edad},{usuario.dni},{usuario.celular},{usuario.email},{usuario.fecha_nacimiento},{usuario.frecuente},{usuario.ultima_visita}\n")
            elif tipo == "empleado":
                file.write(f"{usuario.apellido},{usuario.nombre},{usuario.direccion},{usuario.edad},{usuario.dni},{usuario.celular},{usuario.email},{usuario.fecha_nacimiento},{usuario.legajo},{usuario.seccion},{usuario.disponible_extras},{usuario.antiguedad},{usuario.nivel_acceso}\n")

def agregar_cliente(usuarios):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Dirección: ")
    edad = int(input("Edad: "))
    dni = input("DNI: ")
    celular = input("Celular: ")
    email = input("Email: ")
    fecha_nacimiento = input("Fecha de Nacimiento (AAAA-MM-DD): ")
    frecuente = input("¿Es cliente frecuente? (Sí/No): ").lower() == 'sí'
    ultima_visita = input("Última fecha de visita (AAAA-MM-DD): ")
    cliente = Cliente(nombre, apellido, direccion, edad, dni, celular, email, fecha_nacimiento, frecuente, ultima_visita)
    usuarios.append(cliente)
    guardar_usuarios(usuarios, "empresa.txt")
    print("Cliente agregado con éxito.")

def eliminar_persona(usuarios):
    dni = input("Ingrese el DNI de la persona a eliminar: ")
    for i in range(len(usuarios)):
        if usuarios[i].dni == dni:
            del usuarios[i]
            guardar_usuarios(usuarios, "empresa.txt")
            print("Persona eliminada con éxito.")
            return
    print("Persona no encontrada.")

def mostrar_menu(usuario, usuarios):
    tipo_usuario = usuario.obtener_tipo_usuario()
    if tipo_usuario == "empleado":
        if usuario.nivel_acceso == 'admin':
            while True:
                print("1. Ver empleados")
                print("2. Modificar datos de empleados")
                print("3. Eliminar persona")
                print("4. Agregar cliente")
                print("5. Salir")
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    for u in usuarios:
                        if u.obtener_tipo_usuario() == "empleado":
                            print(f"{u.apellido}, {u.nombre} - Legajo: {u.legajo}")
                elif opcion == 2:
                    # Código para modificar datos de empleados
                    pass
                elif opcion == 3:
                    eliminar_persona(usuarios)
                elif opcion == 4:
                    agregar_cliente(usuarios)
                elif opcion == 5:
                    break

        elif usuario.nivel_acceso == 'gerente':
            while True:
                print("1. Ver empleados")
                print("2. Modificar datos de empleados")
                print("3. Salir")
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    for u in usuarios:
                        if u.obtener_tipo_usuario() == "empleado":
                            print(f"{u.apellido}, {u.nombre} - Legajo: {u.legajo}")
                elif opcion == 2:
                    # Código para modificar datos de empleados
                    pass
                elif opcion == 3:
                    break

        elif usuario.nivel_acceso == 'vendedor':
            while True:
                print("1. Agregar cliente")
                print("2. Salir")
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    agregar_cliente(usuarios)
                elif opcion == 2:
                    break

        elif usuario.nivel_acceso == 'tecnico':
            while True:
                print("1. Ver mis datos")
                print("2. Salir")
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    print(f"Datos de {usuario.nombre} {usuario.apellido}:")
                    print(f"Dirección: {usuario.direccion}")
                    print(f"Edad: {usuario.edad}")
                    print(f"DNI: {usuario.dni}")
                    print(f"Celular: {usuario.celular}")
                    print(f"Email: {usuario.email}")
                    print(f"Fecha de Nacimiento: {usuario.fecha_nacimiento}")
                    print(f"Legajo: {usuario.legajo}")
                    print(f"Sección: {usuario.seccion}")
                    print(f"Disponible para extras: {usuario.disponible_extras}")
                    print(f"Antigüedad: {usuario.antiguedad}")
                elif opcion == 2:
                    break

def login(usuarios):
    dni = input("Ingrese su DNI: ")
    for usuario in usuarios:
        if usuario.dni == dni:
            return usuario
    print("Usuario no encontrado.")
    return None

def main():
    usuarios = [
        Administrador("Juan", "Pérez", "Calle Falsa 123", 45, "12345678", "123456789", "juan@example.com", "1975-05-20", "A001", "Administración", True, 20),
        Gerente("Ana", "González", "Av. Siempre Viva 742", 39, "87654321", "987654321", "ana@example.com", "1980-09-15", "G001", "Ventas", True, 15),
        Vendedor("Carlos", "Lopez", "Calle de la Palma 321", 29, "45678912", "456789123", "carlos@example.com", "1991-02-10", "V001", "Ventas", False, 5),
        Tecnico("Marta", "Gomez", "Calle del Sol 456", 25, "78945612", "789456123", "marta@example.com", "1995-07-25", "T001", "Soporte Técnico", False, 2),
        Cliente("Pedro", "Fernandez", "Calle Luna 789", 30, "11223344", "111222333", "pedro@example.com", "1990-11-11", True, "2024-08-01")
    ]
    guardar_usuarios(usuarios, "empresa.txt")
    
    while True:
        usuario = login(usuarios)
        if usuario:
            mostrar_menu(usuario, usuarios)
        else:
            print("¿Desea intentar nuevamente? (Sí/No)")
            if input().lower() != 'sí':
                break

if __name__ == "__main__":
    main()
