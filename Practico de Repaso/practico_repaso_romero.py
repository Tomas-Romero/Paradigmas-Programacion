import random
import numpy as np

#Ejercicio 1
numero_ingresado = float(input("Ingrese un numero para ver si es par o no: "))
def Par_o_impar(self):
    if self % 2 == 0:
        par_impar = "Par"
    else:
        par_impar = "Impar"
    print(f"El numero ingresado es {par_impar}")
Par_o_impar(numero_ingresado)
#Ejercicio 2
def suma(self):
    suma = 0
    for numero in self:
        suma += numero
    return suma
lista = []
for i in range(8):
    lista.append(float(random.randint(1, 500)))
print(f"La suma de los elementos de la lista es: {suma(lista)}")
#Ejercicio 3
def Ejercicio3(self):
    letras = ""
    letras_pares = ""
    letras_impares = ""
    for letra in self:
        letras += (f"{letra}\n")
    for i in range(len(self)):
        if i % 2 == 0:
            letras_pares += (f"{self[i]}\n")
        else:
            letras_impares += (f"{self[i]}\n")
    print(f"Las letras de la frase son: \n{letras}")
    print(f"Las letras en ubicaciones pares son: \n{letras_pares}")
    print(f"Las letras en ubicaciones impares son: \n{letras_impares}")
frase_ingresada = input("Ingrese una frase: ")
Ejercicio3(frase_ingresada)
#Ejercicio 4
def Ejercicio4(lista):
    palabra = ""
    longitud_par = 0
    palabras = []
    caracteres = [" ", ",", "?", "!", "-", "\n"]
    for caracter in lista:
        if  caracter not in caracteres:
            palabra += caracter
        else:
            palabras.append(palabra)
            palabra = ""
    for elemento in palabras:
        if (len(elemento) % 2 == 0) and (len(elemento) != 0):
            longitud_par += 1
    return longitud_par
frase_ingresada_4 = input("Ingrese una palabra para ver cuantas palabras de longitud par hay: ")
print(f"La cantidad de palabras pares en la frase ingresada es de: {Ejercicio4(frase_ingresada_4)} palabras de longitud par")
#Ejercicio 5
nombre_archivo = "cuento.txt"
with open(nombre_archivo, "r") as archivo:
    lineas = archivo.readlines()
    palabras = []
    palabra = ""
    frases = 0
    for linea in lineas:
        caracteres = [" ", ",", "?", "!", "-", "\n", "", "."]
        for caracter in linea:
            if  caracter not in caracteres:
                palabra += caracter
            elif caracter == ".":
                frases += 1
            else:
                if palabra != "":
                    palabras.append(palabra)
                    palabra = ""
                else:
                    palabra = ""
vocales = ["a", "e", "i", "o", "u"]
contador_vocales = 0
for palabra in palabras:
    for caracter in palabra:
        if caracter in vocales:
            contador_vocales += 1
numero_nombres = 0
texto_5 = ""
for elemento in palabras:
    texto_5 += (elemento + " ")
    if elemento == elemento.capitalize():
        print (elemento)
        numero_nombres += 1
print(texto_5)
print(f"La cantidad de palabras que hay en el texto es: {len(palabras)}")
print(f"La cantidad de frases que hay en el texto es: {frases}")
print(f"La cantidad de nombres propios que hay en el texto es: {numero_nombres - frases}")
print(f"La cantidad de vocales que hay en el texto es: {contador_vocales}")
print(f"La cantidad de palabras de longitud par que hay en el texto es: {Ejercicio4(texto_5)}")
print(f"La cantidad de palabras de longitud impar que hay en el texto es: {len(palabras) - Ejercicio4(texto_5)}")

#Ejercicio 6
def Invertir_palabra_1(frase):
    letras_lista = []
    invertida = ""
    for caracter in frase:
        letras_lista.append(caracter)
    while len(letras_lista) != 0:
        invertida += letras_lista.pop()
    return invertida
frase = input("Ingrese una frase para invertirla: ")
print(Invertir_palabra_1(frase))

def Invertir_palabra_2(frase):
    invertida = ""
    for i in range((len(frase)) -1, -1, -1):
        invertida += frase[i]
    return invertida
frase_2 = input("Ingrese una frase para invertirla: ")
print(Invertir_palabra_2(frase_2))

#Ejercicio 7
def Producto_escalar(vector1, vector2):
    producto_escalar = 0
    for i in range(len(vector1)):
        valor1 = vector1[i] * vector2[i]
        producto_escalar += valor1
        valor1 = 0
    return producto_escalar
vector1 = [4, 5, -2]
vector2 = [7, 9, 5]
print("El producto escalar de los vectores brindados son: ", (Producto_escalar(vector1, vector2)))

#Ejercicio 8
lista_ejercicio8 = []
numero_guardar = float(input("Ingrese un número para guardarlo en la lista, ingrese 'q' para no ingresar más números: "))
while numero_guardar != 'q':
        lista_ejercicio8.append(float(numero_guardar))
        numero_guardar = input("Ingrese un número para guardarlo en la lista, ingrese 'q' para no ingresar más números: ")
print(lista_ejercicio8)

#Ejercicio 9
def Signos(vector):
    signos_lista = []
    for numero in vector:
        if numero > 0:
            signos_lista.append(1)
        elif numero < 0:
            signos_lista.append(-1)
        elif numero == 0:
            signos_lista.append(0)
        else:
            signos_lista.append("-")
    return signos_lista
vector = [1, 8, -5, -7, 10, 4, -8, -9, 0, 0]
print(Signos(vector))

#Ejercicio 10
print("""
------------------------------------
Listas en Python:
->Las listas en Python son estructuras de datos versátiles que pueden contener cualquier tipo de objeto, incluso otras listas y objetos complejos.
->Pueden cambiar de tamaño dinámicamente, lo que significa que puedes agregar, eliminar o modificar elementos fácilmente.
->Las listas en Python están implementadas como arrays dinámicos, lo que significa que tienen cierta sobrecarga en términos de memoria y rendimiento en comparación con los arrays estáticos de otros lenguajes.
------------------------------------
Arreglos en Python (numpy arrays):
->Los arrays en Python, especialmente en el contexto de bibliotecas como NumPy, son estructuras de datos más eficientes y especializadas para cálculos numéricos y científicos.
->Están optimizados para realizar operaciones matemáticas y manipulaciones de datos eficientes.
->Los arrays de NumPy son homogéneos, lo que significa que todos sus elementos son del mismo tipo, lo que permite un almacenamiento más eficiente en memoria y operaciones más rápidas.
->Los arrays de NumPy generalmente tienen un tamaño fijo y no pueden cambiar de tamaño dinámicamente como las listas de Python.
------------------------------------""")

#Ejercicio 11
#Creación de vectores y matrices:

# numpy.array(): Crea un array a partir de una lista o tupla.

#Ejemplos
a1 = np.array([1, 2, 3]) #Array de 1 dimension
print(a1)
a2 = np.array([1, 2, 3, 4, 5, 6])
print(a2)
a3 = np.array([[1, 2, 3], [4, 5, 6]]) #Array de 2 dimensiones
print(a3)
a4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a4)

# numpy.zeros(): Crea un array de ceros.
b1 = np.zeros(5) #Si se le da solo 1 valor se hara de 1 fila y ese valor en columnas
print(b1)
b2 = np.zeros([2, 4]) #Si se le da 2 valores, el primero seran las filas y el segundo las columnas
print(b2)
b3 = np.zeros([2, 3, 4]) #Si se le da 3 valores, el primero sera la dimension 3d o "numero de matrices", 
                        #el 2do valor son el numero de filas y el 3ro el numero de columnas
print(b3)

# numpy.ones(): Crea un array de unos.
c1 = np.ones(5) #Si se le da solo 1 valor se hara de 1 fila y ese valor en columnas
print(c1)
c2 = np.ones([2, 4]) #Si se le da 2 valores, el primero seran las filas y el segundo las columnas
print(c2)
c3 = np.ones([2, 3, 4]) #Si se le da 3 valores, el primero sera la dimension 3d o "numero de matrices", 
                        #el 2do valor son el numero de filas y el 3ro el numero de columnas
print(c3)

# numpy.arange(): Crea un array con valores espaciados uniformemente dentro de un intervalo.
d1 = np.arange(10)
print(d1)
d2 = np.arange(3, 15)
print(d2)
d3 = np.arange(2, 3, 0.1)
print(d3)
#np.eye(n, m) defines a 2D identity matrix. The elements where i=j (row index and column index are equal) are 1 and the rest are 0
e1 = np.eye(3)
print(e1)
e2 = np.eye(3, 5) #si se dan 2 valores, el primero son filas y el segundo columnas, y la identidad empieza desde el primer elemento
print(e2)

#numpy.diag puede definir una matriz 2D cuadrada con valores dados a lo largo de la diagonal o, si se le da una matriz 2D, devuelve una matriz 1D que contiene solo los elementos diagonales.
f1 = np.diag([1, 2, 3])
print(f1)
f2 = np.diag([1, 2, 3], 0) #El segundo valor dice donde empieza el valor distinto de 0 en la diagonal
print(f2)
f3 = np.diag([1, 2, 3], 1) #El segundo valor dice donde empieza el valor distinto de 0 en la diagonal y agrega 1 fila vacia
print(f3)
f4 = np.array([[1, 2], [3, 4]])
print(f4)
diagf4 = np.diag(f4) #Al usarlo de esta manera en otra matriz ya creada, solamente devuelve los valores de la diagonal principal
print(diagf4)

#np.block() Se utiliza para unir varios arrays en 1 solo
A = np.ones((2, 2))
B = np.eye(2, 2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))
e1 = np.block([[A, B], [C, D]])
print(e1)

#np.random.randint(0, 10, size=(10, 10)) genera una matriz de tamaño 10x10 con valores enteros aleatorios en 
# el rango de 0 a 9. El primer argumento (0) especifica el límite inferior del rango, el segundo argumento (10) 
# especifica el límite superior del rango (no incluido), y size=(10, 10) especifica las dimensiones de la matriz.

#Ejercicio 12
import numpy as np
matriz10x10 = np.random.randint(0, 100, size=(10,10)) #Se crea una matriz de numeros entre 0 y 100 de tamaño(size) 10x10
print(matriz10x10)
def Suma10x10tradicional(matriz):
    resultado = 0
    for fila in matriz:
        for elemento in fila:
            resultado += elemento
    return resultado
print("Suma total utilizando metodo 'manual': ", Suma10x10tradicional(matriz10x10))
def Sumanumpy(matriz):
    suma_total = np.sum(matriz)
    return suma_total
print("Suma total utilizando numpy: ", Sumanumpy(matriz10x10))

#Ejercicio 13
#Creacion de la matriz de forma de listas anidadas
matriz_enlazadas = [[random.randint(0, 100) for columna in range(6)] for fila in range(6)]
print("Matriz por lista enlazada: ")
for fila in matriz_enlazadas:
    print(fila)
def Suma_diag_tradicional(matriz):
    sum_diag_tradi = 0
    for i in range(len(matriz)):
        for j in range(len(fila)):
            if j == i:
                sum_diag_tradi += matriz[i][j]
    return sum_diag_tradi
def Suma_diag_numpy(matriz):
    sum_diag_numpy = np.trace(matriz)
    return sum_diag_numpy
matriz_numpy = np.random.randint(0, 100, (6,6))
print("Matriz de Numpy: ")
for fila in matriz_numpy:
    print(fila)
print("La sumatoria de la diagonal principal de la matriz por lista enlazadas por metodo de bucles es: ", Suma_diag_tradicional(matriz_enlazadas))
print("La sumatoria de la diagonal principal de la matriz por lista enlazadas por metodo de Numpy es: ", Suma_diag_numpy(matriz_enlazadas))
print("La sumatoria de la diagonal principal de la matriz por numpy por metodo de bucles es: ", Suma_diag_tradicional(matriz_numpy))
print("La sumatoria de la diagonal principal de la matriz por numpy por metodo de Numpy es: ", Suma_diag_numpy(matriz_numpy))

#Ejercicio 14
matriz_diag_6 = np.diag([1,2,3,4,5,6])
print(matriz_diag_6)
with open("matriz.txt", "w") as archivo:
    for i in range(len(matriz_diag_6)):
        fila = str(matriz_diag_6[i])
        archivo.write(fila + "\n")
