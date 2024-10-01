# -*- coding: utf-8 -*-
"""
# Programa 6 - Checkbuttons
"""
import tkinter as tk
root = tk.Tk()
root.title("Checkbuttons") 

var1 = tk.IntVar()
var2 = tk.IntVar()
tk.Checkbutton(root, text="Opción 1", variable=var1).pack()
tk.Checkbutton(root, text="Opción 2", variable=var2).pack()
label = tk.Label(root, text="")
label.pack()

def mostrar():
    texto = "Seleccionado: \n"
    if var1.get() == 1:
        texto += "Opción 1\n"
    if var2.get() == 1:
        texto += "Opción 2"
        
    label.config(text=texto)

boton = tk.Button(root, text="Mostrar", command=mostrar)
boton.pack()
root.mainloop()