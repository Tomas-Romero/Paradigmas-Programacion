# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 19:58:56 2023

@author: Usuario
"""
# Programa 3 - Botón que cambia texto de etiqueta
import tkinter as tk

root = tk.Tk()
root.title("Botón que Cambia Texto")

# Inicialmente el texto de la etiqueta será "Hola mundo"
texto_actual = "Hola mundo"
label = tk.Label(root, text=texto_actual)
label.pack()

def cambiar_texto():
    global texto_actual
    if texto_actual == "Hola mundo":
        texto_actual = "Chau mundo"
    else:
        texto_actual = "Hola mundo"
    label.config(text=texto_actual)

boton = tk.Button(root, text="Cambiar Texto", command=cambiar_texto)
boton.pack()

root.mainloop()
