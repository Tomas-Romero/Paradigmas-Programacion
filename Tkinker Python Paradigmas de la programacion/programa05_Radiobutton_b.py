# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:06:56 2023

@author: Usuario
"""

# Programa 5 - Radio Buttons
import tkinter as tk

root = tk.Tk()
root.title("Radio Buttons")

opcion = tk.IntVar()

tk.Radiobutton(root, text="Opción 1", variable=opcion, value=1).pack()
tk.Radiobutton(root, text="Opción 2", variable=opcion, value=2).pack()

label = tk.Label(root, text="")
label.pack()

def seleccion():
    if opcion.get() == 1:
        label.config(text="Seleccionó Opción 1")
    else:
        label.config(text="Seleccionó Opción 2")
        
boton = tk.Button(root, text="Mostrar Selección", command=seleccion)
boton.pack()

root.mainloop()