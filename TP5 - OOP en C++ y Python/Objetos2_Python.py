import random

#Ejercicio 7
print("EJERCICIO 7")

class Estudiante():
    def __init__(self, legajo, nombre, carrera, institucion, mail, dni):
        self.__legajo = int(legajo)
        self.__nombre = nombre
        self.__carrera = carrera
        self.__institucion = institucion
        self.__mail = mail
        self.__dni = int(dni)
        self.__materias = []
        self.__notas = []
        self.__finales_aprobados = {}
    
    
    #Definimos los metodos getters
    def get_legajo(self):
        return self.__legajo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_carrera(self):
        return self.__carrera
    
    def get_institucion(self):
        return self.__institucion
    
    def get_mail(self):
        return self.__mail
    
    def get_dni(self):
        return self.__dni
    
    def get_materias(self):
        return self.__materias
    
    def get_notas(self):
        return self.__notas
    
    def get_finales_aprobados(self):
        return self.__finales_aprobados
    
    
    #Definimos los metodos Setters
    def set_legajo(self, nuevo_legajo):
        self.__legajo = int(nuevo_legajo)
        
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    def set_carrera(self, nuevo_carrera):
        self.__carrera = nuevo_carrera
        
    def set_institucion(self, nuevo_institucion):
        self.__institucion = nuevo_institucion
        
    def set_mail(self, nuevo_mail):
        self.__mail = nuevo_mail
        
    def set_dni(self, nuevo_dni):
        self.__dni = int(nuevo_dni)
    
    def set_materias(self, nuevo_materias):
        self.__materias = nuevo_materias
    
    def set_notas(self, nuevo_notas):
        self.__notas = nuevo_notas
        
    def set_finales_aprobados(self, nuevo_finales_aprobados):
        self.__finales_aprobados = nuevo_finales_aprobados
        
        
    #Creamos los métodos
    
    def agregar_materia(self, materia_agregar):
        self.__materias.append(materia_agregar)
        print(f"Se ha agregado la materia '{materia_agregar}' al alumno")
        
    def eliminar_materia(self, materia_eliminar):
        self.__materias.remove(materia_eliminar)
        print(f"Se ha eliminado la materia '{materia_eliminar}' al alumno")
    
    def agregar_nota(self, nota_agregar):
        self.__notas.append(nota_agregar)
        print(f"Se ha agregado la nota '{nota_agregar}' al alumno")
        
    def eliminar_nota(self, nota_eliminar):
        self.__notas.remove(nota_eliminar)
        print(f"Se ha eliminado la nota '{nota_eliminar}' al alumno")
    
    def agregar_final(self, final_agregar, nota_final):
        self.__finales_aprobados[final_agregar] = nota_final
        print(f"Se ha agregado el final '{final_agregar}' al alumno con la nota de '{nota_final}'")
    
    def obtener_promedio(self):
        promedio = sum(self.__notas) / len(self.__notas)
        return promedio
    
    def obtener_promedio_finales(self):
        suma_notas = 0
        for final, nota in self.__finales_aprobados.items():
            suma_notas += int(nota)
        promedio_finales = suma_notas / len(self.__finales_aprobados)
        return promedio_finales
    
    def obtener_informacion(self):
        texto = (f"Nombre: {self.__nombre}\nLegajo: {self.__legajo}\nCarrera: {self.__carrera}\nInstitución: {self.__institucion}\nMail: {self.__mail}\nDni: {self.__dni}\nMaterias: {self.__materias}\n")
        return(texto)
    
    
#Ejemplo de uso
#legajo, nombre, carrera, institucion, mail, dni)

# estudiante_1 = Estudiante(10289, "Tomas Romero", "Ingenieria en Sistemas", "UTN San Rafael", "Tomasromero200310@gmail.com", 44771625)
# estudiante_1.agregar_materia("Paradigmas de la Programacion")
# estudiante_1.agregar_materia("Analisis Matematico II")
# notas = [10,8,7,9,10,8,10,7,6,7,7,9,9,9,9]
# estudiante_1.set_notas(notas)

# print(estudiante_1.obtener_promedio())
# print(estudiante_1.obtener_informacion())


#Ejercicio 8
print("EJERCICIO 8") #Para utilizar el codigo descomentar toda la seccion
# lista_estudiantes = []
# cant_estudiantes = int(input("Ingrese la cantidad de estudiantes que quiere ingresar para ver al abanderado: "))
# for i in range(cant_estudiantes):
#     universidad = "UTN San Rafael"
#     nombre = input(f"Ingrese el nombre del estudiante 'N° {i+1}': ")
#     legajo = input(f"Ingrese el legajo del estudiante 'N° {i+1}': ")
#     carrera = input(f"Ingrese la carrera del estudiante 'N° {i+1}': ")
#     dni = input(f"Ingrese el dni del estudiante 'N° {i+1}': ")
#     mail = nombre + legajo + "@gmail.com"
    
#     estudiante = Estudiante(legajo, nombre, carrera, universidad, mail, dni)
#     lista_estudiantes.append(estudiante)
#     final_agregar = ""
#     while final_agregar != 'q':
#         final_agregar = input("Ingrese la materia que el alumno rindio el final, si no quiere ingresar mas materias ingrese 'q' : ")
#         if final_agregar != 'q':
#             nota_final = input("Ingrese el numero entero de la nota del final: ")
#             lista_estudiantes[i].agregar_final(final_agregar, nota_final)


#Ejemplo de obtener abanderados de 6 estudiantes
# lista_promedios = []
# for estudiante in lista_estudiantes:
#     promedio = estudiante.obtener_promedio_finales()
#     lista_promedios.append(promedio)
# abanderado = lista_estudiantes[lista_promedios.index(max(lista_promedios))]
# print(f"El abanderado es:\n{abanderado.obtener_informacion()}")


#Ejercicio 9
print("EJERCICIO 9")

#Creacion de la clase del personaje
class Personaje:
    def __init__(self, nombre, vitalidad=1, resistencia=1, almacenamiento=100, fuerza=1, velocidad=1, sigilo=1):
        self.__nombre = nombre
        self.__nivel = 1
        self.__vitalidad = vitalidad
        self.__resistencia = resistencia
        self.__hambre = 100
        self.__sed = 100
        self.__almacenamiento = almacenamiento
        self.__fuerza = fuerza
        self.__velocidad = velocidad
        self.__sigilo = sigilo
        self.__experiencia = 0
        self.__mana = 100
        self.__defensa = 10
        self.__inventario = []

    # Metodos Getters
    def get_nombre(self):
        return self.__nombre

    def get_nivel(self):
        return self.__nivel

    def get_vitalidad(self):
        if self.__vitalidad <= 0:
            print(f"'{self.__nombre}' perdio su vitalidad, esta muerto!")
        else:
            return self.__vitalidad

    def get_resistencia(self):
        return self.__resistencia

    def get_hambre(self):
        return self.__hambre

    def get_sed(self):
        return self.__sed

    def get_almacenamiento(self):
        return self.__almacenamiento

    def get_fuerza(self):
        return self.__fuerza

    def get_velocidad(self):
        return self.__velocidad

    def get_sigilo(self):
        return self.__sigilo

    def get_experiencia(self):
        return self.__experiencia

    def get_mana(self):
        return self.__mana

    def get_defensa(self):
        return self.__defensa

    def get_inventario(self):
        return self.__inventario

    # Metodos Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_nivel(self, nivel):
        self.__nivel = nivel

    def set_vitalidad(self, vitalidad):
        self.__vitalidad = vitalidad

    def set_resistencia(self, resistencia):
        self.__resistencia = resistencia

    def set_hambre(self, hambre):
        self.__hambre = hambre

    def set_sed(self, sed):
        self.__sed = sed

    def set_almacenamiento(self, almacenamiento):
        self.__almacenamiento = almacenamiento

    def set_fuerza(self, fuerza):
        self.__fuerza = fuerza

    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def set_sigilo(self, sigilo):
        self.__sigilo = sigilo

    def set_experiencia(self, experiencia):
        self.__experiencia = experiencia

    def set_mana(self, mana):
        self.__mana = mana

    def set_defensa(self, defensa):
        self.__defensa = defensa

    def set_inventario(self, inventario):
        self.__inventario = inventario

# Métodos adicionales

    def atacar(self, enemigo):
        #Reduce la vitalidad del enemigo seleccionado para le ataque
        dano = self.__fuerza - enemigo.get_defensa()
        if dano > 0:
            enemigo.set_vitalidad(enemigo.get_vitalidad() - dano)
        else:
            print(f"{enemigo.get_nombre()} bloqueó el ataque.")

    def defenderse(self):
        # Incrementa la defensa permanentemente
        self.__defensa += 5
        print(f"{self.__nombre} está defendiendo y su defensa ahora es {self.__defensa}.")

    def usar_item(self, item):
        if item in self.__inventario:
            #Utilizacion de un item que sea una pocion de vida
            if item == "pocion_vida":
                self.__vitalidad += 20
                print(f"{self.__nombre} ha usado una poción de vida y ha recuperado 20 puntos de vitalidad.")
            self.__inventario.remove(item) #Remueve el item que se utilizo previamente
        else:
            print(f"{item} no está en el inventario.")
    # subir nivel incrementa el nivel si se alcanza cierta cantidad de experiencia y sube un poco de cada estadistica
    def subir_nivel(self):
        if self.__experiencia >= 100:
            self.__nivel += 1
            self.__experiencia -= 100
            self.__vitalidad += 10
            self.__mana += 10
            self.__fuerza += 2
            self.__defensa += 2
            print(f"{self.__nombre} ha subido al nivel {self.__nivel}.")
    #Se mueve la cantidad de distancia que se le introduzca y reduce la resistencia
    def moverse(self, distancia):
        coste_resistencia = distancia / self.__velocidad
        self.__resistencia -= coste_resistencia
        if self.__resistencia < 0:
            self.__resistencia = 0
        print(f"{self.__nombre} se ha movido {distancia} unidades y su resistencia ahora es {self.__resistencia}.")

    def comer(self, comida):
        # Reduce el hambre si introduce una comida como pan
        if comida == "pan":
            self.__hambre -= 10
        elif self.__hambre < 0:
            self.__hambre = 0
        print(f"{self.__nombre} ha comido {comida} y su hambre ahora es {self.__hambre}.")

    def beber(self, bebida):
        # Reduce la sed si utilizac una bebida que sea agua
        if bebida == "agua":
            self.__sed -= 10
        if self.__sed < 0:
            self.__sed = 0
        print(f"{self.__nombre} ha bebido {bebida} y su sed ahora es {self.__sed}.")

# Ejemplo de utilización, descomentar para ver la utilizacion
# heroe = Personaje("Tominetor", 1, 100, 100, 50, 50, 10)
# enemigo = Personaje("Hombre Lobo", 1, 80, 80, 50, 50, 15)

# heroe.atacar(enemigo)
# heroe.defenderse()
# heroe.usar_item("pocion_vida")
# heroe.subir_nivel()
# heroe.moverse(10)
# heroe.comer("pan")
# heroe.beber("agua")

# print(f"Vitalidad del enemigo después del ataque: {enemigo.get_vitalidad()}")

#Ejercicio 10
print("EJERCICIO 10")

#Creacion de la clase de Texto
class Texto():
    def __init__(self, texto):
        self.__texto = str(texto)
        lista_palabras = []
        palabra = ""
        for caracter in texto:
            if caracter != " ":
                palabra += caracter
            else:
                lista_palabras.append(palabra)
                palabra = ""
        self.__lista = lista_palabras
    
    def get_texto(self): #Devuelve el texto del objeto
        return self.__texto
    
    #Creacion de los metodos de la clase
    #Metodo para contar la cantidad de palabras de la frase
    def contar_palabras(self):
        for caracter in self.__texto:
            contador_palabras = 1
            if caracter == " ":
                contador_palabras += 1
        return contador_palabras
    
    #Metodo para invertir el texto ingresado
    def invertir_texto(self):
        texto_invertido = ""
        texto = list(self.__texto)
        for letra in self.__texto:
            texto_invertido += texto.pop()
        return texto_invertido
    
    def obtener_primer_palabra(self):
        return print(f"La primer palabra de la frase es: {self.__lista[0]}")
    
    def obtener_n_palabra(self, numero):
        return print(f"La {numero}° palabra de la frase es: {self.__lista[numero - 1]}")
    
    #Metodo para ocntar la cantidad de veces del caracter pedido como argumento
    def contar_letra(self, letra):
        contador = 0
        for caracter in self.__texto:
            if caracter == letra:
                contador += 1
        return print(f"La  cantidad de veces que aparece '{letra}' en la frase es: {contador}")
    
    #Metodo para ver si la frase es palindromo o no
    def es_palindromo(self):
        texto_sin_espacio = self.__texto.replace(" ", "")
        invertido_sin_espacio = self.invertir_texto().replace(" ", "")
        if texto_sin_espacio == invertido_sin_espacio:
            return print("Es Palindromo")
        else: 
            return print("No es palindromo")
    
    #Metodo para devolver la longitud de la palabra mas larga del texto
    def longitud_palabra_mas_larga(self):
        max_longitud = 0
        for palabra in self.__lista:
            if len(palabra) > max_longitud:
                max_longitud = len(palabra)
        return max_longitud
    
    #Metodo para contar la cantidad de vocales del texto
    def contar_vocales(self):
        vocales = "aeiouAEIOU"
        contar_vocales = 0
        for caracter in self.__texto:
            if caracter in vocales:
                contar_vocales += 1
        return print(f"La cantidad de las vocales del texto es: '{contar_vocales}'")
    
    
#Ejemplo de utilizacion para la clase de Texto
# texto1 = Texto(input("Ingrese una frase: "))
# print(texto1.invertir_texto())
# texto1.es_palindromo()
# texto1.obtener_primer_palabra()
# texto1.obtener_n_palabra(2)
# texto1.contar_letra("a")
# texto1.contar_letra("s")
# texto1.contar_vocales()


#Ejercicio 11
print("EJERCICIO 11")

#Creacion de la clase Carrito de compras
class Carrito():
    def __init__(self):
        self.__items = []
    
    #Metodo getters
    def get_carrito(self):
        if self.__items:
            lista_items = {}
            for elemento in self.__items:
                lista_items[elemento.get_detalle()] = f"Cant: {elemento.get_cantidad()}; Precio Unitario: ${elemento.get_precio()}; Total: ${elemento.precio_total()}"
            return print(lista_items)
        else:
            print("No hay productos en el carrito.")
        
    #Metodo para agregar productos al carrito
    def agregar_item(self, item):
        self.__items.append(item)
        return print("Se ha agregado el producto en el carrito")
    
    #Metodo para quitar el item del carrito segun el detalle
    def quitar_item(self, nombre):
        nueva_lista = []
        for item in self.__items:
            if item.get_detalle() != nombre:
                nueva_lista.append(item)
        self.__items = nueva_lista
        
    def costo_carrito(self):
        suma_total = 0
        for elemento in self.__items:
            suma_total += elemento.precio_total()
        if suma_total >= 2500:
            envio_gratis = "Tiene envio gratis"
        else:
            envio_gratis = "No tiene envio gratis"
        texto = f"El monto total de la compra es: ${suma_total}\nEnvio Gratis? - '{envio_gratis}'"
        return texto
    
#Creacion de la clase de Producto para los items del carrito
class Producto():
    def __init__(self, detalle, precio, cantidad):
        self.__detalle = detalle
        self.__precio = precio
        self.__cantidad = cantidad
        
    #Metodo getters
    def get_detalle(self):
        return self.__detalle
    
    def get_precio(self):
        return self.__precio
    
    def get_cantidad(self):
        return self.__cantidad
    
    #Metodo para modificar la cantidad de ese producto
    def modificar_cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad
    
    #Metodo para calcular el precio total del producto y la cantidad del mismo
    def precio_total(self):
        total = self.__cantidad * self.__precio
        return total 

#Ejemplo de utilizacion de las clases de Carrito y Producto
# carrito1 = Carrito()
# producto1 = Producto("arroz", 1000, 2)
# producto2 = Producto("huevos", 200, 12)

# carrito1.agregar_item(producto1)
# carrito1.agregar_item(producto2)

# carrito1.get_carrito()
# print(carrito1.costo_carrito())

# carrito1.quitar_item("arroz")

# carrito1.get_carrito()
# print(carrito1.costo_carrito())


#Ejercicio 12
print("EJERCICIO 12")

#Creacion de la clase de Cliente
class Cliente():
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni
        self.__tarjetas = []
    
    #Metodos Getter
    def get_nombre(self):
        return self.__nombre
    
    def get_dni(self):
        return self.__dni
    
    def get_tarjetas(self):
        return self.__tarjetas

    #Metodo para agregar una tarjeta de credito
    def agregar_tarjeta(self, tarjeta):
        if len(self.__tarjetas) < 4:
            self.__tarjetas.append(tarjeta)
            print(f"Tarjeta '{tarjeta.get_nombre()}' añadida.")
        else:
            print("Se ha superado el límite de tarjetas que se pueden agregar.")
    
    #Metodo para quitar una tarjeta
    def quitar_tarjeta(self, alias_tarjeta):
        for tarjeta in self.__tarjetas:
            if tarjeta.get_alias() == alias_tarjeta:
                self.__tarjetas.remove(tarjeta)
                print(f"Se ha eliminado la tarjeta '{alias_tarjeta}'.")
                return
        print(f"No se encontró una tarjeta con el alias '{alias_tarjeta}'.")
        
    #Metodo para cobrar el pago de una sola tarjeta
    def cobrar_sola(self, monto, alias_tarjeta):
        for tarjeta in self.__tarjetas:
            if tarjeta.get_alias() == alias_tarjeta:
                tarjeta.pagar(monto)
                return
        print(f"No se encontró una tarjeta con el alias '{alias_tarjeta}'.")
        
    #Metodo para cobrar de varias tarjetas un mismo monto dividido
    def cobrar_varias(self, monto, *aliases):
        tarjetas_verificadas = [tarjeta for tarjeta in self.__tarjetas if tarjeta.get_alias() in aliases]
        if len(tarjetas_verificadas) != len(aliases):
            print("Una o más tarjetas no fueron encontradas.")
            return

        monto_dividido = monto / len(tarjetas_verificadas)
        if all(tarjeta.suficiente_monto(monto_dividido) for tarjeta in tarjetas_verificadas):
            for tarjeta in tarjetas_verificadas:
                tarjeta.pagar(monto_dividido)
            print("Se ha pagado todo el monto entre las distintas tarjetas seleccionadas.")
        else:
            print("No es posible pagar el monto con las tarjetas ingresadas.")
    #Metodo para mostrar las tarjetas
    def mostrar_tarjetas(self):
        if not self.__tarjetas:
            print("No tiene tarjetas registradas.")
        for tarjeta in self.__tarjetas:
            print(f"Nombre: {tarjeta.get_nombre()}, Alias: {tarjeta.get_alias()}, Dinero disponible: {tarjeta.get_dinero_disponible()}")
    

#Creacion de la clase de TarjetaCredito
class TarjetaCredito():
    def __init__(self, nombre, alias, dinero_disponible): #En este ejemplo tambien deberia estar otros datos como fecha de vencimiento, contraseña, cvu que se podrian agregar despues como funcionalidad.
        self.__nombre = nombre
        self.__alias = alias
        self.__dinero_disponible = dinero_disponible

    #Metodo getters
    def get_nombre(self):
        return self.__nombre
    
    def get_alias(self):
        return self.__alias
    
    def get_dinero_disponble(self):
        return self.__dinero_disponible
    
    #Metodo pagar y sacar el dinero de la cuenta
    def pagar(self, monto_pagar):
        if self.suficiente_monto(monto_pagar):
            self.__dinero_disponible -= monto_pagar
            print(f"Se ha realizado el pago por el monto de '${monto_pagar}' desde la tarjeta '{self.__nombre}'.")
        else:
            print(f"No es posible realizar el pago desde la tarjeta '{self.__nombre}'")
    
    #Metodo para cobrar una transaccion
    def cobrar(self, monto_cobrar):
        self.__dinero_disponible += monto_cobrar
        print(f"Se ha realizado la transaccion, se han añadido {monto_cobrar} a la cuenta, el balance actual es '${self.__dinero_disponible}'")
    
    #Metodo para considerar si alcanza para pagar o no tiene suficiente monto
    def suficiente_monto(self, monto):
        if self.__dinero_disponible >= monto:
            return True
        else:
            return False
    
    #Metodo para transferir de una tarjeta a otra
    def transferir(self, tarjeta_destino, monto):
        if (self.suficiente_monto(monto)):
            self.pagar(monto)
            tarjeta_destino.cobrar(monto)
            print(f"Transferencia de ${monto} realizada desde '{self.get_nombre()}' a '{tarjeta_destino.get_nombre()}'.")
        else:
            print(f"No hay suficiente dinero disponible para transferir ${monto}.")
    

#Ejemplo de utilizacion de las clases de TarjetaCredito y Cliente
def menu_tarjetas():
    nombre_cliente = input("Ingrese su nombre: ")
    dni_cliente = input("Ingrese su DNI: ")
    cliente = Cliente(nombre_cliente, dni_cliente)

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar una tarjeta de crédito nueva")
        print("2. Quitar una tarjeta de crédito de su cuenta actual")
        print("3. Ver sus tarjetas guardadas y la información")
        print("4. Pagar con una sola tarjeta")
        print("5. Pagar con varias tarjetas")
        print("6. Salir del sistema")

        opcion_menu = int(input("Seleccione una opción: "))

        if opcion_menu == 1:
            nombre_tarjeta = input("Ingrese el nombre de la tarjeta: ")
            alias_tarjeta = input("Ingrese el alias de la tarjeta: ")
            dinero_disponible = float(input("Ingrese el dinero disponible en la tarjeta: "))
            nueva_tarjeta = TarjetaCredito(nombre_tarjeta, alias_tarjeta, dinero_disponible)
            cliente.agregar_tarjeta(nueva_tarjeta)

        elif opcion_menu == 2:
            alias_tarjeta = input("Ingrese el alias de la tarjeta que desea quitar: ")
            cliente.quitar_tarjeta(alias_tarjeta)

        elif opcion_menu == 3:
            cliente.mostrar_tarjetas()

        elif opcion_menu == 4:
            alias_tarjeta = input("Ingrese el alias de la tarjeta con la que desea pagar: ")
            monto = float(input("Ingrese el monto a pagar: "))
            cliente.cobrar_sola(monto, alias_tarjeta)

        elif opcion_menu == 5:
            monto = float(input("Ingrese el monto total a pagar: "))
            print("Ingrese los alias de las tarjetas (máximo 4, separadas por comas):")
            aliases = input().split(',')
            aliases = [alias.strip() for alias in aliases]
            cliente.cobrar_varias(monto, *aliases)

        elif opcion_menu == 6:
            print("Gracias por usar nuestro sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida")
#Utilizacion del menu para el ejemplo
# menu_tarjetas()

#Ejercicio 13
print("EJERCICIO 13")

#Creacion de la clase de mensaje cripto
class MensajeCripto:
    def __init__(self, desplazamiento):
        self.desplazamiento = desplazamiento
        self.alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÑabcdefghijklmnopqrstuvwxyzñ'
        self.longitud_alfabeto = len(self.alfabeto)
    
    def encriptar(self, mensaje):
        mensaje_encriptado = ''
        for caracter in mensaje:
            if caracter in self.alfabeto:
                indice_original = self.alfabeto.index(caracter)
                indice_nuevo = (indice_original + self.desplazamiento) % self.longitud_alfabeto
                mensaje_encriptado += self.alfabeto[indice_nuevo]
            else:
                mensaje_encriptado += caracter
        return mensaje_encriptado
    
    def desencriptar(self, mensaje):
        mensaje_desencriptado = ''
        for caracter in mensaje:
            if caracter in self.alfabeto:
                indice_original = self.alfabeto.index(caracter)
                indice_nuevo = (indice_original - self.desplazamiento) % self.longitud_alfabeto
                mensaje_desencriptado += self.alfabeto[indice_nuevo]
            else:
                mensaje_desencriptado += caracter
        return mensaje_desencriptado

#Ejemplo de utilizacion del ejercicio

# mensaje_cripto = MensajeCripto(desplazamiento=3)

# mensaje_original = "Hola como estas? mi nombre es Tomas Romero."
# mensaje_encriptado = mensaje_cripto.encriptar(mensaje_original)
# print("Mensaje encriptado:", mensaje_encriptado)

# # Desencriptar el mensaje
# mensaje_desencriptado = mensaje_cripto.desencriptar(mensaje_encriptado)
# print("Mensaje desencriptado:", mensaje_desencriptado)

#Ejercicio 14
print("EJERCICIO 14")

class EtiquetaHTML:
    def __init__(self, nombre, contenido='', atributos=''):
        self.nombre = nombre
        self.contenido = contenido
        self.atributos = atributos
    
    def __str__(self):
        apertura = f'<{self.nombre} {self.atributos}>' if self.atributos else f'<{self.nombre}>'
        cierre = f'</{self.nombre}>'
        return f'{apertura}{self.contenido}{cierre}'

#Ejemplo de utilizacion de etiquetas html
# parrafo = EtiquetaHTML('p', 'es un párrafo.', 'class="texto"')
# print(parrafo)

# enlace = EtiquetaHTML('a', 'Haz clic aquí', 'href="https://ejemplo.com"')
# print(enlace)

# lista = EtiquetaHTML('ul',
#     f'{EtiquetaHTML("li", "Elemento 1")} {EtiquetaHTML("li", "Elemento 2")} {EtiquetaHTML("li", "Elemento 3")}'
# )
# print(lista)


#Ejercicio 15
print("EJERCICIO 15")

#Creacion de la clase para binario
class Binario:
    def __init__(self, valor):
        if type(valor) == int:
            # Convertir de decimal a binario y almacenar como cadena
            self.valor = self._decimal_a_binario(valor)
        elif type(valor) == str:
            # Verificar que la cadena contenga solo '0' y '1'
            for caracter in valor:
                if caracter != '0' and caracter != '1':
                    print("Error: La cadena debe contener solo '0' y '1'.")
                    self.valor = '0'
                    return
            self.valor = valor
        else:
            print("Error: El valor debe ser un entero o una cadena de números binarios.")
            self.valor = '0'
    
    def _decimal_a_binario(self, decimal):
        if decimal == 0:
            return '0'
        binario = ''
        while decimal > 0:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
        return binario

    def a_decimal(self):
        decimal = 0
        potencia = 1
        for bit in reversed(self.valor):
            if bit == '1':
                decimal += potencia
            potencia *= 2
        return decimal

    def sumar(self, otro):
        if type(otro) == Binario:
            suma_decimal = self.a_decimal() + otro.a_decimal()
            return Binario(suma_decimal)
        else:
            print("Error: El argumento debe ser una instancia de Binario.")
            return Binario(0)

    def restar(self, otro):
        if type(otro) == Binario:
            resta_decimal = self.a_decimal() - otro.a_decimal()
            if resta_decimal < 0:
                print("Error: La resta da un resultado negativo.")
                return Binario(0)
            return Binario(resta_decimal)
        else:
            print("Error: El argumento debe ser una instancia de Binario.")
            return Binario(0)

    def __str__(self):
        return self.valor

# Ejemplo de uso
# bin1 = Binario("1010")  # Binario 1010 (decimal 10)
# bin2 = Binario(5)       # Decimal 5 convertido a binario (101)
# print(f"Binario 1: {bin1}") 
# print(f"Binario 2: {bin2}") 
# # Convertir a decimal
# print(f"Binario 1 a decimal: {bin1.a_decimal()}") 
# # Sumar
# resultado_suma = bin1.sumar(bin2)
# print(f"Suma: {resultado_suma}")
# # Restar
# resultado_resta = bin1.restar(bin2)
# print(f"Resta: {resultado_resta}")
