# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:43:49 2023

@author: Usuario
"""

import tkinter as tk
root = tk.Tk()

var_opcion = tk.IntVar()  ## Crea una variable de tipo IntVar de Tkinter que se utiliza para vincular widgets radiobutton

tk.Radiobutton(root, text="Opción 1", variable=var_opcion, value=1).pack()
tk.Radiobutton(root, text="Opción 2", variable=var_opcion, value=2).pack()
tk.Radiobutton(root, text="Opción 3", variable=var_opcion, value=3).pack()

label = tk.Label(root)
label.pack()

def seleccionar():
  seleccion = var_opcion.get() ## Obtiene el valor actual almacenado en la variable var_opcion de Tkinter
  label.config(text=f"Seleccionado: Opción {seleccion}")

btn = tk.Button(root, text="Mostrar Selección", command=seleccionar)
btn.pack()

root.mainloop()