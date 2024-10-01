# Programa 2 - Etiqueta de texto
import tkinter as tk

root = tk.Tk()  ## Crea una ventana raíz o root, que es la ventana base de la aplicación Tkinter.
root.title("Etiqueta de Texto")   ## modifico la propiedad title

label = tk.Label(root, text="¡Hola Mundo!")  ##Crea un widget Label (etiqueta) como hijo de la ventana root, con el texto "¡Hola Mundo!".
label.pack()  ## muestra la etiquet, Empaqueta el widget Label para mostrarlo en la ventana root.

root.mainloop() ##Inicia el bucle de eventos principal de Tkinter que muestra la ventana y permite la interacción.