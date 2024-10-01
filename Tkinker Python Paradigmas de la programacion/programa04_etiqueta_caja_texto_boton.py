# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:06:10 2023

@author: Usuario
"""

# Programa 4 - Entry y Label
import tkinter as tk

root = tk.Tk()
root.title("Ventana Principal")

entry = tk.Entry(root) 
entry.pack()

label = tk.Label(root, text="")
label.pack()

def mostrar_entrada():
    entrada = entry.get()
    label.config(text=entrada)
    
boton = tk.Button(root, text="Boton Mostrar", command=mostrar_entrada)
boton.pack()

root.mainloop()